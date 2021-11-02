# list constructor
import random
new1=list((('pratheek','m','s',26),4,5,6,7))
print(new1[0][3])


#create a random list
rlist=random.sample(range(10,50),10)
print(rlist)

newl=[x for x in range(10) if x%2==0]
print(newl)

slist=['a','b','c','A','B','C']
slist.sort()
print(slist)
slist.sort(key=str.lower)
print(slist)

print('list')

newl1=[1,2,3]
newl1.append(4)
newl2=[5,6,'7']
newl1.extend(newl2)
print(newl1)
newtp=('1',2,'string')
newl1.extend(newtp)
print(newl1)
print('converting list {} to tuple:{}'.format(newl1,tuple(newl1)))

print(newl1)
newl1.pop()
newl1.pop(4)
del newl1[3]
cpnewl1=newl1.copy()
newl3=newl1
newl1.clear()
print(newl1,cpnewl1,newl3)
cpnewl1.append('string')
stringl=[x.upper() for x in cpnewl1 if x=='string']
print(stringl)

#test list comprehension with if

l4=[1,2,3,4,5,6,7,8,9,0]
s4=['even' if num%2==0 else 'odd' for num in l4]
print(s4)
