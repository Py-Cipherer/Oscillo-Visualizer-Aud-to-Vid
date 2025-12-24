import librosa
import numpy as np

y, sr = librosa.load("audio/input.m4a")
rms = librosa.feature.rms(y=y)[0]
rms = np.convolve(rms, np.ones(5)/5, mode="same")

np.save("audio/energy.npy", rms)
print("Audio energy extracted")
