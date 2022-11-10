
import numpy as np
import scipy 
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks, resample
from scipy.fft import fft, fftfreq, rfft
from functions import *
import matplotlib.pyplot as plt
import bioread



ECG_source = "Sample_ECG.acq"
file = bioread.read_file(ECG_source)
Channel_List=file.channels
ECG_Data = file.channels[1].raw_data
Time = file.channels[1].time_index
ECG_fs = len(ECG_Data)/max(Time)
BP_Data = file.channels[0].raw_data
BP_Time = file.channels[0].time_index
x = ECG_Data
peaks, _ = find_peaks(x, height = 1.0, threshold = None, distance = 100, prominence=(0.7,None), width=None, wlen=None, rel_height=None, plateau_size=None)
td_peaks = (peaks / ECG_fs)
RRDistance=distancefinder(td_peaks)
newRRDistance = [element * 1000 for element in RRDistance]
Successive_time_diff=SuccessiveDiff(newRRDistance)
AvgDiff=np.average(Successive_time_diff)
SDNN=np.std(newRRDistance)
NN50=NNCounter(Successive_time_diff, 50)
pNN50=(NN50/len(td_peaks))*100
RMSSD = np.sqrt(np.average(rms(Successive_time_diff)))

print("n = " + str(len(newRRDistance)) + " beats are included for analysis")
print("The total sampling time is " + str(max(td_peaks)) + " seconds")
print("the mean difference between R-R intervals is = " + str(AvgDiff) + " ms")
print("The mean R-R Interval is  " + str(np.average(newRRDistance)) + " ms")
print("pNN50 = " + str(pNN50)+ " %" )
print("RMSSD = " + str(RMSSD) + " ms")
print("Ln RMSSD = " + str(np.log(RMSSD)))
print("SDNN = " + str(SDNN) + " ms")
print("Ln SDNN = " + str(np.log(SDNN)))
plt.figure()
plt.plot(Time,ECG_Data)
plt.xlabel("time (s)")
plt.ylabel("ECG (mV)")

plt.figure()
plt.plot(BP_Time, BP_Data)
plt.xlabel("time (s)")
plt.ylabel("Finger Pressure (mmHg) ")

plt.figure()
plt.title("Raw ECG Signal with R-R Detected")
plt.plot(x)
plt.plot(peaks, x[peaks], "x")

plt.ylabel("ECG (mV)")
# plt.show()


# data = mne.io.read_raw_edf(file)
# raw_data = data.get_data()

# info = data.info
# channels = data.ch_names
# ECG_Data = raw_data[1]
# print(ECG_Data)
# time_secs = data.times


# #plt.plot(time_secs,ECG_Data)
# plt.plot(time_secs, ECG_Data)
# plt.show()