numstr = input("input a set of numbers: ")
numlist = numstr.split()
numlist.sort()
print(numlist[len(numlist)-1])