from re import I
from statistics import stdev
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
from functions import *
from main import RRDistance

class TimeDomainHRV:
    
    def __init__(self, input_data=None):
        self.ecg = electrocardiogram() [2000:100000]
        self.fs = 360
        self.time = np.arange(self.ecg.size) / self.fs
        self.peaks, _ = find_peaks(self.ecg, height = 0.2, threshold = None, distance = 100, 
            prominence=(0.7,None), width=None, wlen=None, rel_height=None, plateau_size=None)
        self.td_peaks = self.peaks / self.fs
        self.RRDistance = distancefinder(self.td_peaks)
        # convert to milliseconds
        self.RRDistance = [element * 100 for element in RRDistance]

        # if we dont have data by default, create sample data
        if input_data is not None:
            print("we load data here")
    
    def run(self):
        self.compute()
        self.print()
        self.graph()

    def compute(self):
        self.SDNN = np.std(self.RRDistance)
        self.NN50=NNCounter(self.td_peaks, 0.5)
        self.pNN50=(self.NN50/len(self.td_peaks))*100
        self.RMSSD=rmsValue(self.RRDistance,len(self.RRDistance))
        self.SDNN_Index=np.average(NNIndexer(self.RRDistance))

    def print(self):
        print("pNN50 = " + str(self.pNN50)+ " %" )
        print("RMSSD = " + str(self.RMSSD) + " ms")
        print("Ln RMSSD = " + str(np.log(self.RMSSD)))
        print("SDNN = " + str(self.SDNN) + " ms")
        print("Ln SDNN = " + str(np.log(self.SDNN)))
        print("SDNN Index = " + str(self.SDNN_Index * 100) + " ms")
        #print("AvgRR is " + str(AvgRR) + " ms")
        #print("StDev of RR Array is " + str(NNIndexer(RRDistance)))
        #print("The array of RR differences is " + str(newRRDistance))

    def graph(self):
        #graph 1
        plt.title("Raw ECG Signal")
        plt.plot(self.ecg)
        plt.plot(self.peaks, self.ecg[self.peaks], "x")
        plt.xlabel("# of samples")
        plt.ylabel("ECG (mV)")

        # graph 2
        plt.figure()
        plt.plot(self.td_peaks, self.ecg[self.peaks])
        plt.title("RRI")
        plt.xlabel("time (s)")
        plt.ylabel("ECG (mV)")
        plt.show()

        