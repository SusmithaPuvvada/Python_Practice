#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

num = int(input('enter a number:'))

list_range = list(range(1,num+1))

divisors=[]

for x in list_range:
    if num % x == 0:
        divisors.append(x)

print(divisors)