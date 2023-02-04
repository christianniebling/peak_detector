import mne 
file = "Sample_ECG.edf"
data = mne.io.read_raw_edf(file)
raw_data = data.get_data()
# you can get the metadata included in the file and a list of all channels:
info = data.info
channels = data.ch_names
time_secs=data.times
print(time_secs)

print(info)