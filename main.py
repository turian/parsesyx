# Adapted from https://github.com/Nintorac/NeuralDX7/

import glob
import json
import os.path

from utils import consume_syx

if __name__ == "__main__":
    preset_paths = sorted(glob.glob("DX7_AllTheWeb/**/*syx", recursive=True))

    for p in preset_paths:
        print(p)
        if not os.path.isfile(p):
            continue
        for v in consume_syx(p):
            print(json.dumps(v))
