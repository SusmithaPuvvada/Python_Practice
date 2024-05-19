# Write a program to list out the common elements in two random lists without duplicates.


import random

a = [random.randint(1,10) for i in range (random.randint(10,15))]
b = [random.randint(1,10) for i in range (random.randint(10,20))]
c=[]

for x in a:
    if (x in b and x not in c):
        c.append (x)

print(a,b,c)



