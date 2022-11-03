from re import I
from statistics import stdev
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks, resample
from scipy.fft import fft, fftfreq, rfft
import scipy
from functions import *
ecg = electrocardiogram()
#print(ecg)
fs = 360
time = np.arange(ecg.size) / fs
# plt.plot(time, ecg)
# plt.xlabel("time in s")
# plt.ylabel("ECG in mV")


x = electrocardiogram() [2000:100000]
time = np.arange(x.size) / fs
peaks, _ = find_peaks(x, height = 0.1, threshold = None, distance = 100, prominence=(0.7,None), width=None, wlen=None, rel_height=None, plateau_size=None)
# peaks = time in x where peak occurs
# convert peaks to time domain by diving by frequency sampled?
td_peaks = (peaks / fs)
td_peaks_adjusted=np.delete(td_peaks,-1)

plt.figure()
plt.title("Raw ECG Signal with R-R Detected")
plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.xlabel("# of samples")
plt.ylabel("ECG (mV)")
#get difference between RR intervals
RRDistance=distancefinder(td_peaks)

#convert to ms
newRRDistance = [element * 1000 for element in RRDistance]
Successive_time_diff=SuccessiveDiff(newRRDistance)
AvgDiff=np.average(Successive_time_diff)
SDNN=np.std(newRRDistance)
NN50=NNCounter(Successive_time_diff, 50)
pNN50=(NN50/len(td_peaks))*100
RMSSD = np.sqrt(np.average(rms(Successive_time_diff)))
SDNN_Index=np.average(NNIndexer(newRRDistance))
#Smoothed_RRI=RemoveOutliers(newRRDistance)
print("n = " + str(len(newRRDistance)) + " beats are included for analysis")
print("The total sampling time is " + str(max(td_peaks)) + " seconds")
print("the mean difference between R-R intervals is = " + str(AvgDiff) + " ms")
print("The mean R-R Interval is  " + str(np.average(newRRDistance)) + " ms")
print("pNN50 = " + str(pNN50)+ " %" )
print("RMSSD = " + str(RMSSD) + " ms")
print("Ln RMSSD = " + str(np.log(RMSSD)))
print("SDNN = " + str(SDNN) + " ms")
print("Ln SDNN = " + str(np.log(SDNN)))
#print("StDev of RR Array is " + str(NNIndexer(RRDistance)))
print("SDNN Index = " + str(SDNN_Index * 100) + " ms")



# plt.figure()
# plt.plot(td_peaks, x[peaks])
# plt.title("RRI")
# plt.xlabel("time (s)")
# plt.ylabel("ECG (mV)")

plt.figure()
plt.plot(td_peaks_adjusted, newRRDistance)
plt.title("RRI")
plt.xlabel("time (s)")
plt.ylabel("RRI (ms)")

# #extract the signal for the y axis of the FFT 
# y=x[peaks]

#extract the correct x axis in the frequency domain
# N=fs*duration
# x = np.linspace(0, N*time, N)
# plt.figure()
# plt.plot(x, y)
# plt.grid()

# # # Take the fourier
# # yf = fft(y)
# # xf = fftfreq(N, T)

# # # Plot in the frequency domain
# # plt.figure()
# # plt.plot(xf, 1/N * np.abs(yf))
# # plt.grid()

# num_samples = 1000
# y = resample(x[peaks], num_samples)
# x = np.linspace(td_peaks[0], td_peaks[-1], num_samples)
# plt.figure()
# plt.plot(x,y)
# plt.title("Resampled RRI")
# plt.xlabel("time (s)")
# plt.ylabel("ECG (mV)")
# yf = fft(y)
# xf = fftfreq(num_samples, 1/fs)
# #xf = list(range(0,len(yf),1))
# plt.figure()
# plt.plot(xf,1/num_samples * np.abs(yf))
# plt.title("RRI FFT")
# plt.xlabel("Freq (Hz)")
# plt.ylabel("PSD")

plt.show()
