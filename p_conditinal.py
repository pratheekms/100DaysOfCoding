#conditional

#if
b='True'
if not b:
    print('true')
    b=0
elif b=='True':
    print('false',b)
else:
    print('nothing')

if b: print('true b')

l1=['y','n']

inp=input('your y/n')
while inp not in l1:
    inp=input('your y/n')
    if inp in l1:
        break

