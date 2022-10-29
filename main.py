from re import I
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
import scipy
from functions import *
ecg = electrocardiogram()
print(ecg)
        
fs = 360
time = np.arange(ecg.size) / fs
# plt.plot(time, ecg)
# plt.xlabel("time in s")
# plt.ylabel("ECG in mV")
# plt.xlim(0, 10)
# plt.ylim(-1, 3.0)

x = electrocardiogram() [2000:10000]
peaks, _ = find_peaks(x, prominence=(0.6,None))
plt.plot(x)
plt.plot(peaks, x[peaks], "x")
RRDistance=distancefinder(peaks)
print("SDNN = " + str(np.std(RRDistance)))
NN50=NNCounter(peaks,50)
pNN50=NN50/len(peaks)
RMSSD=rmsValue(RRDistance,len(RRDistance))
print("pNN50 = " + str(pNN50))
print("RMSSD = " + str(RMSSD))


#plt.show()



