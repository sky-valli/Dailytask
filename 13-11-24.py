#data abstarction---it hides internal details of an object nd only exposes what is neccesarry to user
#abstractmethod---it declares in abstractcalss bt lack of immplementation 
                # acts as placeholders ensures that sub-class of abstract class provide specific functinality
#abstractclass----


from abc import ABC , abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    @abstractmethod
    def habitat(self):
        pass
class dog(animal):
    def sound(self):
        print("bark")
    def habitat(self):
        print('domestic')
class lion(animal):
    def sound(self):
        print('roar')
    def habitat(self):
        print('savanna')
d=dog()
l=lion()
d.sound()
d.habitat()

l.sound()
l.habitat()

class employee(ABC):
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary
    def get_name(self):
        print(self.__name)
    def get_salary(self):
        print(self.__salary)
    def set_salary(self,salary):
        if salary > 0:
            self.__salary=salary
        else:
            raise ValueError("sal must positive")
    @abstractmethod
    def job(self):
        pass
class developer(employee):
    def job(self):
        print('develops and maintain software')
name=input('enter name :')
sal=int(input('enter salary:'))
dev=developer(name,sal)    
dev.job()
dev.set_salary(39000)
dev.get_name()

class vehicles(ABC):
    def __init__(self,model,year):
        self.model=model
        self.year=year
    @abstractmethod
    def moving(self):
        pass
    @abstractmethod
    def stopping(self):
        pass
    def get_info(self):
        print(self.model)
        print(self.year)
class car(vehicles):
    def __init__(self,model,year,engine):
        super().__init__(model,year)
        self.engine=engine
    def moving(self):
        print('car started moving')
    def stopping(self):
        print('car stopped') 
    def get_info(self):
        print(self.model)
        print(self.year)
        print(self.engine)
class bicycle(vehicles):
    def __init__(self,model,year,gear_count):
        super().__init__(model,year)
        self.gear_count=gear_count
    def moving(self,members):
        self.members=members 
        print(self.members)
    def stopping(self,dropped):
        self.dropped=dropped
        print(self.dropped)
    def get_info(self):
        print(self.gear_count)
model=input('enter model:')
year=int(input('enter year:'))
engine=input('enter engine:')

c1=car(model,year,engine)
c1.moving()
c1.stopping()
c1.get_info()     
model1=input('enter model:')
year1=int(input('enter year:'))  
gear_c=int(input('enter count :')) 
b1=bicycle(model1,year1,gear_c)
b1.get_info()
member=int(input('enter menbers:'))
stop=int(input('enter dropped persons:'))
b1.moving(member) 
b1.stopping(stop)
 