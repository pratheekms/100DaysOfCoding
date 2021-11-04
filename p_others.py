from typing import Match, Optional, SupportsComplex


# iterators
# scope 
# module 
# dates 
# math 
# json
# regex 
# pip 
# try..except 
# user iput 
# string formating 

#iter....__iter__(), __next__()
#create an iter object and use next to iter on them

list1=[1,2,3,4,5,6,7]
itl=iter(list1)
print(next(itl))
print(next(itl))
print(next(itl))

#python dates
import datetime
x=datetime.datetime.now()
print(x,x.strftime('%Z'))
print(x.year)

#strftime
y=datetime.datetime(2021,11,4)
print(y)
print(y.strftime('%C'))

myorder='your order is {} {} with a price {:.2f}'
print(myorder.format('burger','fries',23.3423))