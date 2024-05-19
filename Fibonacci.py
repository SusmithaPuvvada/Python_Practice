#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.

def fib():
    previous_number = 1
    current_number = 1
    next_number = 0
    count = int(input('enter how many number of elements in a sequence:'))
    
    if count == 0:
         fib = []
    elif count == 1:
         fib = [previous_number]
    elif count == 2:
         fib = [previous_number , current_number]
    elif count > 2:
        fib = [previous_number , current_number]
        i = 2     
        while i < count:
            next_number = previous_number + current_number
            fib.append(next_number)
            i +=1
            previous_number = current_number
            current_number = next_number


    print(fib)

fib()