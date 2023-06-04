
import numpy as np
import scipy 
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks, resample, ZoomFFT
from scipy.fft import fft, fftfreq, rfft
from functions import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches 
import matplotlib.axes
import matplotlib.lines as lines
from matplotlib.patches import Ellipse
from math import pi
import bioread


#Open ACQ File
ECG_source = "data/TEST.acq"
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
peaks, _ = find_peaks(x, height = 0.8, threshold = None, distance = 100, prominence=(0.7,None), width=None, wlen=None, rel_height=None, plateau_size=None)
td_peaks = (peaks / ECG_fs)
RRDistance=distancefinder(td_peaks)
#convert to ms
RRDistance_ms = [element * 1000 for element in RRDistance]

#Tag Systolic BP Peaks Untrimmed and trimmed
BP_peaks, _ = find_peaks(BP, height = 50, threshold = None, distance = 100, prominence=(40,None), width=None, wlen=None, rel_height=None, plateau_size=None)
td_BP_peaks = (BP_peaks/BP_fs)
# Trimmed_BP_peaks, _ = find_peaks(TrimmedBP, height = 50, threshold = None, distance = 100, prominence=(40,None), width=None, wlen=None, rel_height=None, plateau_size=None)
# Trimmed_td_BP_peaks = (Trimmed_BP_peaks/BP_fs)
# Trimmed_Systolic_Array = TrimmedBP[Trimmed_BP_peaks]


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
print("SD1/SD2 = " +str(np.round((SD1/SD2),3)))
print("The area of the ellipse fitted over the Poincaré Plot (S) is " + str(np.round(S,3)) + " ms^2")

#Blood Pressure Information
Systolic_Array = BP[BP_peaks]
Avg_BP = np.round((np.average(Systolic_Array)),3)
SD_BP = np.round((np.std(Systolic_Array)),3)
Num_Waves = len(Systolic_Array)

#Print Blood Pressure Information
print("The average systolic blood pressure during the sampling time is " + str(Avg_BP) + " + - " + str(SD_BP) + " mmHg")
print(str(Num_Waves) + " pressure waves are included in the analysis")

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

#RRI 
plt.figure()
#Need to remove last element of td_peaks in order for two arrays that we are plotting to match in size 
plt.plot(np.delete(td_peaks,-1), RRDistance_ms)
plt.title("RRI")
plt.xlabel("time (s)")
plt.ylabel("RRI (ms)")
plt.ylabel("ECG (mV)")

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
e=Ellipse((Center_coords),SD2*2,SD1*2, angle=theta, edgecolor='black',facecolor='none')
matplotlib.axes.Axes.add_patch(ax,e)
plt.plot(np.delete(RRDistance_ms,-1), p(np.delete(RRDistance_ms,-1)), color="red")
plt.ylabel("RRI + 1 (ms)")
plt.xlabel("RRI (ms)")

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


# #plot trimmed ECG and BP
# plt.figure()
# plt.plot(TrimmedECG_time, TrimmedECG)
# plt.xlabel("time (s)")
# plt.ylabel("ECG (mV)")

# plt.figure()
# plt.plot(TrimmedBP_time,TrimmedBP)
# plt.xlabel("time (s)")
# plt.ylabel("Finger Pressure (mmHg) ")







# BpUpRamps,BpDownRamps = bpCount(Systolic_Array,1)
# TotalRamps = BpUpRamps + BpDownRamps
# print(str(BpUpRamps) + " SBP Up Ramps were observed during the Recording Period")
# print(str(BpDownRamps) + " SBP Down Ramps were observed during the Recording Period")
# print(str(TotalRamps) + " Total SBP Ramps were observed during the Recording Period")
# print(Trimmed_Systolic_Array)

# Frequency analysis
# f1, f2 = 0, 1
# # y = newRRDistance
# transform = ZoomFFT(len(y), [f1, f2], len(y), fs=fs)
# Y = transform(y)
# f = np.linspace(f1, f2, len(y))
# plt.figure()
# plt.plot(f, np.abs(Y))
# plt.savefig('show.png')

# TODO: try resampling newRRDistance and see if that improves FFT
# num_samples = 1000
# y = resample(y, num_samples)
# x = np.linspace(x[0], x[-1], num_samples)
# plt.figure()
# plt.plot(x,y)

# plt.show()
