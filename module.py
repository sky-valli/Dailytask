def fun(v,b):
    return v+b

def get_evens(l):
    n=[]
    for i in l:
        if i%2 == 0:
            n.append(i)
    return n 

from datetime import date,time
import datetime
import random



print(dir(datetime))
print(date.today())
print(datetime.datetime.now())
print(dir(random))

for i in range(1,10):
    print(random.random())

for i in range(1,15):
    print(random.randint(100,200))

for i in range(1,5):
    print(random.randrange(5))

for i in range(1):
    print(random._floor(5.78))

for i in range(3):
    print(random._ceil(6.65))

import math

print(dir(math))
print(math.floor(99.9))
print(math.floor(16.17))
print(math.ceil(18.28))
print(math.factorial(5))
print(math.sqrt(4))