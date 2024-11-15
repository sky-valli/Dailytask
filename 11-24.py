#polymorhism----diffrent types of objects used in same way.
#Duck typing
class Bird:
    def __init__(self,name):
        self.name=name
    def fly(self):
        print('bird flies')
class aeroplane:
    def __init__(self,name):
        self.name=name
    def fly(self):
        print('aeroplane flies')
b = Bird("kamju")
a = aeroplane("kingfisher")
for flying in (b,a):
    print(flying.name)
    flying.fly()


#overridding-----base class employee with a method cal_sal(),which is 
#              override by each sub class to implement their specific sal
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def cal_sal(self):
        print(self.salary)
class manager(employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus=bonus
    def cal_sal(self):
        print(self.salary + self.bonus)
class engineer(employee):
    def __init__(self,name,salary,hourly_pay,over_time):
        super().__init__(name,salary)
        self.hourly_pay=hourly_pay
        self.over_time=over_time
    def cal_sal(self):
        regular_sal=self.salary
        overtime_pay=self.hourly_pay * self.over_time
        print( regular_sal + overtime_pay )
m = manager('thanish',35000,5000)
m.cal_sal()   
e = engineer('bhasha',60000,120,50)
e.cal_sal()


# OVERLOADING
class shopping:
    def __init__(self):
        self.items = []
    def calculate_total(self,price, quantity = 1, discount=0):
        total = price * quantity
        if discount > 0:
            total = total - (total*discount/100)
        print(total)
s=shopping()
s.calculate_total(256,2,0.2)
s.calculate_total(345,5,0)
s.calculate_total(555,8,0.3)

#operator overloading
class test:
    def add(self):
        print(1762 + 678)
    def add1(self):
        print("operator" + "overloading")
t=test()
t.add()
t.add1()

#method overloading----it returns last method in class ,so it doesn't support overloading
class test1:
    def adding(self):
        print('it wont returns this output')
    def adding(self):
        print('it returns last method')
v=test1()
v.adding()    

#constructor overloading---  it returns last method in class ,so it doesn't support overloading
class test2:
    def __init__(self):
        print('it wont returns this constructor')  
    def __init__(self):
        print('it returns last constructor')
test2()