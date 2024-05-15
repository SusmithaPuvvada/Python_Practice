#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 

num = int(input('enter a number:'))
if num % 2 ==0:
    print('The number',num, ' is even.')
else:
    print('The number', num, 'is odd.')