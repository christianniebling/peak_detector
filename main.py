from re import I
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.misc import electrocardiogram

ecg = electrocardiogram()
ecg_size = ecg.size
ratio = 1/100
ecg = ecg[:int(ecg_size * ratio)]

fs = 360
time = np.arange(ecg.size) / fs
plt.plot(time, ecg)
plt.xlabel("time in s")
plt.ylabel("ECG in mV")
plt.show()

peaks = scipy.signal.find_peaks(ecg)
print(peaks)