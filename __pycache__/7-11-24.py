class vehicle:
    def __init__(self,name,wheels,doors,colour):
        self.name=name
        self.wheels=wheels
        self.doors=doors
        self.colour=colour
    def electric_car(self):
        print(self.name)
        print(self.wheels)
    def car(self):
        print(self.doors)
        print(self.colour)
class vehicle1(vehicle):
    def __init__(self,name,wheels,doors,colour,engine,seats):
        self.engine=engine
        self.seats=seats
        super().__init__(name,wheels,doors,colour)
        
    
    def electric_car(self):
        super().electric_car()
        print(self.engine)
        print(self.seats)
    def car(self):
        super().car()
class vehicle2(vehicle):
    def __init__(self,name,wheels,doors,colour,load_capacity):
        super().__init__(name,wheels,doors,colour)
        self.load_capacity=load_capacity
    def electric_car(self):
        super().electric_car()
        print(self.load_capacity)
    def car(self):
        super().car()
c=vehicle1('car',4,'petrolengine',4,4,'red')
c.electric_car()
c.car()
v=vehicle2('truck',6,'10qinta',4,'green')
v.electric_car()
v.car()

#super() using constructor,instance,static,class method 

class P:
    def __init__(self):
        print("this is perent class constrocter")
    def m1(self):
        print("this is instnace method")
    @classmethod
    def m2(cls):
        print("this is clasmethod")
    @staticmethod
    def m3():
        print("this is static method")
class Car(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    @staticmethod
    def m5():
        super(Car,Car).m3()
    @classmethod
    def m6(cls):
        super().m2()
        super().m3()
        super(Car,cls).__init__(cls)
        super(Car,cls).m1(cls)
        

c= Car()
c.m5()
c.m6()
#super() Using Instance method

class staff:
    def __init__(self,name,staff_id):
        self.name=name
        self.staff_id=staff_id
    def display(self):
        print(self.name)
        print(self.staff_id)
class Teacher(staff):
    def __init__(self,name,staff_id,subject):
        super().__init__(name,staff_id)
        self.subject=subject
    def display(self):
        super().display()
        print(self.subject)
sub=input('enter subject :')
name=input('enter name :')
staf=int(input('enter id :'))
o2=Teacher(name,staf,sub)
o2.display()

#super using Static method----in super() function we can only access @staticmethod from child class @staticmethod
class Book:
    def __init__(self,title,authoe):
        self.title=title
        self.authoe=authoe
        print(self.title)
        print(self.authoe)
    @staticmethod
    def display():
        print('this is staic')
class Library(Book):
    def __init__(self,title,authoe,shelf_num):
        super().__init__(title,authoe)
        self.shelf_num = shelf_num
        print(self.title)
        print(self.authoe)
    @staticmethod
    def display():
        super(Library,Library).display()
titl=input('enter title :')
aut=input('enter author :')
shel=int(input('enter shelf :'))
b=Library(titl,aut,shel)
b.display()

#super() using classmethod

class Bankaccount:
    def __init__(self,account_number,balance=0):
        self.account_number=account_number
        self.balance = balance
        
    @classmethod
    def deposite(cls,amount):
        cls.balance = cls.balance+amount
class D(Bankaccount):
    def __init__(self,account_number,balance=0):
        super().__init__(account_number,balance=0)
    @classmethod
    def deposite(cls,amount):
        super().deposite(amount)
        super(D,cls).__init__(cls)
s=D(12334456,4567)
s.deposite()