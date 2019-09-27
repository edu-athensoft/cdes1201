places = []

try:
    with open(input('please enter file name, ex: filename.txt or filename.csv: '), 'r') as filehandle:
        for data in filehandle:
            currentPlace = data[:]
            currentPlace = currentPlace.strip()

            # add item to the list
            places.append(currentPlace)
    print('your data set is: ', places)
    num = list(map(float, places))  # conv to int
    num.sort()  # min to max
    if len(num) % 2 == 1:
        mid = (len(num) - 1) / 2
        print('median is: ', num[mid])
    else:
        mid = int(len(num) / 2)
        median = (num[mid] + num[mid - 1]) / 2
        print('median is: ', median)
except:
    print('please try again')
