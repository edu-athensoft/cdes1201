numstr = input("to find variance and standard deviation, input a set of numbers separated by space: ")
try:
    numlist = numstr.split( )
    numint = map(int, numlist)
    numint = list(map(int, numlist))#conv to int
    import math
    mean = math.fsum(numint[:]) / len(numint)
    diff = []
    i = 0
    while i < len(numint):
        square = (mean - numint[i]) ** 2
        i += 1
        diff.append(square)
        var = math.fsum(diff[:])
    print(var)
    str = var ** (1/2)
    print(str)
except ValueError:#not num or separated by comma
    print("please enter valid numbers and separate them by space")
except IndexError:#no input
    print("please enter at least one number")
