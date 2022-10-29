from re import I
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
import scipy
ecg = electrocardiogram()
print(ecg)
def rmsValue(arr, n):
    square = 0
    mean = 0.0
    root = 0.0
    for i in range(0,n):
        square += (arr[i]**2)
    mean = (square / (float)(n))
    root = math.sqrt(mean)
    return root
def distancefinder(input):
    size=len(input)
    distanceArray = []
    for x in range(size-1):
        distanceArray.append(input[x+1]-input[x])
    return distanceArray
def NNCounter(input,thresh):
    counter=0
    for x in input:
        if x>thresh:
            counter += 1
    return counter
        
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



