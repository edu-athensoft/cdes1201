import math

numstr = input("to find standard deviation, input a set of numbers separated by space: ")
try:
    numlist = numstr.split()
    num = list(map(float, numlist))  # conv to int

    mean = math.fsum(num[:]) / len(num)
    diff = []
    i = 0
    while i < len(num):
        square = (mean - num[i]) ** 2
        i += 1
        diff.append(square)
        var = math.fsum(diff[:])
    std = var ** (1 / 2)
    print(std)
except ValueError:  # not num or separated by comma
    print("please enter valid numbers and separate them by space")
except IndexError:  # no input
    print("please enter at least one number")
except:
    print("other error occured, please try again")
