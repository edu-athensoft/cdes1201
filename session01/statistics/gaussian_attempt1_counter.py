from collections import Counter
import math

try:

    datastr = input('please enter data set')
    datalist = datastr.split()
    dataint = list(map(float, datalist))
    low = float(input("please enter lower boundary"))
    high = float(input("please enter higher boundary"))
    if high < max(dataint):
        print('higher boundary is lower than maximum, please try again')
        quit()
    bins = int(input("please enter number of intervals"))


    def histogram(iterable, low, high, bins):

        step = (high - low + 0.0) / bins  # length of interval
        dist = Counter((float(x) - low) // step for x in iterable)  # return list for number of data in each interval
        print('dist=',dist,type(dist))
        # return [dist[b] for b in range(bins)]
        return [dist[b] / math.fsum(dist[s] for s in range(bins)) for b in range(bins)]


    print(histogram(dataint, low, high, bins))
# i = 0
# datafre = []

# while i < len(dataint):
# datafre.append(dataint[i] / math.fsum(dataint[:]))
# i += 1
# print(datafre)

except:
    print("please try again")
