
import numpy as np
import scipy 
# import pandas as pd
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks, resample, ZoomFFT
from scipy.fft import fft, fftfreq, rfft
from functions import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches 
import matplotlib.axes
import matplotlib.lines as lines
import pywt
from matplotlib.patches import Ellipse
from math import pi
import bioread
# import EntropyHub



#Open ACQ File
ECG_source = "data/REST.acq"
file = bioread.read_file(ECG_source)
Channel_List=file.channels



#Pull BP Data 
BP_Data = file.channels[0].raw_data
BP_Time = file.channels[0].time_index
BP_fs = len(BP_Data)/max(BP_Time)
BP = BP_Data
BP_peaks, _ = find_peaks(BP, height = 50, threshold = None, distance = 100, prominence=(40,None), width=None, wlen=None, rel_height=None, plateau_size=None)
td_BP_peaks = (BP_peaks/BP_fs)

#Pull ECG Data  and all Variables
ECG_Data = file.channels[1].raw_data
Time = file.channels[1].time_index
ECG_fs = len(ECG_Data)/max(Time)
x = ECG_Data

#Trim signals to any time we want (cutting the first x seconds)
# TrimmedECG = SignalTrimmer(ECG_Data, ECG_fs, 60)
# TrimmedBP = SignalTrimmer (BP_Data, BP_fs, 60)
# TrimmedECG_time = TimeTrimmer(Time, 60)
# TrimmedBP_time = TimeTrimmer(BP_Time, 60)

#Tag R Intervals and create Array of RR Interval Distances
peaks, _ = find_peaks(x, height = 0.9, threshold = None, distance = 100, prominence=(0.7,None), width=None, wlen=None, rel_height=None, plateau_size=None)
td_peaks = (peaks / ECG_fs)
RRDistance = distancefinder(td_peaks)
#convert to ms
RRDistance_ms = [element * 1000 for element in RRDistance]

#Tag Systolic BP Peaks Untrimmed and trimmed
BP_peaks, _ = find_peaks(BP, height = 50, threshold = None, distance = 100, prominence=(40,None), width=None, wlen=None, rel_height=None, plateau_size=None)
td_BP_peaks = (BP_peaks/BP_fs)
# Trimmed_BP_peaks, _ = find_peaks(TrimmedBP, height = 50, threshold = None, distance = 100, prominence=(40,None), width=None, wlen=None, rel_height=None, plateau_size=None)
# Trimmed_td_BP_peaks = (Trimmed_BP_peaks/BP_fs)
# Trimmed_Systolic_Array = TrimmedBP[Trimmed_BP_peaks]
#Obtain pulse interval (time difference between BP peaks)
PulseIntervalDistance = distancefinder(td_BP_peaks)
#Convert to ms
PI_ms = [element * 1000 for element in PulseIntervalDistance]

#Time domain HRV Variables
Successive_time_diff=SuccessiveDiff(RRDistance_ms)
AvgDiff=np.average(Successive_time_diff)
SDNN=np.std(RRDistance_ms)
SDSD=np.std(Successive_time_diff)
NN50=NNCounter(Successive_time_diff, 50)
pNN50=(NN50/len(td_peaks))*100
RMSSD = np.sqrt(np.average(rms(Successive_time_diff)))
SD1 = np.sqrt(0.5*math.pow(SDSD,2))
SD2 = np.sqrt((2*math.pow(SDNN,2) - (0.5*math.pow(SDSD,2))))
S = math.pi * SD1 * SD2
Sampling_Time = max(td_peaks)
Num_Beats = len(RRDistance_ms)
HR = np.round(Num_Beats/(Sampling_Time/60),2)

#Create axes for Poincare Plot
RRIplusOne = Poincare(RRDistance_ms)




#Print Time Domain HRV Variables
print("n = " + str(Num_Beats) + " beats are included for analysis")
print("The total sampling time is " + str(Sampling_Time) + " seconds")
print("The average heart rate during the sampling time is = " + str(HR) + " BPM")
print("the mean difference between successive R-R intervals is = " + str(np.round(AvgDiff,3)) + " ms")
print("The mean R-R Interval duration is  " + str(np.round(np.average(RRDistance_ms),3)) + " ms")
print("pNN50 = " + str(np.round(pNN50,3)) + " %" )
print("RMSSD = " + str(np.round(RMSSD,3)) + " ms")
print("SDNN = " + str(np.round(SDNN,3)) + " ms")
print("SDSD = " + str(np.round(SDSD,3)) + " ms")
#Leave log transformations in in case we want them
# print("Ln RMSSD = " + str(np.log((RMSSD))))
# print("Ln SDNN = " + str(np.log(SDNN)))
print("SD1 = " + str(np.round(SD1,3)) + " ms")
print("SD2 = " + str(np.round(SD2,3)) + " ms")
print("SD1/SD2 = " + str(np.round((SD1/SD2),3)))
print("The area of the ellipse fitted over the Poincaré Plot (S) is " + str(np.round(S,3)) + " ms^2")

#Blood Pressure Information
Systolic_Array = BP[BP_peaks]
Avg_BP = np.round((np.average(Systolic_Array)),3)
SD_BP = np.round((np.std(Systolic_Array)),3)

#Print Blood Pressure Information
print("The average systolic blood pressure during the sampling time is " + str(Avg_BP) + " + - " + str(SD_BP) + " mmHg")
print(str(len(Systolic_Array)) + " pressure waves are included in the analysis")

#Start of All ECG Plots 
#Raw ECG
plt.figure()
plt.plot(Time,ECG_Data)
plt.xlabel("time (s)")
plt.ylabel("ECG (mV)")

#ECG with R intervals tagged
plt.figure()
plt.title("Raw ECG Signal with R-R Detected")
plt.plot(x)
plt.plot(peaks, x[peaks], "x")

#RRI / Tachogram
plt.figure()
#Need to remove last element of td_peaks in order for two arrays that we are plotting to match in size 
plt.plot(np.delete(td_peaks,-1), RRDistance_ms)
plt.title("RRI")
plt.xlabel("time (s)")
plt.ylabel("RRI (ms)")
plt.ylim(400,1100)
plt.text(0, 600, 'n = ' + str (len(RRDistance_ms)), fontsize=10)
plt.text(0, 500, 'Mean = ' + str (np.round(np.average(RRDistance_ms),1)) + ' ms', fontsize=10)
plt.text(200, 500, 'σ2 = ' + str (np.round(np.var(RRDistance_ms),1)) + 'ms\u00b2', fontsize=10)  
# plt.show()

#Poincare Plot (RRI, RRI + 1)
EllipseCenterX = np.average(np.delete(RRDistance_ms,-1))
EllipseCenterY = np.average(RRIplusOne)
Center_coords=EllipseCenterX,EllipseCenterY
fig = plt.figure()
ax=plt.axes()
#need to remove last element of array of RR Distances to make arrays we are plotting match
z = np.polyfit(np.delete(RRDistance_ms,-1), RRIplusOne, 1)
p = np.poly1d(z)
slope = z[0]
theta=np.degrees(np.arctan(slope))
plt.title("Poincaré Plot")
plt.scatter(np.delete(RRDistance_ms,-1), RRIplusOne)
#create ellipse parameters, xy coordinates for center, width of ellipse, height of ellipse, angle of ellipse, colors of outline and inside
e=Ellipse((Center_coords),SD2*2,SD1*2,theta, edgecolor='black',facecolor='none')
matplotlib.axes.Axes.add_patch(ax,e)
plt.plot(np.delete(RRDistance_ms,-1), p(np.delete(RRDistance_ms,-1)), color="red")
plt.ylabel("RRI + 1 (ms)")
plt.xlabel("RRI (ms)")
plt.text(950, 750, 'SD1 = ' + str(np.round((SD1),1)) + " ms", fontsize=10)
plt.text(950, 700, 'SD2 = ' + str(np.round((SD2),1)) + "ms", fontsize=10)

#Start of BP Plots 
# #Raw BP Data 
plt.figure()
plt.plot(BP_Time, BP_Data)
plt.xlabel("time (s)")
plt.ylabel("Finger Pressure (mmHg) ")

# #Systolic Tagged
plt.figure()
plt.plot(BP)
plt.plot(BP_peaks, BP[BP_peaks], "x")
plt.ylabel("Blood Pressure (mmHg)")
plt.title("Raw BP with Systolic Detected")

#Any type of preprocessing for FFT: Resampling, windowing, filtering, etc.

#Tachogram Resampling
sampling_rate = 250
resampled_tachogram, resampled_sampling_rate = resample_tachogram(RRDistance_ms, ECG_fs, 250)
original_time = np.arange(0, len(RRDistance_ms)/ECG_fs, 1/ECG_fs)
resampled_time = np.arange(0, len(resampled_tachogram)/resampled_sampling_rate, 1/resampled_sampling_rate)

#Windowing
window = np.hanning(len(RRDistance_ms))
windowed_RRI = RRDistance_ms * window 

#Plot original + Windowed RRI 
plt.figure(figsize=(10, 6))
plt.plot(RRDistance_ms, label='Original Signal')
plt.plot(windowed_RRI, label='Windowed Signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.title('ECG Signal with Hann Windowing')
plt.legend()
# plt.show()

#Low Pass Filtering (eliminate noise from high frequency bands)
cutoff_freq = 0.5
filter_order = 4 
nyquist_freq = 0.5 * len(windowed_RRI)
cutoff = cutoff_freq/nyquist_freq
#Apply filter
b, a = signal.butter(filter_order, cutoff, btype = 'low')
filtered_windowed_RRI = signal.lfilter(b,a, windowed_RRI)

#Plot original + filtered RRI 
plt.figure(figsize=(10, 6))
plt.plot(windowed_RRI, label='Original Signal')
plt.plot(filtered_windowed_RRI, label='Filtered Signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.title('ECG Signal with Low-Pass Filtering')
plt.legend()



#FFT 
fft_result = np.fft.fft(windowed_RRI)
frequencies = np.fft.fftfreq(len(windowed_RRI))

#Calculate Power Spectral Density
psd = np.abs(fft_result)**2

#Plot FFT Result
plt.figure()
plt.plot(frequencies[:len(filtered_windowed_RRI)//2], np.abs(fft_result[:len(filtered_windowed_RRI)//2]))
plt.title('FFT Result')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')


#Plot FFT with PSD Instead of Magnitude
plt.figure()
plt.plot(frequencies[:len(filtered_windowed_RRI)//2], psd[:len(filtered_windowed_RRI)//2])
plt.title('Power Spectral Density (PSD)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('PSD')

#Try Discrete Wavelet Transform Instead
wavelet = 'db4'
level = 5
coeffs = pywt.wavedec(filtered_windowed_RRI, wavelet, level = level)

#Plot DWT 
plt.figure()
for i in range (level + 1): 
    plt.subplot(level+1, 1, i+1)
    plt.plot(coeffs[i])
    plt.title(f'DWT Coefficients - Level {i}')
    plt.xlabel('Index')
    plt.ylabel('Coefficient')
# plt.show()

#plot resampled tachogram
plt.figure()
plt.plot(original_time, RRDistance_ms, label='Original Tachogram')
plt.plot(resampled_time, resampled_tachogram, label='Resampled Tachogram')
plt.xlabel('Time (s)')
plt.ylabel('RR Interval')
plt.title('Resampled Tachogram')
plt.legend()
# plt.show()
# #plot trimmed ECG and BP
# plt.figure()
# plt.plot(TrimmedECG_time, TrimmedECG)
# plt.xlabel("time (s)")
# plt.ylabel("ECG (mV)")

# plt.figure()
# plt.plot(TrimmedBP_time,TrimmedBP)
# plt.xlabel("time (s)")
# plt.ylabel("Finger Pressure (mmHg) ")

#Count BP Ramps
BpUpRamps,BpDownRamps = bpCount(Systolic_Array,1)
TotalRamps = BpUpRamps + BpDownRamps
print(str(BpUpRamps) + " SBP Up Ramps were observed during the Recording Period")
print(str(BpDownRamps) + " SBP Down Ramps were observed during the Recording Period")
print(str(TotalRamps) + " Total SBP Ramps were observed during the Recording Period")

#Count PI + BP Ramps
UpEvents, DownEvents = count(PI_ms, np.delete(Systolic_Array,-1), 4, 1)
# print(UpEvents) #+ " PI/SBP up-up events were observed during the Recording Period"
# print(DownEvents) #+ " PI/SBP down-down events were observed during the Recording Period"

#Entropy 
Shannon_Entropy = compute_shannon_entropy(RRDistance_ms)
#Approximate Entropy
print(ApEn(RRDistance_ms,2,0.2 * np.std(RRDistance_ms)))
print(SampEn(RRDistance_ms,2,0.2 * np.std(RRDistance_ms)))


# print(ApEn(sin_y, 2, np.std(sin_y) * 0.2))
# plt.show()