"""
Obejct oriented programming language in python is a way to organize code to 
represent data and behaviour using objects.
it helps make code more organised reusable and easier to understand,manage
complex syatems nd scale applications.we have concepts like.
class:
      It defines blueprint for creating objects,encapsulating data nd funtions
      ex:if we have class called Car ,it defines what a car is(like its colour nd model
      nd air bags)
objects:
    objects are instances of classes that hold speciic data nd can perform actions defined 
    by their class
    ex: using the car class, we can create an object like mycar , it has specific details like
    colour:red , model:sedan,  air-bags: 4
inheritance: 
     allows new class to inherit properties and methods from exsting class
     ex: if we have class electricscooty that inherit from scotty ,that electric sccoty will have all 
     features of scotty and some additional ones like battery or charging
encapsulation:
     restricks access to certain components of an object this means keeping inernal details
     of an object hidden. u can control what data is accessible and protect it from being changed directly
polymorphism:
     enables different clases  to be treated as instance of same class through a common interface
     ex:if auton nd cab have methods call drive on either object without worrying about which type it is

     
Use Cases in python :
     opps is widely used in various areas of python development to enhance code organization,reusability and 
     clarity making it easier to built nd maintain complex system
Web development: 
     frame works like Django and flask use oops to structure applications, with models,views nd controllers 
     organised as classes
Game Development:
     libraries  like pygame use classes to represent game entities nd manage their behaviour
Data analysis nd machine learning:
     libraries like pandas utilize oops to encapsulation data structure nd algorithm in classes
Desktop applications: 
     GUI frame work like Tkinter oop to create nd manage user interface element as object
simulation nd modeling:
     oops is used to create models of real worls system where classes can represent entities
     nd their interactions
Financial Applications: 
     in trading platforms,classes can represent finacial insructions tractions nd users accounts

     
Real time apploication:
web application :
    framework uses oops to structure models,views nd templates as classes
game development:
     oops allows to create game objects like players , enemies using classes to manage their behaviour
     nd properties
Desktop application :
     create graphical user interface where buttons nd windows are represent as classes, makes easy to 
     organise app
Data science:
     defines  machine learning models as classes, which predit using different algorithms
robots:
     classes can represent robots nd sensors,makes easier to control nd manage robotic system
simulations:
     in traffic simulation software, cars ,traffic ,lights can be modeled as clsses helps to simulates 
     real world interaction
Networking:
     classes  can manage connections nd data transation in applications
Apis: when bulding service, classes can represents differnce  API endpoints
     makes easy to manage data flow
content management system :
     appliacation like wagatail use classes to handle diirent types of content
finance application:
     in trading platform, we can use classes to model different financial instruments


     
Importance of oops:
    oops enhance code organization,promotes better software design d makes program easier
    to understand maintain nd extend .these r advantages of particualarly valuable in large
     projects
code reusability:
     classes can reusable across different programs.inheritance allows new classes to adopt
     properties nd methods of existingclasses,promting euse nd reducing redundancy
encapsulation:
     oops encapsulate data and methods within classes protecting the integrity of data
abstraction:
     it allows programmers to work with high level abstraction
flexible nd maintaince:
     oops makes easy to modify existing code.it allows easy updates nd enhancements.
real-world:
     objects can represent  real world entities simulate complex systems.
polymorphism:
    different classes to be treated as instance of same class through common interface.
     
class:
      It defines blueprint for creating objects,encapsulating data nd funtions
      ex:if we have class called Car ,it defines what a car is(like its colour nd model
      nd air bags)

class library:
     def books(self,sname):
        print(sname,'reading book completed')
firstbook = library()
firstbook.books('big little lies')
firstbook.books('Dune')



objects:
    objects are instances of classes that hold speciic data nd can perform actions defined 
    by their class
    ex: using the car class, we can create an object like mycar , it has specific details like
    colour:red , model:sedan,  air-bags: 4
class Car:
    def _init_(self,colour,model,airbags)
        self.colour=colour
        self.model=model
        self.airbags=airbags
    def mycar(self):
        print(self.colour)
        print(self.model)
        print(self.airbags) 
newcar = Car('red','nissan',4)
newcar.mycar()

newcar1=Car('white','audi',6)
newcar1.mycar()
    

class washing:
     def _init_(self,name,model,stars)
         self.name=name
         self.model=model
         self.stars=stars
    def machine(self):
          print(self.name)
          print(self.model)
          print(self.stars)
oldmachine=washing('Ifb',Trin7654,5)
oldmachine.machine()

"""