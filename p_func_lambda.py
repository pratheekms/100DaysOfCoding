# functions and lambda

def print_whatever_twice(st:str)->str:
    print(st*2+ ' in func')
    return st*2

print(print_whatever_twice('hi'))

#*args and **kwargs

def fargs(*l1):
    print(l1[2])

def fkwargs(**k1):
    print(k1['place'])

fargs('one','two','three')
fkwargs(name='myname',place='myplace')




