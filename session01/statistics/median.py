numstr = input("to find median, input a set of numbers separated by space: ")
try:
    numlist = numstr.split( )
    numint = map(int, numlist)
    numint = list(map(int, numlist))#conv to int
    numint.sort()#min to max
    if len(numint) % 2 == 1:
        mid = int((len(numint)-1) // 2)
        print(numint[mid])
    else:
        mid = len(numint) // 2
        median = (numint[mid-1] + numint[mid]) / 2
        print(median)
except ValueError:#not num or separated by comma
    print("please enter valid numbers and separate them by space")
except IndexError:#no input
    print("please enter at least one number")
