from scipy.fftpack import fft, ifft
import numpy as np

#https://www.ritchievink.com/blog/2017/04/23/understanding-the-fourier-transform-by-example/
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
y = fft(x)
print(y)
# array([ 4.5       +0.j        ,  2.08155948-1.65109876j,    -1.83155948+1.60822041j, -1.83155948-1.60822041j,     2.08155948+1.65109876j])

print('sum is ',x.sum())
print('average is ', np.average(x))

print('abs is ',np.abs(x))

z= np.abs(x)
print('abs-sum is ',z.sum())
print('average is ', np.average(z))


yinv = ifft(y)
print(yinv)
#array([ 1.0+0.j,  2.0+0.j,  1.0+0.j, -1.0+0.j,  1.5+0.j])



# Number of sample points
N = 1600
# sample spacing
T = 1.0 / 500.0
x = np.linspace(0.0, N*T, N)
#y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
import matplotlib.pyplot as plt
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()

#to show spectrogram ,,this will help to see time and frequency data in one plot.
from scipy import signal

M =1024
freqs, times, Sx = signal.spectrogram (x, fs=T, window='hanning', nperseg=1024, noverlap=M - 100, detrend=False, scaling='spectrum')

plt.pcolormesh(times, freqs *100000 , 10 * np.log10(Sx), cmap='viridis')
plt.pcolormesh(times, freqs  , 10 * np.log10(Sx), cmap='viridis')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

