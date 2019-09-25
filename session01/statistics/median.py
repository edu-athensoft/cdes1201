numstr = input("to find median, input a set of numbers separated by space: ")
try:
    numlist = numstr.split()
    num = list(map(float, numlist))  # conv to int
    num.sort()  # min to max
    if len(num) % 2 == 1:
        mid = (len(num) - 1) / 2
        print(num[mid])
    else:
        mid = int(len(num) / 2)
        median = (num[mid] + num[mid - 1]) / 2
        print(median)
except ValueError:  # not num or separated by comma
    print("please enter valid numbers and separate them by space")
except IndexError:  # no input
    print("please enter at least one number")
except:
    print("other error occured, please try again")
