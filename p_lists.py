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