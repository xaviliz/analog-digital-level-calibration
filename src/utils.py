from enum import Enum
import math


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(str, cls))

    def __str__(self):
        return str(self.name.lower())


class Standard(ExtendedEnum):
    EBU_R68 = "ebu_r68"
    SMPTE_RP155 = "smpte_rp155"


def dbfs_to_dbu(dbfs: float, standard: str = "smpte_rp155") -> float:
    if standard == str(Standard.SMPTE_RP155):
        dbu = dbfs + 24
    elif standard == str(Standard.EBU_R68):
        dbu = dbfs + 18
    else:
        raise ValueError(
            f"Undefined standard: {standard}. Choices: {Standard.list()}"
        )
    return dbu


def dbu_to_dbfs(dbu: float, standard: str = None) -> float:
    if standard == str(Standard.SMPTE_RP155):
        dbfs = dbu - 24
    elif standard == str(Standard.EBU_R68):
        dbfs = dbu - 18
    else:
        raise ValueError(
            f"Undefined standard: {standard}. Choices: {Standard.list()}"
        )
    return dbfs


def dbu_to_volts(dbu: float) -> float:
    return 10 ** (dbu / 20) * 0.775


def volts_to_dbu(volts: float) -> float:
    return 20 * math.log10(volts / 0.775)


# assuming a sinusoid as a test signal
def peak_to_rms(volts_pp: float) -> float:
    return volts_pp / math.sqrt(2)


def rms_to_peak(volts_rms: float) -> float:
    return volts_rms * math.sqrt(2)


if __name__ == "__main__":
    dbfs = -20
    dbu = dbfs_to_dbu(dbfs)
    voltage = round(dbu_to_volts(dbu), 3)
    print(f"{dbfs} dBFS -> {dbu} dBu -> {voltage} V")
    v_rms = round(peak_to_rms(voltage), 3)
    print(f"{voltage} Vpp -> {v_rms} Vrms")
