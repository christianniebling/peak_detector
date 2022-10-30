import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

N = 600

T = 1.0 / 800.0

x = np.linspace(0.0, N*T, N,)
y = np.sin(50.0 * 2.0 * np.pi*x) 
yf = fft(y)
xf = fftfreq(N, T)

plt.plot(xf, 1/N * np.abs(yf))
plt.grid()
plt.show()