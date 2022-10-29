import math
import numpy as np


def rmsValue(arr, n):
    square = 0
    mean = 0.0
    root = 0.0
    for i in range(0,n):
        square += (arr[i]**2)
    mean = (square / (float)(n))
    root = math.sqrt(mean)
    return root
def distancefinder(input):
    size=len(input)
    distanceArray = []
    for x in range(size-1):
        distanceArray.append(input[x+1]-input[x])
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
def FillInTheGaps(input, RRDistance, fs):
    size = len(input)
    newArray = []
    for i in range(1, size-1):
        temp = np.linspace(input[i-1], input[i], round(RRDistance[i-1] * fs), endpoint=False)
        #newArray = np.concatenate(newArray, temp)
        newArray = newArray + list(temp)
    return newArray



    # differene in time between peaks is RRDistance
    # RRDistance[i-1] * fs = num samples