import matplotlib.pyplot as plt
import mne

data = mne.io.read_raw_edf('test.edf')
raw_data = data.get_data()
y = raw_data[1] [0:1000]
print('yes')
x = list(range(len(y)))
plt.plot(x,y)
plt.savefig('show_ecg.png')