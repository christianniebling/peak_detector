import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import ZoomFFT
from scipy.fft import fft

t = np.linspace(0, 1, 1021)
y = np.cos(2*np.pi*15*t)
f1, f2 = 5, 27
transform = ZoomFFT(len(y), [f1, f2], len(y), fs=1021)
Y = transform(y)
f = np.linspace(f1, f2, len(y))
plt.plot(f, np.log10(np.abs(Y)))
plt.show()
