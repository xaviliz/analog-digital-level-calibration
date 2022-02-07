import argparse
import utils as ut
from pathlib import Path

script_path = Path(__file__).resolve()


def dbfs_to_voltage(dbfs: float, standard: ut.Standard) -> float:
    dbu = ut.dbfs_to_dbu(dbfs, standard=standard)
    v_rms = ut.dbu_to_volts(dbu)
    v_peak = ut.rms_to_peak(v_rms)
    print(f"{dbfs} dBFS -> {dbu} dBu -> {round(v_rms, 3)} Vrms")
    print(f"{round(v_rms, 3)} Vrms -> {round(v_peak, 3)} Vpeak")


def voltage_to_dbfs(v_rms: float, standard: ut.Standard) -> float:
    if v_rms < 0:
        raise ValueError(f"Voltage must be a positive value: {v_rms}Vrms")
    dbu = ut.volts_to_dbu(v_rms)
    dbfs = ut.dbu_to_dbfs(dbu, standard)
    print(
        f"{round(v_rms, 3)} V -> {round(dbu, 3)} dBu -> {round(dbfs, 3)} dBFS"
    )


def main(value: float, standard: ut.Standard, invert: bool) -> None:
    if invert:
        voltage_to_dbfs(value, standard)
    else:
        dbfs_to_voltage(value, standard)


def handle_args() -> dict:
    parser = argparse.ArgumentParser(
        prog=script_path.name,
        description="Converts dBFS levels to voltage using EBU R68 or SMPT R155 standards.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "value", type=float, help="Levels in decibels (dbFS or Vpp)"
    )
    parser.add_argument(
        "-s",
        "--standard",
        type=str,
        help="Standard scaling levels.",
        choices=ut.Standard.list(),
        default=str(ut.Standard.SMPTE_RP155),
    )
    parser.add_argument(
        "-i",
        "--invert",
        help=f"Invert functionality (VRMS to dBFS).",
        action="store_true",
        required=False,
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = handle_args()
    main(**vars(args))
