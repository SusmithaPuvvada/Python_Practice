def factorial(n):
    if (n<0):
        print ("factorial of number", n," doesn't exist.")
    elif (n==0 or n==1):
        return 1
    else:
        fact =1
        for i in range(1,n+1):
            fact = fact*i
        print(' factorial of a number', n, 'is', fact)

if __name__=='__main__':
    n = int(input('enter a number:'))
    factorial(n)