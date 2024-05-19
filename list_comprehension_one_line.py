#write a program that returns a list that contains only the elements that are common between the lists (without duplicates)

import random

a = random.sample(range(1,100),10)
b = random.sample(range(1,100),11)
c = [x for x in set(a) if x in b]
print(a,b,c)