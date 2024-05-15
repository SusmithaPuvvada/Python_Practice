#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime

name = input('enter your name:')
age = int(input('enter your age:'))
today = datetime.date.today()
year = today.year
print('The year when',name,'has 100 years old is',(year+(100-age)),'.' )
