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

#lambda, can have any number of arguments but only one expression
#parameter: inside ()
#arguments: value pass to the function

x=lambda x:x+5
print(x(5))

y=lambda a,b:a*b
print(y(4,4))

