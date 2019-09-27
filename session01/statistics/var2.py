places = []
import math

with open(input('please enter txt file name'), 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:]
        currentPlace = currentPlace.strip()
        # print(currentPlace.strip())

        # add item to the list
        places.append(currentPlace)
print(places)
numint = list(map(float, places))  # conv to int
mean = math.fsum(numint[:]) / len(places)
diff = []
i = 0
while i < len(places):
    square = (mean - float(places[i])) ** 2
    i += 1
    diff.append(square)
    var = math.fsum(diff[:])
print(var)
