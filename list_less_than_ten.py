#write a program that prints out all the elements of the list that are less than 10.

a=[]
n = int(input('enter a number:'))
for i in range (0,n):
    ele = int(input())
    a.append(ele)

b=[]
for j in range(0,n):
    if a[j] < 10:
        b.append(a[j])
print ('The numbers less than 5 in a list is:', b)