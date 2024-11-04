l=[1,2,3,4,5]
l1=[9,8,7,6]
l.extend(l1)
print(l)
l=[1,2,3,4,5,6]
l.remove(3)
print(l)
l=[3,4,5,6,7]
l.pop(2)
print(l)
l=[1,2,3,1,4,5,1,2]
s=set(l)
p=s.union()
o=list(p)
print(o)

"""
students=[]
num_students=int(input('enter students :'))
for i in range(num_students):
    n=input('enter name:')
    g=input('enter grade:')
    students.append([n,g])
print('student grades :')
for student in students:
    print('name :', student[1], 'grade :', student[0])

print("-------------")
numbers=input('enter numbers, seperated by space:')

l1=[]
l2=[]
for i in numbers:
    if i % 2 == 0:
        l1.append(i)
    else:
        l2.append(i)

print(l1)
print(l2)

def unique():
    input_num = input('enter list of integers, seperated by space :')
    numbers = list(map(int, input_num.split()))
    unique_n=[]
    for num in numbers:
        if num not in unique_n:
            unique_n.append(num)
    return unique_n
unique_list = unique()
print(unique_list)

def get_list():
    number=input('enter numbers, seperated by space :')
    con_num=list(map(int, number.split()))
    emp_list = []
    for i in con_num:
        if i not in emp_list:
            emp_list.append(i)
    return emp_list
list_numbers=get_list()
print(list_numbers)


class Employee:
    def __init__(self,name,montly_salary):
        self.name=name
        self.montly_salary=montly_salary
    def get_details(self):
        return self.name  + str(self.montly_salary)
    def cal_salary(self):
        return self.montly_salary * 12
name = input('enter name:')
montly_salary = float(input('enter salary :'))

employee = Employee(name,montly_salary)

print(employee.get_details())
print(employee.cal_salary())


class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display_info(self):
        print(self.name)
        print(self.age)
        print(self.gender)
    def update_age(self,new_age):
        self.age=new_age
def create_person():
    name = input('enter name :')
    age = input('enter age')
    gender = input('enter name :')
    return Person(name,age,gender)
person1 = create_person()
person2 = create_person()
person3 = create_person()
print('initial information:')
person1.display_info()
person2.display_info()
person3.display_info()
new_age = input('\n Enter new age for' + person1.name+':')
person1.update_age(new_age)
print('\nafer updating:')
person1.display_info()

"""
class BankAccount:
    def __init__(self,deposit,withdraw):
        self.deposit=deposit
        self.withdraw=withdraw
    def bal(self):
        print(self.deposit)
        print(self.withdraw)
    










































