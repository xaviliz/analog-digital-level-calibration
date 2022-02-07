import argparse
from IPython.display import display
import numpy as np
import pandas as pd
from pathlib import Path
import utils as ut

script_path = Path(__file__).resolve()


def main(bottom: int, standard: ut.Standard) -> None:
    dbfs_list = np.arange(bottom, 1)[::-1]
    dbu_list = [ut.dbfs_to_dbu(dbfs, standard) for dbfs in dbfs_list]
    voltage_list = [round(ut.dbu_to_volts(dbu), 3) for dbu in dbu_list]

    levels_dict = {"dBFS": dbfs_list, "dBu": dbu_list, "Volts": voltage_list}

    df = pd.DataFrame(levels_dict)
    print(f"\t{standard.upper()}")
    display(df)


def handle_args() -> dict:
    parser = argparse.ArgumentParser(
        prog=script_path.name,
        description="Converts dBFS levels to voltage using EBU R68 or SMPT R155 standards.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-b",
        "--bottom",
        type=int,
        help="Bottom level in table in dBFS.",
        default=-35,
    )
    parser.add_argument(
        "-s",
        "--standard",
        type=str,
        help="Standard scaling levels.",
        choices=ut.Standard.list(),
        default=str(ut.Standard.SMPTE_RP155),
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = handle_args()
    main(**vars(args))
