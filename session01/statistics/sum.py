numstr = input("to find sum, input a set of numbers separated by space: ")
try:
    numlist = numstr.split( )
    numint = map(int, numlist)
    numint = list(map(int, numlist))#conv to int
    import math
    print(math.fsum(numint[:]))
except ValueError:#not num or separated by comma
    print("please enter valid numbers and separate them by space")
except IndexError:#no input
    print("please enter at least one number")
