def add_func(num1: int, num2: int)-> int:
    return num1+num2

def sub_func(num1: int, num2: int)-> int:
    return num1-num2

add_s='Sum of {} and {} is {}'
sub_s='Difference between {} and {} is {}'
print(add_s.format(4,5,add_func(4,5)))
print(sub_s.format(10,5,sub_func(10,5)))


new_list=list(('pratheek',25,'banglore')) #list constructor
print(new_list)

def new_func2(name: str,age:int)->str:
    return 'my name is {} and i\'m {} years old'.format(name,age)

my_dict={'john':20,'mark':25,'jake':35,'amy':32,'rachel':23}

for name,age in my_dict.items():
    # print(name, age)
    print(new_func2(name,age))

def new_func3(place:str)->str:
    pass