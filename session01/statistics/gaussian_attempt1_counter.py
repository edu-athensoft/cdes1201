from collections import Counter
import math
try:

    datastr = input('please enter data set')
    datalist = datastr.split()
    dataint = list(map(float, datalist))
    low = int(input("please enter lower boundary"))
    high = int(input("please enter higher boundary"))
    bins = int(input("please enter number of intervals"))


    def histogram(iterable, low, high, bins):

        step = (high - low + 0.0) / bins
        dist = Counter((float(x) - low) // step for x in iterable)
        return [dist[b] for b in range(bins)]


    print(histogram(dataint, low, high, bins))
    i = 0
    datafre = []
    while i < len(dataint):
        #math.fsum(dataint[:])
        datafre.append(dataint[i] / math.fsum(dataint[:]))
        i += 1
    print(datafre)

except:
    print("please try again")
