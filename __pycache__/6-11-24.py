#simple inheritance---allows derived (or) child class to inherit properties of one parent class

class mosquitoe_repellents:
    def __init__(self,brand,ingredient):
        self.brand=brand
        self.ingredient=ingredient
    def m1(self):
        print(self.brand)
        print(self.ingredient)
class chemical_repellent(mosquitoe_repellents):
    def m2(self,flavour):
        self.flavour=flavour
        print(self.brand)
        print(self.ingredient)
        print(self.flavour)
class electrical_repellent(mosquitoe_repellents):
    def m3(self,light,flavour):
        self.light=light
        self.flavour=flavour
        print(self.brand)
        print(self.ingredient)
        print(self.flavour)
        print(self.light)
brand=input('enter brand :')
ingra=input('enter ingredient :')
l=input('ener light :')
f=input('enter flavour :')
r=electrical_repellent(brand,ingra)
r.m3(l,f)
brand1=input('enter brand :')
ingra1=input('enter ingredient :')
f1=input('enter flavour :')
r1=chemical_repellent(brand1,ingra1)
r1.m2(f1)

"""
class Bankaccount:
    def __init__(self,account_number,balance=0):
        self.account_number=account_number
        self.balance = balance
    def deposite(self,amount):
        self.balance = self.balance+amount
class savings_account(Bankaccount):
    def __init__(self,account_number,balance=0,interest=0.02):
        self.account_number=account_number
        self.balance = balance
        self.interest = interest
    def add_interest(self):
        interest = self.balance * self.interest
        self.balance = self.balance + interest
        print(self.balance)
a_n=int(input('enter acc_no :'))
bal=int(input('enter balance :'))
i=float(input('enter interst :'))
b=savings_account(a_n,bal,i)
b.add_interest()

a1_n=int(input('enter acc_no :'))
bal1=int(input('enter balance :'))
i1=float(input('enter interst :'))
amoun=int(input('enter amount'))
b.deposite(amoun)

"""

#multiple inheritance----a class is derived from more than one parent(or)base class.
"""
class fulltimeemployee:
    def get_hours(self):
        self.hours="40 hrs per week"
    def get_benefits(self):
         self.benifits='eligible for full-time'
class manager:
    def role(self):
        self.role= 'manages team'
    def bonu(self):
        self.bonus='eligible for bonuses'
class fulltimemanager(fulltimeemployee,manager):
    def discription(self):
        print(self.benifits)
        print(self.hours)
        print(self.role)
        print(self.bonus)
emp=fulltimemanager()
emp.discription()
emp.bonus()
emp.get_benefits()

"""


class Device:
    def power_on(self):
        return "device on"
    def power_off(self):
        return "device off"
class phone(Device):
    def call(self):
        return 'making a call'
class smartphone(phone):
    def browse_internet(self):
        return "browser the internet"
s=smartphone()
print(s.browse_internet())
print(s.power_off())
print(s.power_on())
print(s.call())
"""
class Book:
    def __init__(self,title,authoe):
        self.title=input('enter title :')
        self.authoe=input('enter author :')
    def display(self):
        print(self.title)
        print(self.authoe)
class Library(Book):
    def __init__(self,shelf_num):
        self.shelf_num = input('enter shelf :')
    def display_L(self):
        print(self.shelf_num)
        print(self.authoe)
b=Library()
b.display_L()
"""
#hyrachichle inheritance----can inherit multiple classes from single class
"""
class staff:
    def __init__(self,name,staff_id):
        self.name=name
        self.staff_id=staff_id
    def display(self):
        print(self.name)
        print(self.staff_id)
class Teacher(staff):
    def __init__(self,subject):
        self.subject=subject
    def display1(self):
        print(self.subject)
        print(self.name)
        print(self.staff_id)
sub=input('enter subject :')
name=input('enter name :')
staf=int(input('enter id :'))
o2=Teacher(sub)
o2.display1(name,staf)
"""

class vehicle:
    def __init__(self,model,year):
        self.model=model
        self.year=year
    def start(self):
        print("is starting")
    def stop(self):
        print('stopped')
class car(vehicle):
    def seats(self):
        print(4)
class truck(vehicle):
    def capacity(self):
        print('loads heavy goods')

c=car('fh16',8)
t=truck('carmy',9)
c.start()
c.seats()
t.start()
t.capacity()


#hybrid inheritance--it is combination of hierarchical inheritance nd multiple inheritance
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print( self.name)
        print(self.age)
class student(person):
    def display_student(self):
        print(7645)
class teacher(person):
    def display_teacher_info(self):
        print('computers')
class teacherassistant(student,teacher):
    def display_assist(self):
        self.display()
        self.display_student()
        self.display_teacher_info()
t=teacherassistant('ram',30)
t.display_assist()