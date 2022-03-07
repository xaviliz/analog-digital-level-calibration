# Analog Digital Level Calibration

This repository contains some explanations and functionalities to calibrate digital to analog reference levels using [EBU R68](https://tech.ebu.ch/docs/r/r068.pdf) or [SMPT RP155](https://ieeexplore.ieee.org/document/7291101) [1] standard and Dolby calibration used in [K-System](http://www.ranchstudio.com/student/bob%20katz%20levels.pdf) [2, 3], which map -20dBFS(RMS) to 0VU or +4dBu in professional equipment.

## Table of contents

- [Analog Digital Level Calibration](#analog-digital-level-calibration)
  - [Table of contents](#table-of-contents)
  - [General Info](#general-info)
    - [Balanced and unbalanced signals](#balanced-and-unbalanced-signals)
  - [Setup](#setup)
  - [Usage](#usage)
    - [Level list](#level-list)
  - [Converters](#converters)
    - [dBFS to Volts](#dbfs-to-volts)
    - [Volts peak to Volts RMS](#volts-peak-to-volts-rms)
  - [References](#references)

## General Info

This repository provides a way to map digital to analog level scaling (dBFS to dBu). It might be useful to sample audio gear (referenced to voltage or dBu) using a soundcard with digital level scaling (dBFS). Also it provides some functionalities to understand the level conversion and references between dBFS and dBu units using different standards (*EBU R68*, *SMPTE RP155* or a customized one).

Currently the soundcard's manufacturer don't use EBU R68 or SMPTE RP155 standards. However they always provide a **MAXIMUM OUTPUT LEVEL** in dBu that we can use to map signals from a dBFS scale.

Here a list with different customized output level standards in different soundcards:

| Manufacturer | Model | Maximum Output Level |
| ------------ | ----- | ---------------------|
| Focusrite | Scarlet 2i2 | +10dBu|
| RME | UC | +2dBV, +13dBu and +19dBu |
| UA | Apollo Twin MKII | +20.2dBu|
| Audient | id4 | +12dBu |
| Avid | HD I/O | +22dBu

The table below shows only AVID HD I/O is following the SMPTE RP155 standard.
It is clear the rest of manufacturers are applying customized standards that can generate differences in voltage levels if you reproduce the same signal with different soundcard.

When we want to sample audio gear with a correlated scaling we should bear in mind the specifications provided by the manufacturer and apply the maximum output level to the converters of this repository.

### Balanced and unbalanced signals

Obviously it is different to sample a processor prepared for *TRS* cable (balanced signals) than an instrument like a synthesizer which are prepared for *TS* cables (unbalanced signals). Using TS cables will provide **-6dB** of the maximum output level.

## Setup

The `requirements.txt` file contains the Python modules necessary for this project. We suggest to create a virtual environment to have a clean installation.

To build a virtual environment, you might use `venv`,

```bash
python3 -m venv env
```

For installing packages in the virtual environment:

1. Activate your `env`:

```bash
source env/bin/activate
```

2. Install Python packages:

```bash
pip install -r requirements.txt
```

## Usage

Here some examples to display the level table, which maps dBFS -> dBu -> Volts

### Level list

`src/level_list.py` generates a list/table to display the level mapping between dBFS, dBu and Volts.

```bash
python level_list.py
>>> SMPTE_RP155
    dBFS  dBu   Volts
0      0   24  12.283
1     -1   23  10.947
2     -2   22   9.757
3     -3   21   8.696
4     -4   20   7.750
5     -5   19   6.907
6     -6   18   6.156
...
```

You can also specify the bottom level and the standard to use (SMPTE RP155 by default):

```bash
python level_list.py -b -58 -s ebu_r6
```

## Converters

Sometimes, we also need to have some reference between the different scalings: dBFs-> dBu, Vpeak -> Vrms (for sinusoidal signal)

### dBFS to Volts

```bash
python dbfs_to_volts.py -20
>>> -20.0 dBFS -> 4.0 dBu -> 1.228 V
>>> 1.228 Vpeak -> 0.869 Vrms
```

or Volts to dBFS using `-i` flag

```bash
python dbfs_to_volts.py 1.2283 -i
>>> 1.228 V -> 4.0 dBu -> -20.0 dBFS
```

### Volts peak to Volts RMS

```bash
python peak_to_rms.py 1.228
>>> 1.228 Vpeak -> 0.868 Vrms
```

or RMS to peak-to-peak:

```bash
python peak_to_rms.py 0.868 -i
>>> 0.868 Vrms -> 1.228 Vpeak
```

## References

"RP 155:2014 - SMPTE Recommended Practice - Reference Levels for Analog and Digital Audio Systems," in RP 155:2014 , vol., no., pp.1-7, 29 Dec. 2014, doi: 10.5594/SMPTE.RP155.2014.

Katz, B. (2000). Integrated approach to metering, monitoring, and leveling practices, part 1: Two-channel metering. Journal of the Audio Engineering Society, 48(9), 800-809.

Katz, B., & Katz, R. A. (2003). Mastering audio: the art and the science. Butterworth-Heinemann.

Brixen, E. B. (2020). Audio Metering: Measurements, Standards, and Practice. Focal Press.
