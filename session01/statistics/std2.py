places = []
import math

try:
    with open(input('please enter file name, ex: filename.txt or filename.csv: '), 'r') as filehandle:
        for data in filehandle:
            currentPlace = data[:]
            currentPlace = currentPlace.strip()

            # add item to the list
            places.append(currentPlace)
    print('your data set is: ', places)
    numint = list(map(float, places))  # conv to int
    mean = math.fsum(numint[:]) / len(places)
    diff = []
    i = 0
    while i < len(places):
        square = (mean - float(places[i])) ** 2
        i += 1
        diff.append(square)
        var = math.fsum(diff[:])
    std = var ** (1 / 2)

    print('standard deviation is: ', std)
except:
    print('please try again')
