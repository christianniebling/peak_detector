import math

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