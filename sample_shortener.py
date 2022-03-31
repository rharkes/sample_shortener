import soundfile as sf
from pathlib import Path
import numpy as np

notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
start = ['F', '0']
end = ['C', '7']
vel = 'Mp'
pth = Path(r'D:\github_reps\SplendidGrandPiano\Samples')

octave = start[1]
note = start[0]
samplerate = 44100
data = np.zeros((samplerate, 2))
while True:
    file = Path(pth, ''.join([vel, ' ', note, octave, '.flac']))
    file_out = Path(Path.cwd(), 'samples', file.stem + '.wav')
    file_out.parent.mkdir(exist_ok=True)
    if file.exists():
        data, samplerate = sf.read(file)
        print(f"{file.stem} exists")
    else:
        print(f"{file.stem} not exists")
        samplerate = int(samplerate * 2**(1/12))  # up the previous note by a semitone
    data_sh = data[0:samplerate, 1]
    fadeout = np.linspace(1, 0, samplerate)
    data_sh *= fadeout
    sf.write(file_out, data_sh, samplerate)
    if note == end[0] and octave == end[1]:
        break
    if note == 'B':
        octave = str(int(octave) + 1)
    note = notes[(notes.index(note)+1) % len(notes)]
