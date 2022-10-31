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
print(ecg)
duration = 50      
fs = 360
time = np.arange(ecg.size) / fs
#plt.plot(time, ecg)
# plt.xlabel("time in s")
# plt.ylabel("ECG in mV")
# plt.xlim(0, 10)
# plt.ylim(-1, 3.0)

x = electrocardiogram() [60000:75000]
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
newRRDistance = [element * 1000 for element in RRDistance]

SDNN=np.std(newRRDistance)
NN50=NNCounter(td_peaks,0.5)
pNN50=(NN50/len(td_peaks))*100
RMSSD=rmsValue(newRRDistance,len(newRRDistance))
SDNN_Index=np.average(NNIndexer(newRRDistance))
print("n = " + str(NNCounter(td_peaks,0.5)) + " beats are included for analysis")
print("the mean difference per beat = " + str(np.mean(newRRDistance)) + " ms")
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


# X=FFT(np.reshape(x[peaks],12,6))
# n=np.arange(N)
# T=N/fs
# freq=n/T

# plt.figure()
# plt.subplot(121)
# plt.stem(freq, abs(X), 'b', \
#          markerfmt=" ", basefmt="-b")
# plt.xlabel('Freq (Hz)')
# plt.ylabel('FFT Amplitude |X(freq)|')

#plt.figure()
#x, y = generate_sin_wave(2, fs, duration)
#plt.plot(x, y)
#plt.figure()
#temp = np.linspace(0.0, 18000, x[peaks])
#temp = FillInTheGaps(x[peaks], RRDistance, fs)
#yf = fft(temp)
#xf = fftfreq(len(x) * df, (1/fs))
#plt.plot(xf[:18000], yf)

num_samples = 1000
y = resample(x[peaks], num_samples)
x = np.linspace(td_peaks[0], td_peaks[-1], num_samples)
plt.figure()
plt.plot(x,y)
plt.title("Resampled RRI")
plt.xlabel("time (s)")
plt.ylabel("ECG (mV)")
yf = fft(y)
xf = fftfreq(num_samples, 1/fs)
#xf = list(range(0,len(yf),1))
plt.figure()
plt.plot(xf,1/num_samples * np.abs(yf))
plt.title("RRI FFT")
plt.xlabel("Freq (Hz)")
plt.ylabel("PSD")

plt.show()