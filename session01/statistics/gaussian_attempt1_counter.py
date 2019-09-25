from collections import Counter
try:

    datastr = input('please enter data set')
    datalist = datastr.split()
    dataint = list(map(int, datalist))
    low = int(input("please enter lower boundary"))
    high = int(input("please enter higher boundary"))
    bins = int(input("please enter number of intervals"))


    def histogram(iterable, low, high, bins):

        step = (high - low + 0.0) / bins
        dist = Counter((float(x) - low) // step for x in iterable)
        return [dist[b] for b in range(bins)]


    print(histogram(dataint, low, high, bins))
except:
    print("please try again")