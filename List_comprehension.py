#Write a one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a = [int(x) for x in input('Enter elements seperated by space :').split()]
c = [i for i in a if i%2 == 0]
print(c)