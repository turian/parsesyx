import hashlib
import json
import os
import os.path
import random

import numpy as np
import pedalboard
import torch
import torchaudio
from db.dexed_core_params import (
    INSTRUMENT_PATH,
    DexedParams,
    DexedParamsDatabase,
    parameter_names,
    parameter_valid_values,
)
from db.note import Note, NoteDatabase
from globals import SAMPLE_RATE
from mido import Message
from slugify import slugify
from tqdm.auto import tqdm
from typeguard import typechecked


def dexed_play_audio(note: Note, params: DexedParams, sample_rate: int = SAMPLE_RATE):
    print(params.valuedict)
    instrument = pedalboard.VST3Plugin(INSTRUMENT_PATH)
    for name, raw_value in params.rawvaluedict.items():
        instrument.__getattr__(name).raw_value = raw_value

    print(instrument.parameters)  # Debugging print statement

    # Generate audio
    audio = instrument(
        [
            Message("note_on", note=note.note, velocity=note.velocity),
            Message("note_off", note=note.note, time=note.hold_duration),
        ],
        duration=note.duration,
        sample_rate=sample_rate,
    )

    return audio


def dexed_save_audio(
    note: Note,
    params: DexedParams,
    sample_rate: int = SAMPLE_RATE,
    verbose: bool = False,
):
    audio = dexed_play_audio(note, params, sample_rate)
    # If the audio is silent, don't save it
    if np.all(audio == 0):
        return
    audio_tensor = torch.tensor(audio * 32767, dtype=torch.int16)
    hsh = hashlib.sha256(audio).hexdigest()[:4]
    if not os.path.exists("audio"):
        os.makedirs("audio")
    filename = f"audio/dexed/{slugify(params.preset_name)}/note-{note.id}/{hsh}.wav"
    # Create directories if they don't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    torchaudio.save(filename, audio_tensor, sample_rate=SAMPLE_RATE)
    open(filename + ".json", "w").write(
        json.dumps({"note": note.to_json(), "params": params.to_json()}, indent=2)
    )
    if verbose:
        print(f"Saved audio to {filename}")


def generate_random_sounds(k):
    random.seed()
    note_db = NoteDatabase()
    params_db = DexedParamsDatabase()

    note_ids = note_db.all_ids()
    params_ids = params_db.all_ids()

    for i in tqdm(range(k), total=k):
        random_note = note_db[random.choice(note_ids)]
        random_params = params_db[random.choice(params_ids)]

        dexed_save_audio(random_note, random_params, verbose=False)


if __name__ == "__main__":
    generate_random_sounds(41666)
