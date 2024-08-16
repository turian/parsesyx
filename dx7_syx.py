# Adapted from https://github.com/Nintorac/NeuralDX7/

import glob
from functools import reduce
from itertools import chain
from pathlib import Path

import bitstruct
import mido
import numpy as np
from tqdm import tqdm as tqdm

from dx7_constants import (
    ARTIFACTS_ROOT,
    N_OSC,
    N_VOICES,
    VOICE_KEYS,
    VOICE_PARAMETER_RANGES,
    header_bytes,
    header_struct,
    take,
    verify,
    voice_bytes,
    voice_struct,
)

# %%


def consume_syx(path):
    path = Path(path)
    try:
        preset = mido.read_syx_file(path.as_posix())[0]
    except IndexError as e:
        return None
    except ValueError as e:
        return None
    if len(preset.data) == 0:
        return None

    def get_voice(data):

        unpacked = voice_struct.unpack(data)

        if not verify(unpacked, VOICE_PARAMETER_RANGES):
            return None

        return unpacked

    get_header = header_struct.unpack
    sysex_iter = iter(preset.data)

    try:
        header = get_header(bytes(take(sysex_iter, len(header_bytes))))
        yield from (
            get_voice(bytes(take(sysex_iter, len(voice_bytes))))
            for _ in range(N_VOICES)
        )
    except RuntimeError:
        return None


if __name__ == "__main__":
    preset_paths = glob.glob("DX7_AllTheWeb/**/*syx", recursive=True)

    for p in preset_paths:
        for v in consume_syx(p):
            print(v)
