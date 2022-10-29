from re import I
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import electrocardiogram

ecg = electrocardiogram()
print(ecg)

fs = 360
time = np.arange(ecg.size) / fs
plt.plot(time, ecg)
plt.xlabel("time in s")
plt.ylabel("ECG in mV")
plt.xlim(9, 10.2)
plt.ylim(-1, 1.5)
plt.show()