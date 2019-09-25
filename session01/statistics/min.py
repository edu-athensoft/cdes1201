numstr = input("to find min, input a set of numbers separated by space: ")
try:
    numlist = numstr.split()
    num = map(float, numlist)
    num = list(num)  # conv to int
    print(min(num))
except ValueError:  # not num or separated by comma
    print("please enter valid numbers and separate them by space")
except IndexError:  # no input
    print("please enter at least one number")
except:
    print("other error occured, please try again")
