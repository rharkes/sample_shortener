"""
Generates samples for PianOil (https://github.com/nicolasbrailo/PianOli)
"""
import soundfile as sf
from pathlib import Path
import numpy as np
from scipy.interpolate import interp1d

notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
start = ['C', '3']
end = ['B', '4']
vel = 'vL'
pth = Path(r'\\samples')  # set the directory here, and set the naming scheme for the filenames on line 22

octave = start[1]
note = start[0]
samplerate = 44100
data = np.zeros((samplerate, 2))
Path(Path.cwd(), 'samples').mkdir(exist_ok=True)
i = 0
while True:
    file = Path(pth, ''.join([note, octave, vel, '.flac']))
    file_out = Path(Path.cwd(), 'samples', f"n{i:02}.wav")
    i += 1
    if file.exists():
        data, samplerate = sf.read(file)
        data = data[:, 1]
        print(f"{file.stem} exists")
    else:
        print(f"{file.stem} not exists")
        org_x = np.arange(0, data.shape[0], 1)
        func = interp1d(org_x, data, 'cubic')
        interp_x = np.arange(0, data.shape[0] - 1, (2 ** (1 / 12)))
        data = func(interp_x)
    data_sh = data[0:samplerate]
    fadeout = np.linspace(1, 0, samplerate)
    data_sh *= fadeout
    sf.write(file_out, data_sh, samplerate)
    if note == end[0] and octave == end[1]:
        break
    if note == 'B':
        octave = str(int(octave) + 1)
    note = notes[(notes.index(note) + 1) % len(notes)]
