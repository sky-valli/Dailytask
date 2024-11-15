"""
    1.Create a class Vehicle with attributes brand and year. The class should have a method get_info() that returns the brand and year of the vehicle. Then, create two subclasses:

Car, which adds an attribute number_of_doors.
Motorcycle, which adds an attribute has_sidecar.
Both subclasses should override the get_info() method to include their respective additional attributes in the returned string.
"""
class vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def def_info(self):
        print(self.brand)
        print(self.year)
class car(vehicle):
    def __init__(self,brand,year,num_doors):
        super().__init__(brand,year)
        self.num_doors=num_doors
    def def_info(self):
        print(self.brand)
        print(self.year)
        print(self.num_doors)
class motorcycle(vehicle):
    def __init__(self, brand, year,side_car):
        super().__init__(brand,year)
        self.side_car=side_car
    def get_info(self):
        print(self.brand)
        print(self.year)
        print(self.side_car)
m=motorcycle('honda',2023,'yes')
m.get_info()    
        
"""
        2.Define an abstract class Animal with an abstract method make_sound(). Then, create three classes that inherit from Animal:

Dog with the sound "Woof".
Cat with the sound "Meow".
Cow with the sound "Moo".
Create a function play_sound(animal) that takes an object of type Animal and calls its make_sound() method.

"""

from abc  import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class dog(animal):
    def make_sound(self):
        print("bow bow")
class cat(animal):
    def make_sound(self):
        print("meow meow")
class cow(animal):
    def make_sound(self):
        print("ambaa")

def play_sound(animal):
    animal.make_sound()
d=dog()
c=cat()
c1=cow()
play_sound(d)
play_sound(c)
play_sound(c1)
    


                
"""
            
class BankAccount(ABC):
    def __init__(self, initial_balance=0):
        self._balance = initial_balance  # Private variable for balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self): 
        pass
class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("Deposited", amount, "New balance:", self.get_balance())
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self._balance - amount >= 500:
                self._balance -= amount
                print("Withdrew", amount, "New balance:", self.get_balance())
            else:
                print("Cannot withdraw: balance cannot go below $500.")
        else:
            print("Withdrawal amount must be positive.")
    def get_balance(self):
        return self._balance

savings = SavingsAccount(1000)
savings.deposit(500)
savings.withdraw(200)
savings.withdraw(1500)  # This should fail, trying to go below $500
print("Savings Account Balance:", savings.get_balance())
        
"""
class bank_acc:
    def __init__(self,initial_bal=0):
        self._bal=initial_bal
    @abstractmethod
    def deposite(self, amount):
        pass
    @abstractmethod
    def withdrawl(self, amount):
        pass
    @abstractmethod
    def get_bal(self):
        pass
class savings_acc(bank_acc):
    def deposite(self, amount):
        if amount > 0:
            if self._bal ==  self._bal + amount:
                print('deposited',amount,'new balance',self.get_bal())
        else:
            print('deposite amount must positive')
    def withdrawl(self, amount):
        if amount >= 0:
            if self._bal - amount >= 500:
                self._bal = self._bal - amount
                print('withdraw',amount,'newbalnce',self.get_bal())
            else:
                print("cann't withdraw less than 500")
        else:
            print('must be positive')
    def get_bal(self):
        return self._bal
class current_acc(bank_acc):
    def deposite(self,amount):
        if amount > 0:
            self._bal = self._bal + amount
            print('deposited',amount,'new_bal',self.get_bal)
        else:
            print('deposited amount must be positive')
    def withdrawl(self, amount):
        if amount > 0:
            if self._bal-amount >= -1000:
                self._bal = self._bal - amount
                print('withdraw',amount,'new withdraw',self.get_bal())
            else:
                print('withdraw amount : over draftted limit exceeded')
        else:
            print('amount must be positive')
    def get_bal(self):
        return self._bal
                
savings = savings_acc(1000)
savings.deposite(500)
savings.withdrawl(200)
savings.withdrawl(1500)  # This should fail, trying to go below $500
print("Savings Account Balance:", savings.get_bal())
w=current_acc(500)
w.deposite(400)
w.withdrawl(1200)
print(w.get_bal())
                
"""

4.Create a base class Employee with attributes name and salary, and methods get_details() and get_salary(). Then create two subclasses:

Manager, which adds an attribute department.
Developer, which adds an attribute programming_language.
Both subclasses should override the get_details() method to include their respective additional attributes in the returned string.

Add a method increase_salary(percent) in the Employee class that
increases the salary by a given percentage.

"""
class employee:
    def __init__(self,name,salary):
        self.name=name   
        self.salary=salary
    def get_details(self):
        print(self.name)
        print(self.salary)
    def get_sal(self):
        return self.salary
    def increase_salary(self,percentage):
        if percentage > 0:
            increase = self.salary * (percentage/100)
            self.salary=self.salary + increase
            print('salary increased by',percentage,'new salary',self.salary)
        else:
            print('percentage must be positive')
        
        
class manager(employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department
    def get_details(self):
        print(self.name)
        print(self.salary)
        print(self.department)
class developer(employee):
    def __init__(self,name,salary,programming_lang):
        super().__init__(name,salary)
        self.programming_lang=programming_lang
    def get_details(self):
        print(self.name)
        print(self.salary)
        print(self.programming_lang)
m1=manager('naresh',70000,'development')
m1.get_details()
d1=developer('suresh',72000,'python')
d1.get_details()
m1.increase_salary(10)
d1.increase_salary(12)
           
from abc import ABC ,abstractmethod

class media(ABC):
    @abstractmethod
    def play(self):
        pass
class audio(media):
    def play(self):
        print('plays .mp3 file')
class vedio(media):
    def play(self):
        print('plays .mp4 file')
class livestream(media):
    def play(self):
        print('plays live stream')
def start_media(media):
    media.play()
a=audio()
v=vedio()
l=livestream()
start_media(a)
start_media(v)
start_media(l)

class library:
    @abstractmethod
    def borrow(self):
        pass
    @abstractmethod
    def return_item(self):
        pass
class book(library):
    def __init__(self,title,author,num_copies):
        self.title=title
        self.author=author
        self.num_copies=num_copies
    def borrow(self):
        if self.num_copies > 0:
            self.num_copies=self.num_copies-1
            print('borrowed book',self.title,'copies left',self.num_copies)
        else:
            print('sorry, the book ',self.title,'is currently unavailable')
    def return_item(self):
        self.num_copies=self.num_copies+1
        print('returned book',self.title,'copies available',self.num_copies)
        
class dvd(library):
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
    def borrow(self):
        if not self.borrow:
            self.borrow=True
            print('borrowed dvd',self.title,'directored by self.director')
        else:
            print('sorry,dvd',self.title,'is already borrowwd')
    def return_item(self):
        self.borrow = False
        print('returned dvd',self.title,'is not available')
            
def borrow_items(library):
    library.borrow()
b1=book('2016','nightgale',3)
d1=dvd('deception','orwel',159)
borrow_items(b1)
borrow_items(b1)
borrow_items(d1)
    