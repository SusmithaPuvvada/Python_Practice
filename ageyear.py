import datetime

name = input('enter your name:')
age = int(input('enter your age:'))
today = datetime.date.today()
year = today.year
print('The year when',name,'has 100 years old is',(year+(100-age)),'.' )
