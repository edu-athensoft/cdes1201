numstr = input("to find max, input a set of numbers separated by space: ")
try:
    numlist = numstr.split( )
    numint = map(float, numlist)
    numint = list(map(float, numlist))#conv to int
    #numint.sort()#min to max
    #print(numint[len(numint)-1])
    print(max(numint))
except ValueError:#not num or separated by comma
    print("please enter valid numbers and separate them by space")
except IndexError:#no input
    print("please enter at least one number")
except:
    print("other error occur")
