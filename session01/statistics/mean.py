import math

numstr = input("to find mean, input a set of numbers separated by space: ")
try:
    numlist = numstr.split()
    num = list(map(float, numlist))  # conv to int

    print(math.fsum(num[:]) / len(num))
except ValueError:  # not num or separated by comma
    print("please enter valid numbers and separate them by space")
except IndexError:  # no input
    print("please enter at least one number")
except:
    print("other error occured, please try again")
