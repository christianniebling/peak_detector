import math
import numpy as np

#def generate_sin_wave(freq, fs, duration):
 #   x=np.linspace(0, duration, fs * duration, endpoint=False)
  #  frequencies = x * freq
   # y = np.sin((2* np.pi) * frequencies)
    #return x, y
def FFT(x):
    N=len(x)
    if N==1:
        return x
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = \
          np.exp(-2j*np.pi*np.arange(N)/ N)

        X = np.concatenate(\
            [X_even+factor[:int(N/2)]*X_odd,
             X_even+factor[int(N/2):]*X_odd])
        return X
def rms(input):
     SquareArray = []
     for x in input:
             SquareArray.append(np.square(x))
     return SquareArray       
def distancefinder(input):
    size=len(input)
    distanceArray = []
    for x in range(size-1):
            distanceArray.append(abs(input[x]-input[x+1]))
    return distanceArray
def NNCounter(input,thresh):
    counter=0
    for x in input:
        if x>thresh:
            counter += 1
    return counter
def NNIndexer(input):
    Size1=len(input)
    Mean=np.mean(input)
    StDevArray=[]
    for x in input:
        StDevArray.append(np.sqrt(np.sum(np.absolute(x-np.mean(input)))**2)/Size1)  
    return StDevArray
def SuccessiveDiff(input):
    size=len(input)
    SDArray=[]
    for x in range(size-1):
            SDArray.append(abs(input[x]-input[x+1]))
    return SDArray
def RemoveOutliers(x, y, threshold):
    new_x = []
    new_y = []
    size = len(y)
    for i in range(size):
        if y[i] < threshold:
            new_x.append(x[i])
            new_y.append(y[i])
    return new_x, new_y
def Poincare(input):
    size=len(input)
    newArray=[]
    for x in range(size-1):
        newArray.append(input[x+1])
    return newArray
def TimeTrimmer(input,thresh):
    timeArray=[]
    for x in input:
        if x >= thresh:
            timeArray.append(x)
    return timeArray
def SignalTrimmer(input, fs, thresh):
    trimmedArray=[]
    counter=0
    for x in input:
        counter += 1
        timex=counter/fs
        if timex >=thresh:
            trimmedArray.append(x)
    return trimmedArray


def FindTimeIndex(time_list, time):
    for i in range(0, len(time_list)):
        if time_list[i] >= time:
            # As soon as we find the first occurance where time[i] is >= the time we want,
            # we can exit the function and return the index
            return i
    
    # If we never found the index, return 0
    print("[CutTime]: Could not find index!")
    return 0
def UpRampCount(input,BPthresh):
    count=0
    size=len(input)
    for x in range(size-2):
        if (input[x]+BPthresh) >= input[x+1] >= (input[x+2]+BPthresh):
            count += 1
    return count
    
def UpCount(input1,input2,RRthresh,BPthresh):
     count = 0
     size1 = len(input1)
     size2 = len(input2) 
     for x in range(size1-2):
            if (input1[x]-RRthresh) >= input1[x+1] >= (input1[x+2]+RRthresh):
                for x in range (size2-2):
                    if (input2[x]+BPthresh) <= input2[x+1] <= (input2[x+2]-BPthresh):
                        count += 1
                return count 

def DownCount(input1,input2,RRthresh, BPthresh):
     count = 0
     size1 = len(input1)
     size2 = len(input2) 
     for x in range(size1-2):
            if (input1[x]+RRthresh) <= input1[x+1] <= (input1[x+2]-RRthresh):
                for x in range (size2-2):
                    if (input2[x]-BPthresh) >= (input2[x+1]) >= (input2[x+2]+BPthresh):
                        count += 1
                return count 





        



# def FillInTheGaps(input, RRDistance, fs):
#    size = len(input)
#    newArray = []
#    for i in range(1, size-1):
#        temp = np.linspace(input[i-1], input[i], round(RRDistance[i-1] * fs), endpoint=False)
#        #newArray = np.concatenate(newArray, temp)
#        newArray = newArray + list(temp)
#        return newArray



    # differene in time between peaks is RRDistance
    # RRDistance[i-1] * fs = num samples
 