#https://www.oreilly.com/library/view/elegant-scipy/9781491922927/ch04.html
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

rate, audio = wavfile.read('BaldEagle.wav')

print(audio.shape)

#convert to mono by averaging the left and right channels.
#audio = np.mean(audio, axis=1)

N = audio.shape[0]
L = N / rate

print(f'Audio length: {L:.2f} seconds')

f, ax = plt.subplots()
ax.plot(np.arange(N) / rate, audio)
ax.set_xlabel('Time [s]')
ax.set_ylabel('Amplitude [unknown]');
plt.show()


from skimage import signal

freqs, times, Sx = signal.spectrogram(audio, fs=rate, window='hanning',
                                      nperseg=1024, noverlap=M - 100,
                                      detrend=False, scaling='spectrum')

f, ax = plt.subplots(figsize=(4.8, 2.4))
ax.pcolormesh(times, freqs / 1000, 10 * np.log10(Sx), cmap='viridis')
ax.set_ylabel('Frequency [kHz]')
ax.set_xlabel('Time [s]');

plt.show()



