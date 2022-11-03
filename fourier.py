import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

# Number of Samples
N = 1000

# Frequency of sampling 
fs = 2 # Hz

# Frequency of the wave
f = 1

# Time period of sampling
T = 1 / fs

print("Duration is: " + str(N*T))

# the start is 0 seconds
# the stop is N*T seconds
# the number of samples is N
x = np.linspace(0, N*T, N)

# y = f Hz sine wave
y = np.sin(2 * np.pi * f * x) 

# Plot in the time domain
plt.plot(x, y)
plt.grid()

# Take the fourier
yf = fft(y)
xf = fftfreq(N, T)

# Plot in the frequency domain
plt.figure()
plt.plot(xf, 1/N * np.abs(yf))
plt.grid()
plt.show()