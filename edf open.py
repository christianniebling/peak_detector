
import numpy as np
import scipy 
import matplotlib.pyplot as plt
#import mne 
import bioread


ECG_source = "Sample_ECG.acq"
file = bioread.read_file(ECG_source)
Channel_List=file.channels
ECG_Data = file.channels[1].raw_data
Time = file.channels[1].time_index

plt.plot(Time,ECG_Data)
plt.xlabel("time (s)")
plt.ylabel("ECG (mV)")
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