places = []

try:
    with open(input('please enter file name, ex: filename.txt or filename.csv: '), 'r') as filehandle:
        for data in filehandle:
            currentPlace = data[:]
            currentPlace = currentPlace.strip()

            # add item to the list
            places.append(currentPlace)
    print('your data set is: ', places)
    numint = list(map(float, places))  # conv to int
    print('min value is: ', min(numint))
except:
    print('please try again')
