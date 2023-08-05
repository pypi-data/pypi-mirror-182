#!/usr/bin/env python3
import argparse
import csv
import datetime
import sys
import time
from importlib.metadata import version
from pathlib import Path
from pprint import pprint
from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
import serial.tools.list_ports
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import MultipleLocator

from .yamspy import MSPy

LIBRARY_NAME = "assault_and_battery"
try:
    VERSION = version(LIBRARY_NAME)
except Exception:
    VERSION = "0.0.0u"


def plot(
    filename: Path,
    title: Optional[str] = None,
    skip_rows: int = 0,
    min_amps: float = 0,
    show_plot: bool = False,
):
    """Plot the results of a sampling from a CSV file."""
    with filename.open() as csvfile:
        reader = csv.reader(csvfile)
        # Skip the first two rows, as they're headers, plus whatever is
        # requested.
        for _ in range(2 + skip_rows):
            reader.__next__()

        data = []
        prev_voltage = 1e10
        for raw_row in reader:
            row = [float(x) for x in raw_row]
            timestamp, voltage, cell_voltage, amperage, consumed = row
            if voltage >= prev_voltage or amperage < min_amps:
                # Only add an item if the voltage has dropped.
                continue
            data.append((cell_voltage, amperage, int(consumed * 1000)))
            prev_voltage = voltage

    pprint(data)

    voltages_array = np.array([x[0] for x in data])
    amperage_array = np.array([x[1] for x in data])
    ah_consumed_array = np.array([x[2] / 1000 for x in data])

    title = title if title else "Discharge curve"
    plt.title(title)
    plt.xlabel("Charge consumed (Ah)")

    ax = plt.gca()
    ax.set_ylabel("Cell voltage (V)")
    line1 = ax.plot(
        ah_consumed_array,
        voltages_array,
        label="Voltage",
    )
    ax.set_ylim([2.7, 4.3])

    ax.xaxis.set_major_locator(MultipleLocator(0.5))
    ax.yaxis.set_major_locator(MultipleLocator(0.2))
    ax.xaxis.set_minor_locator(AutoMinorLocator(4))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))

    ax.grid(which="major", alpha=0.5, linestyle="--")
    ax.grid(which="minor", alpha=0.3, linestyle=":")

    ax2 = ax.twinx()
    ax2.set_ylabel("Current drawn (A)")
    line2 = ax2.plot(
        ah_consumed_array,
        amperage_array,
        label="Current",
        linestyle="--",
        color="#ff7f00",
    )
    ax2.set_ylim([0, max(amperage_array) * 1.1])

    lines = line1 + line2
    plt.legend(lines, [line.get_label() for line in lines], loc="best")
    outfile = filename.with_suffix(".png")
    plt.savefig(outfile, dpi=150)
    if show_plot:
        plt.show()

    print(f"Wrote {outfile}.")


def discover_socket() -> str:
    """Try to autodiscover the socket the craft is on."""
    devices = [x.__dict__ for x in serial.tools.list_ports.comports()]
    for port in devices:
        manufacturer = port.get("manufacturer", "")
        hwid = port.get("hwid", "")
        if ("INAV" in manufacturer) or ("1209:5741" in hwid):
            return port["device"]

    if not devices:
        sys.exit(
            "Could not autodetect your socket, please specify it "
            "manually with `--socket`."
        )

    # Just return the first device, as we're out of options.
    return devices[0]["device"]


class Sampler:
    def __init__(self, port=None):
        if port is None:
            port = discover_socket()
            print(f"Autodiscovered socket: {port}.")
        self._num_cells = 0
        self._board = MSPy(
            device=port,
            baudrate=115200,
        )
        self._board.__enter__()

    def _get_data(self):
        self._board.send_RAW_msg(MSPy.MSPCodes["MSPV2_INAV_ANALOG"], data=[])
        dataHandler = self._board.receive_msg()
        self._board.process_recv_data(dataHandler)
        data = {
            "cell_count": self._board.ANALOG["cell_count"],
            "voltage": self._board.ANALOG["voltage"],
            "amperage": self._board.ANALOG["amperage"],
            "ah_drawn": self._board.ANALOG["mAhdrawn"] / 1000,
        }
        return data

    def begin(self, filename):
        with open(filename, "w") as output:
            output.write(f"# Number of cells: {self._num_cells}\n")
            output.write("Time,Voltage,Volts per cell,Amperage,Ah consumed\n")

            time_start = time.time()
            try:
                while True:
                    data = self._get_data()
                    voltage = data["voltage"]
                    amperage = data["amperage"]
                    consumed = data["ah_drawn"]
                    duration = int(time.time() - time_start)
                    volts_per_cell = voltage / data["cell_count"]
                    output.write(
                        f"{duration},{voltage},{volts_per_cell:.2f},"
                        f"{amperage},{consumed}\n"
                    )
                    output.flush()

                    print(
                        str(
                            {
                                "duration": duration,
                                "voltage": voltage,
                                "amperage": amperage,
                                "mah_consumed": int(consumed * 1000),
                                "volts_per_cell": round(volts_per_cell, 2),
                            }
                        )
                        + ("\a" if volts_per_cell <= 2.8 else "")
                    )
                    time.sleep(1)
            except KeyboardInterrupt:
                pass
        self.close()

    def close(self):
        self._board.__exit__(None, None, None)


def sample(port=None, name=None):
    s = Sampler(port)
    ts = datetime.datetime.today().isoformat()[:19].replace("T", "_").replace(":", "-")
    filename = f"curve_{name}_{ts}.csv" if name else f"curve_{ts}.csv"
    print(f"Sampling to {filename}...")
    s.begin(filename)
    s.close()
    print("Done!")


def cli():
    parser = argparse.ArgumentParser(
        prog=LIBRARY_NAME, description="Plot the discharge curve."
    )
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {VERSION}"
    )
    subparsers = parser.add_subparsers(
        required=True, dest="command", help="Supported subcommands."
    )

    parser_sample = subparsers.add_parser(
        "sample",
        help="Sample the battery while it is being discharged.",
    )
    parser_sample.add_argument(
        "-n",
        "--name",
        help="Add a name snippet to the CSV filename.",
    )
    parser_sample.add_argument(
        "-p",
        "--port",
        help="The port to talk to the FC on (default: autodetect).",
    )

    parser_plot = subparsers.add_parser(
        "plot",
        help="Plot a sampled CSV.",
    )
    parser_plot.add_argument(
        "csv_filename",
        help="The filename of the CSV.",
    )
    parser_plot.add_argument(
        "-t",
        "--title",
        help="Add a title snippet to the graph.",
    )
    parser_plot.add_argument(
        "-m",
        "--min-amps",
        default=0,
        type=float,
        help="Ignore any data point where the load is less than this many A,"
        " to ignore any data points before there was load.",
    )
    parser_plot.add_argument(
        "-s",
        "--skip-rows",
        default=0,
        type=int,
        help="Skip the specified number of rows.",
    )
    parser_plot.add_argument(
        "-w",
        "--show-plot",
        action="store_true",
        help="Show the plot when done.",
    )

    args = parser.parse_args()

    if args.command == "sample":
        sample(port=args.port, name=args.name)
    elif args.command == "plot":
        plot(
            Path(args.csv_filename),
            title=args.title,
            skip_rows=args.skip_rows,
            min_amps=args.min_amps,
            show_plot=args.show_plot,
        )


if __name__ == "__main__":
    cli()
