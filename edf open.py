
import numpy as np
import scipy 
import matplotlib.pyplot as plt
import mne 

file = "Sample_ECG.edf"
data = mne.io.read_raw_edf(file)
raw_data = data.get_data()

info = data.info
channels = data.ch_names
print(channels)
ECG_Data = mne.pick_channels(channels, [1])
print(ECG_Data)

time_secs = data.times
print(ECG_Data)

#plt.plot(time_secs,ECG_Data)
plt.show()