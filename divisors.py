#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

num = int(input('enter a number:'))

divisors=[x for x in range(2,num) if num % x==0]

print(divisors)