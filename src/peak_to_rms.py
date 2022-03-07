import argparse
import utils as ut
from pathlib import Path

script_path = Path(__file__).resolve()


def main(voltage: float, invert: bool):
    if invert:
        v_peak = round(ut.rms_to_peak(voltage), 3)
        print(f"{voltage} Vrms -> {v_peak} Vpeak")
    else:
        v_rms = round(ut.peak_to_rms(voltage), 3)
        print(f"{voltage} Vpeak -> {v_rms} Vrms")


def handle_args() -> dict:
    parser = argparse.ArgumentParser(
        prog=script_path.name,
        description="Converts dBFS levels to voltage using EBU R68 or SMPT R155 standards.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "voltage",
        type=float,
        help="Voltage peak value or RMS if invert option is on.",
    )
    parser.add_argument(
        "-i",
        "--invert",
        help=f"Invert functionality (rms to peak).",
        action="store_true",
        required=False,
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = handle_args()
    main(**vars(args))
