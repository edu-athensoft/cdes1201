numstr = input("input a set of numbers separated by space: ")
try:
    numlist = numstr.split( )
    numint = map(int, numlist)
    numint = list(map(int, numlist))#conv to int
    numint[0]
    numint.sort()#min to max
    print(numint[len(numint)-1])
except ValueError:#not num or separated by comma
    print("please enter valid numbers and separate them by space")
except IndexError:#no input
    print("please enter at least one number")
