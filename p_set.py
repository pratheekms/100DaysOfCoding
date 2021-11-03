#set

s1={1,2,3,4,4,5,3,4,1}
print(s1)

#list to set
l1=[1,2,3,4,5,5,4,3,2,1]
print('lsit:{}'.format(l1))
s2=set(l1)
print('set:{}'.format(s1))


s2.add(10)
print(s2)
print(s2)

s2.remove(10)
print(s2)

#remove item in sets, discard and remove

#discard wont through error if the item is not found
#but remove in throguh an error if item not found
s2.discard(10)
print(s2)