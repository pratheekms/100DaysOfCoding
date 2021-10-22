


a=5
print('type of a is {}'.format(type(a)))

x=10
y=1.5
z=1j

# l=list(x,y,z)

print(type(z))


sentence='i\'m a banana'

print('banana' in sentence)
print('mango' not in sentence)

name='0123456789'
print(name[-4:-2])

txt1='my name is pratheek  im from b a n g lo re  '
print(txt1.strip())
print((txt1.upper().strip()))

print(txt1.replace('pratheek','Pra'))
print(txt1)

splitname=txt1.split('a')
print(splitname)

myorder='i want {} and {}'
print(myorder.format('burger','fries'))

print('end for day 2')