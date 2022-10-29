from re import I
from statistics import stdev
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
import scipy
from functions import *
ecg = electrocardiogram()
print(ecg)
        
fs = 360
time = np.arange(ecg.size) / fs
#plt.plot(time, ecg)
# plt.xlabel("time in s")
# plt.ylabel("ECG in mV")
# plt.xlim(0, 10)
# plt.ylim(-1, 3.0)

x = electrocardiogram() [2000:20000]
time = np.arange(x.size) / fs
peaks, _ = find_peaks(x, height = 0.2, threshold = None, distance = 100, prominence=(0.7,None), width=None, wlen=None, rel_height=None, plateau_size=None)
# peaks = time in x where peak occurs
# convert peaks to time domain by diving by frequency sampled?
td_peaks = peaks / fs
plt.title("Raw ECG Signal")
plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.xlabel("# of samples")
plt.ylabel("ECG (mV)")
RRDistance=distancefinder(td_peaks)
newRRDistance = [element * 100 for element in RRDistance]

SDNN=np.std(newRRDistance)
NN50=NNCounter(td_peaks,0.5)
pNN50=(NN50/len(td_peaks))*100
RMSSD=rmsValue(newRRDistance,len(newRRDistance))
SDNN_Index=np.average(NNIndexer(newRRDistance))
print("pNN50 = " + str(pNN50)+ " %" )
print("RMSSD = " + str(RMSSD) + " ms")
print("Ln RMSSD = " + str(np.log(RMSSD)))
print("SDNN = " + str(SDNN) + " ms")
print("Ln SDNN = " + str(np.log(SDNN)))
#print("AvgRR is " + str(AvgRR) + " ms")
#print("StDev of RR Array is " + str(NNIndexer(RRDistance)))
print("SDNN Index = " + str(SDNN_Index * 100) + " ms")
#print("The array of RR differences is " + str(newRRDistance))

plt.figure()
plt.plot(td_peaks, x[peaks])
plt.title("RRI")
plt.xlabel("time (s)")
plt.ylabel("ECG (mV)")
plt.show()