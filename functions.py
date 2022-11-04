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
def RemoveOutliers(input, threshold):
    NewArray=[]
    size=len(input)
    for x in range(size):
        if input[x] < threshold:
            NewArray.append(input[x])
    return NewArray
        



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
 