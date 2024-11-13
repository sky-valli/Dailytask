# single inheritance with overloading
#single inheritance----allows class to inherit all properties nd methods from parent class
#overridding----we can add extra features to child class which is already available in paent class
class Animal():
    def __init__(self,name):
        self.name=name
    def speak(self):
        print('animal sound')
class Dog(Animal):
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("bow bow")
d=Dog('lab')
d.speak()

print("====single====")

# Multiple inheritance---a class is derived from one or more parent class
class Teacher:
    def __init__(self,subject):
        self.subject=subject
    def display(self,marks):
        self.marks=marks
class researcher:
    def __init__(self,field):
        self.field=field
    def display1(self):
        print('researching on a topic')
class tachingresearching(Teacher,researcher):
    def __init__(self,subject,field):
        super().__init__(subject)
        researcher.__init__(self,field)
    def display(self):
        print(self.subject)
        print(self.field)
        super().display(100)
        print(self.marks)
        super().display1()
r=tachingresearching('com','oops')
r.display()
        
class bird:
    def __init__(self,species):
        self.species=species
class flyable:
    def fly(self):
        print('bird can fly')
class eagle(bird,flyable):
    def __init__(self, species):
        super().__init__(species)
    def display(self):
        print(self.species)
        super().fly()
e=eagle('blad eagle')
e.display()

print("====multiple====")
#Multi level inheritance---allows each class to inherit all properties and methods fromits parent calss
        
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
class employee(person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def display1(self):
        print(self.salary)
        print(self.name)
        print(self.age)
class manager(employee):
    def __init__(self,name,age,salary,department):
        super().__init__(name,age,salary)
        self.department=department
    def display2(self):
        print(self.salary)
        print(self.name)
        print(self.age)
        print(self.department)
p=manager('sarika',29,30000,'developer')
p.display2()

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(self.name)
        print(self.salary)
class developer(employee):
    def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language=programming_language
    def display(self):
        print(self.name)
        print(self.salary)
        print(self.programming_language)
class manager(employee):
    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size=team_size
    def display(self):
        print(self.name)
        print(self.salary)
        print(self.team_size)
class intern(developer):
    def __init__(self,name,salary,programming_language,intership_duration):
        super().__init__(name,salary,programming_language)
        self.intership_duration=intership_duration
    def display(self):
        print(self.name)
        print(self.salary)
        print(self.programming_language)
        print(self.intership_duration)
e1=employee('harika',29)
e1.display()
d1=developer('harika',29,'python')
d1.display()
m1=manager('harika',35000,20)
m1.display()
u=intern('harika',35000,"python",'two months')
u.display()
    
class vehicle:
    def __init__(self,brand,models):
        self.brand=brand
        self.models=models
    def display(self):
        print(self.brand)
        print(self.models)
class car(vehicle):
    def __init__(self,brand,models,num_doors):
        super().__init__(brand,models)
        self.num_doors=num_doors
    def display(self,num_seats):
        self.num_seats=num_seats
        super().display()
        print(self.brand)
        print(self.models)
        print(self.num_seats)
        print(self.num_doors)
class bike(vehicle):
    def __init__(self,brand,models,type):
        super().__init__(brand,models)
        self.type=type
    def display(self,wheels):
        self.wheels=wheels
        print(self.brand)
        print(self.models)
        print(self.wheels)
        print(self.type)
v=bike('honda',2023,'petrol_engine_type')
v.display(2)
c2=car('adi',2024,4)
c2.display(4)
        
print('====hierarchical=====')

#Hybrid inheritance----it is combination oif hierarchical and multiple inheritance
class device:
    def __init__(self,name):
        self.name=name
class phone(device):
    def __int__(self,name,phone_num):
        super().__init__(name)
        self.phone_num=phone_num
class tablet(device):
    def __int__(self,name,screen_size):
        super().__init__(name)
        self.screen_size=screen_size
class smartphone(phone,tablet):
    def __init__(self,name,phone_num,screen_size,os):
        phone.__int__(self,name,phone_num)
        tablet.__int__(self,name,screen_size)
        self.os=os
    def display(self):
        print(self.name)
        print(self.phone_num)
        print(self.screen_size)
        print(self.os)
s=smartphone('redme',8766544332,'any','installed')
s.display()

print("====hybrid====")

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def dispaly(self):
        print(self.name)
        print(self.age)
class student(person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade
    def display(self):
        print(self.grade)
        print(self.name)
        print(self.age)
stu=student('harika',29,'A')
stu.dispaly()
