
import numpy as np
import scipy 
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks, resample
from scipy.fft import fft, fftfreq, rfft
from functions import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches 
import matplotlib.axes
import matplotlib.lines as lines
from matplotlib.patches import Ellipse
from math import pi
# import cv2 as cv 
import bioread

#make an ellipse
# cv.ellipse(center location (x,y), axes length (x AND Y), start angle, end angle)
# cv.ellipse((0,0),(256,3), (3,270), 0, 360)

#Open ACQ File
ECG_source = "Sample_ECG.acq"
file = bioread.read_file(ECG_source)
Channel_List=file.channels


#Pull BP Data and Peaks
BP_Data = file.channels[0].raw_data
BP_Time = file.channels[0].time_index
BP_fs = len(BP_Data/max(BP_Time))
BP = BP_Data
BP_peaks, _ = find_peaks(BP, height = 60, threshold = None, distance = 100, prominence=(40,None), width=None, wlen=None, rel_height=None, plateau_size=None)
td_BP_peaks = (BP_peaks/BP_fs)

#Pull ECG Data and Peaks and all Variables
ECG_Data = file.channels[1].raw_data
Time = file.channels[1].time_index
ECG_fs = len(ECG_Data)/max(Time)
x = ECG_Data
peaks, _ = find_peaks(x, height = 1.0, threshold = None, distance = 100, prominence=(0.7,None), width=None, wlen=None, rel_height=None, plateau_size=None)
td_peaks = (peaks / ECG_fs)
td_peaks_adjusted = np.delete(td_peaks,-1)
RRDistance=distancefinder(td_peaks)
newRRDistance = [element * 1000 for element in RRDistance]
Successive_time_diff=SuccessiveDiff(newRRDistance)
AvgDiff=np.average(Successive_time_diff)
SDNN=np.std(newRRDistance)
SDSD=np.std(Successive_time_diff)
NN50=NNCounter(Successive_time_diff, 50)
pNN50=(NN50/len(td_peaks))*100
RMSSD = np.sqrt(np.average(rms(Successive_time_diff)))
SD1 = np.sqrt(0.5*math.pow(SDSD,2))
SD2 = np.sqrt((2*math.pow(SDNN,2) - (0.5*math.pow(SDSD,2))))
S = math.pi * SD1 * SD2
Sampling_Time = max(td_peaks)
Num_Beats = len(newRRDistance)
HR = np.round(Num_Beats/(Sampling_Time/60),2)
NewRRDistancePPlot = np.delete(newRRDistance,-1)
RRIplusOne = Poincare(newRRDistance)

#Print out all pertinent ECG Information
print("n = " + str(Num_Beats) + " beats are included for analysis")
print(len(BP_peaks))
print(x[BP_peaks])
print("The total sampling time is " + str(Sampling_Time) + " seconds")
print("The average heart rate during the sampling time is = " + str(HR) + " BPM")
print("the mean difference between successive R-R intervals is = " + str(np.round(AvgDiff,3)) + " ms")
print("The mean R-R Interval duration is  " + str(np.round(np.average(newRRDistance),3)) + " ms")
print("pNN50 = " + str(np.round(pNN50,3)) + " %" )
print("RMSSD = " + str(np.round(RMSSD,3)) + " ms")
print("SDNN = " + str(np.round(SDNN,3)) + " ms")
print("SDSD = " + str(np.round(SDSD,3)) + " ms")
# print("Ln RMSSD = " + str(np.log((RMSSD))))
# print("Ln SDNN = " + str(np.log(SDNN)))
print("SD1 = " + str(np.round(SD1,3)) + " ms")
print("SD2 = " + str(np.round(SD2,3)) + " ms")
print("SD1/SD2 = " +str(np.round((SD1/SD2),3)))
print("The area of the ellipse fitted over the Poincaré Plot (S) is " + str(np.round(S,3)) + " ms^2")

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
plt.plot(td_peaks_adjusted, newRRDistance)
plt.title("RRI")
plt.xlabel("time (s)")
plt.ylabel("RRI (ms)")
plt.ylabel("ECG (mV)")

#Poincare Plot (RRI, RRI + 1)
EllipseCenterX = np.average(NewRRDistancePPlot)
EllipseCenterY = np.average(RRIplusOne)
Center_coords=EllipseCenterX,EllipseCenterY
fig = plt.figure()
ax=plt.axes()
z = np.polyfit(NewRRDistancePPlot, RRIplusOne, 1)
p = np.poly1d(z)
slope = z[0]
theta=np.degrees(np.arctan(slope))
plt.title("Poincaré Plot")
plt.scatter(NewRRDistancePPlot, RRIplusOne)
#create ellipse parameters, xy coordinates for center, width of ellipse, height of ellipse, angle of ellipse, colors of outline and inside
e=Ellipse((Center_coords),SD2*2,SD1*2,theta, edgecolor='black',facecolor='none')
matplotlib.axes.Axes.add_patch(ax,e)
plt.plot(NewRRDistancePPlot, p(NewRRDistancePPlot), color="red")
plt.ylabel("RRI + 1 (ms)")
plt.xlabel("RRI (ms)")

#Raw BP Data 
plt.figure()
plt.plot(BP_Time, BP_Data)
plt.xlabel("time (s)")
plt.ylabel("Finger Pressure (mmHg) ")

#Systolic Tagged
plt.figure()
plt.plot(BP)
plt.plot(BP_peaks, BP[BP_peaks], "x")



plt.show()

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
# plt.figure()
# u=EllipseCenterX     #x-position of the center
# v=EllipseCenterY   #y-position of the center
# a=SD2     #radius on the x-axis
# b=SD1    #radius on the y-axis
# angle=60

# t = np.linspace(0, 2*pi, 100)
# plt.plot( u+a*np.cos(t) , v+b*np.sin(t) )
