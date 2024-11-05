"""
1.basic instance variable using input variable
class Library:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def l(self):
        print(self.name)
        print(self.address)
name=input('enter name :')
address=input('enter address :')
lib=Library(name,address)
lib.l()

2.instance variable with default variable using input

class Library:
    def __init__(self,name='unknown',address='unknown'):
        self.name=name
        self.address=address
    def l(self):
        print(self.name)
        print(self.address)
name=input('enter name :')
address=input('enter name :')
if not name:
    name='unknown'
else:
    adress='not know'
l1=Library(name,address)
l1.l()

Create a class Person that has instance variables name, age, and gender. Add methods to:
#Initialize these variables.
#Update the age.
#Display the person's information.
# Exercise:
 #> Create multiple instances of the Person class.
 #> Change the age of one person and display the updated information

 class Person:
    def __init__(self,name,age,gender,phone_no,account_no):
        self.name=name
        self.age=age
        self.gender=gender
        self.phone_no=phone_no
        self.account_no=account_no
    def person_details(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.phone_no)
        print(self.account_no)
    def update(self,new_age,new_phone_no):
        self.age=new_age
        self.phone_no=new_phone_no
p=[]
for i in range(1):
    name=input('enter name:')
    age=int(input('enter age :'))
    gender=input('enter gender:')
    phone=int(input('enter number :'))
    account=int(input('enter account :'))


    person=Person(name,age,gender,phone,account)
    p.append(person)
for person in p:
    person.person_details()


update_age=int(input('enter new age :'))
update_phone=int(input('enter new phone :'))

p.update(update_age,update_phone)
for person in p:
    person.person_details()

#2.Create a class Company that keeps track of the total number of employees using a
# static variable total_employees.
#  Each employee has instance variables name and department. Every time an employee is
# added, the total_employees should increment.
#  Exercise:
#   >Create multiple employee instances.
#   >Print the total number of employees after adding each new employee.
#   >Check whether changing the total_employees in one instance affects the others

3.Create a class Rectangle that has instance variables length and width.
#  Add a method calculate_area that calculates and prints the area of the rectangle
# using local variables inside the method.
#  Exercise:
#    >Create instances of the Rectangle class with different lengths and widths.
#    >Calculate and print the area for each rectangle



class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
        area = self.length * self.width
        print(str(self.length) + str(self.width) +str(area))
f=[]
ran=int(input('enter how many rectangles :'))
for i in range(ran):
    length = int(input('enter length:'))
    width = int(input('enter input :'))
    ref = Rectangle(length,width)
    f.append(ref)
print('\n area of rectangle')
for ref in f:
    ref.calculate_area()

class Account:
    def __init__(self,account_holder):
        self.account_holder=account_holder
        self.balance=0.0
    def deposite(self,amount):
        self.balance = self.balance + amount
        print(str(amount))
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance=self.balance-amount
            print(str(amount))
        else:
            print('insufficient funds')
    def check_balance(self):
        print(str(self.balance))
def main():
    account = Account()
    action = input('choose action (deposite,withdraw,check balance):')
    if action == 'deposite':
        amount = float(input('enter deposite:'))
        account.deposite(amount)
    elif action =='withdraw':
        amount = float(input('enter withdraw :'))
        account.withdraw(amount)
    elif action == 'check balance':
        account.check_balance()
    else:
        print('inald action')

if __name__ == 'main':
    main()
"""
#class method.
class Employee:
    company_name = 'skywaves'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
    def display(self):
        print(self.name)
        print(self.age)
        print(Employee.company_name)
name=input('enter name :')
age=int(input('enter age :'))
emp=Employee(name,age)
emp.display()
new_company=input('entser company :')

Employee.change_company(new_company)
emp.display()
