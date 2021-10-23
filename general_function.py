def add_func(num1: int, num2: int)-> int:
    return num1+num2

def sub_func(num1: int, num2: int)-> int:
    return num1-num2

add_s='Sum of {} and {} is {}'
sub_s='Difference between {} and {} is {}'
print(add_s.format(4,5,add_func(4,5)))
print(sub_s.format(10,5,sub_func(10,5)))