#oop

class person():
    def __init__(self,fname:str,lname:str) -> None:
        self.fname=fname
        self.lname=lname
    def show_full_name(self):
        print('fullname:{} {}'.format(self.fname,self.lname))

myname=person('john','cena')

myname.show_full_name()

print(myname.fname)
print(myname.lname)

