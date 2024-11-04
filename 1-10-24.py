"""
Create a class Person that has instance variables name, age, and gender. Add methods to:
Initialize these variables.
Update the age.
Display the person's information.  
 Exercise:
 > Create multiple instances of the Person class.
 > Change the age of one person and display the updated information
"""
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

2.Create a class Company that keeps track of the total number of employees using a static variable total_employees. 
  Each employee has instance variables name and department. Every time an employee is added, the total_employees should increment.
  Exercise:
   >Create multiple employee instances.
   >Print the total number of employees after adding each new employee.
   >Check whether changing the total_employees in one instance affects the others.
"""


class Company:
    total_employees = 0
    def __init__(self):
        self.employees = []
    
    def add_employee(self, name, department):
        employee = Employee(name, department)
        self.employees.append(employee)
        Company.total_employees += 1
        print('Added employee: ' + employee.name + ', Department: ' + employee.department)
        print('Total Employees: ' + str(Company.total_employees))
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department
company = Company()
num_employees = int(input("How many employees do you want to add? "))
for _ in range(num_employees):
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    company.add_employee(name, department)
print('\nFinal Total Employees: ' + str(Company.total_employees))
print('\nChanging total_employees directly for demonstration (not recommended in practice):')
Company.total_employees += 5
print('Total Employees after modification:' + str(Company.total_employees))

"""
3.Create a class Rectangle that has instance variables length and width. 
  Add a method calculate_area that calculates and prints the area of the rectangle using local variables inside the method.
  Exercise:
    >Create instances of the Rectangle class with different lengths and widths.
    >Calculate and print the area for each rectangle.
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width  
        print('Area of rectangle with length ' + str(self.length) + ' and width ' + str(self.width) + ' is ' + str(area))

rectangles = []
num_rectangles = int(input("How many rectangles do you want to create? "))
for _ in range(num_rectangles):
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    rectangle = Rectangle(length, width)
    rectangles.append(rectangle)

print("\nAreas of the Rectangles:")
for rectangle in rectangles:
    rectangle.calculate_area()

"""
4.Create a class Employee where:
  Each employee has an instance variable salary.
  There is a static variable bonus shared by all employees. The bonus is applied to each employee's salary.
  Write a method total_salary that calculates the total salary for an employee (including the bonus).
  Exercise:
   >Create several employee instances with different salaries.
   >Change the bonus amount (static variable) and see how it affects all employees.
   >Calculate and print the total salary for each employe
"""
class Employee:
    bonus = 0  

    def __init__(self, salary):
        self.salary = salary

    def total_salary(self):
        total = self.salary + Employee.bonus  
        print('Total salary for employee with salary ' + str(self.salary) + ' is ' + str(total))


employees = []

num_employees = int(input("How many employees do you want to create? "))
for _ in range(num_employees):
    salary = float(input("Enter salary: "))
    employee = Employee(salary)
    employees.append(employee)

print("\nTotal Salaries of Employees:")
for employee in employees:
    employee.total_salary()


new_bonus = float(input("\nEnter the new bonus amount: "))
Employee.bonus = new_bonus


print("\nTotal Salaries of Employees After Bonus Change:")
for employee in employees:
    employee.total_salary()
