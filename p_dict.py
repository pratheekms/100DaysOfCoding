#dict
d1={
    1:'one',
    2:'two',
    3:'three',
    4:'TWO'
}

print(d1)

for i in d1.values():
    print(i)

for i in d1.keys():
    print(i)

for i,j in d1.items():
    print(i,j)

print(d1[1])
print(d1.get(4))

d1.update({4:'four'})
print(d1)