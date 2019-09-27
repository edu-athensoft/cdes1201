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
    num = list(map(float,places))  # conv to int

    print('sum is: ', math.fsum(num[:]))
except:
    print('please try again')
