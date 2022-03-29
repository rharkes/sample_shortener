import soundfile as sf
from pathlib import Path
import numpy as np

pth = Path(r'D:\github_reps\SplendidGrandPiano\Samples')
samples = [x for x in pth.glob('Mp *.flac')]
for sample in samples:
    data, samplerate = sf.read(sample)
    data = data[0:samplerate, 1]
    fadeout = np.linspace(1, 0, samplerate)
    data *= fadeout
    pth_out= Path(Path.cwd(), 'samples' ,sample.stem + '.wav')
    pth_out.parent.mkdir(exist_ok=True)
    sf.write(pth_out, data, samplerate)
