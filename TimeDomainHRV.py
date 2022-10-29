from re import I
from statistics import stdev
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
import scipy
from functions import *

class TimeDomainHRV:
    
    def __init__(input_data=None):
        self.fs 
        self.time

        # if we dont have data by default, create sample data
        if input_data is None:
            self.fs = 360
            self.ecg = 


        