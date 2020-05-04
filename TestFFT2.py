from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as plt

#https://www.ritchievink.com/blog/2017/04/23/understanding-the-fourier-transform-by-example/

print('FFT -- is ')
#take a simple periodic function, sin(10 × 2πt), you can view it as a wave:
#10  # Frequency, in cycles per second, or Hertz

t = np.linspace(0, 0.5, 500)
s = np.sin(40 * 2 * np.pi * t) + 0.5 * np.sin(90 * 2 * np.pi * t)
#s = np.sin(10 * 2 * np.pi * t)

plt.ylabel("Amplitude")
plt.xlabel("Time [s]")
plt.plot(t, s)
plt.show()


# to show FFT
fft = np.fft.fft(s)

for i in range(2):
    print("Value at index {}:\t{}".format(i, fft[i + 1]), "\nValue at index {}:\t{}".format(fft.size -1 - i, fft[-1 - i]))



fft = np.fft.fft(s)
T = t[1] - t[0]  # sampling interval
N = s.size

# 1/T = frequency
f = np.linspace(0, 1 / T, N)

plt.ylabel("Amplitude")
plt.xlabel("Frequency [Hz]")
plt.bar(f[:N // 2], np.abs(fft)[:N // 2] * 1 / N, width=1.5)  # 1 / N is a normalization factor
plt.show()

