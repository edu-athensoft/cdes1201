numstr = input("to find min, input a set of numbers separated by space: ")
try:
    numlist = numstr.split( )
    numint = map(int, numlist)
    numint = list(map(int, numlist))#conv to int
    numint.sort()#min to max
    print(numint[0])
except ValueError:#not num or separated by comma
    print("please enter valid numbers and separate them by space")
except IndexError:#no input
    print("please enter at least one number")
