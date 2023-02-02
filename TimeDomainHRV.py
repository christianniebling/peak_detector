from statistics import stdev
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
from functions import *
import bioread

class TimeDomainHRV():
    
    def __init__(self, input_data=None):

        self.init_data("data/TEST.acq") # TODO: move to const var location 

        # if we dont have data by default, create sample data
        if input_data is not None:
            print("we load data here")
    
    def run(self):
        self.compute()
        self.print()
        self.graph()

    def init_data(self, data_source):
        _file = bioread.read_file(data_source)
        channel_list = _file.channels

        # Get BP data
        self.BP_data = _file.channels[0].raw_data
        BP_time = _file.channels[0].time_index
        self.BP_fs = len(self.BP_data)/max(BP_time)
        self.BP_peaks, _ = find_peaks(self.BP_data, height = 50, threshold = None, distance = 100, prominence=(40,None), width=None, wlen=None, rel_height=None, plateau_size=None)
        td_BP_peaks = (self.BP_peaks/self.BP_fs)

        # Get ECG data
        self.ECG_data = _file.channels[1].raw_data
        self.time = _file.channels[1].time_index
        self.ECG_fs = len(self.ECG_data)/max(self.time)

        self.peaks, _ = find_peaks(self.ECG_data, height = 0.8, threshold = None, distance = 100, prominence=(0.7,None), width=None, wlen=None, rel_height=None, plateau_size=None)
        self.td_peaks = (self.peaks / self.ECG_fs)
        self.td_peaks_adjusted = np.delete(self.td_peaks,-1)
        self.RRDistance=distancefinder(self.td_peaks)
        #convert to ms. TODO: rename to RRDistance_ms
        self.newRRDistance = [element * 1000 for element in self.RRDistance]

        self.BP_peaks, _ = find_peaks(self.BP_data, height = 50, threshold = None, distance = 100, prominence=(40,None), width=None, wlen=None, rel_height=None, plateau_size=None)
        td_BP_peaks = (self.BP_peaks/self.BP_fs)

    def compute(self):
        self.compute_time_domain_HRV_vars()
        self.compute_blood_pressure_info()

    def print(self):
        print(self.print_s())

    def print_s(self) -> str:
        s = ''
        s += "n = " + str(self.num_beats) + " beats are included for analysis\n"
        s += "The total sampling time is " + str(self.sampling_time) + " seconds\n"
        s += "The average heart rate during the sampling time is = " + str(self.HR) + " BPM\n"
        s += "the mean difference between successive R-R intervals is = " + str(np.round(np.average(self.sd), 3)) + " ms\n"
        s += "The mean R-R Interval duration is  " + str(np.round(np.average(self.newRRDistance),3)) + " ms\n"
        s += "pNN50 = " + str(np.round(self.pNN50, 3)) + " %\n" 
        s += "RMSSD = " + str(np.round(self.RMSSD, 3)) + " ms\n"
        s += "SDNN = " + str(np.round(self.SDNN, 3)) + " ms\n"
        s += "SDSD = " + str(np.round(self.SDSD, 3)) + " ms\n"
        s += "SD1 = " + str(np.round(self.SD1, 3)) + " ms\n"
        s += "SD2 = " + str(np.round(self.SD2, 3)) + " ms\n"
        s += "SD1/SD2 = " +str(np.round((self.SD1 / self.SD2), 3)) + "\n"
        s += "The area of the ellipse fitted over the Poincaré Plot (S) is " + str(np.round(self.S,3)) + " ms^2\n"
        return s

    def graph(self):
        #graph 1: raw ECG
        plt.title("Raw ECG Signal")
        plt.plot(self.time, self.ECG_data)
        plt.xlabel("time (s)")
        plt.ylabel("ECG (mV)")

        # graph 2: ECG with R intervals tagged
        plt.figure()
        plt.title("Raw ECG Signal with R-R Detected")
        plt.plot(self.ECG_data)
        plt.plot(self.peaks, self.ECG_data[self.peaks], "x")
        plt.xlabel("time (s)")
        plt.ylabel("ECG (mV)")

        plt.show()

    def compute_time_domain_HRV_vars(self):
        self.SDNN = np.std(self.newRRDistance)
        self.sd = SuccessiveDiff(self.newRRDistance)
        self.SDSD = np.std(self.sd)
        self.NN50 = NNCounter(self.sd, 50)
        self.pNN50 = (self.NN50 / len(self.td_peaks)) * 100
        self.RMSSD = np.sqrt(np.average(rms(self.sd)))
        self.SD1 = np.sqrt(0.5 * math.pow(self.SDSD, 2))
        self.SD2 = np.sqrt(2 * math.pow(self.SDNN, 2) - (0.5 * math.pow(self.SDSD, 2)))
        self.S = math.pi * self.SD1 * self.SD2
        self.sampling_time = max(self.td_peaks)
        self.num_beats = len(self.newRRDistance)
        self.HR = np.round(self.num_beats / (self.sampling_time / 60), 2)

        # Create axes for Poincare Plot
        PPlot = np.delete(self.newRRDistance, -1)
        RRI_plus_one = Poincare(self.newRRDistance)

    def compute_blood_pressure_info(self):
        systolic_array = self.BP_data[self.BP_peaks]
        avg_BP = np.round(np.average(systolic_array), 3)
        sd_bp = np.round(np.std(systolic_array), 3)
        num_waves = len(systolic_array)

