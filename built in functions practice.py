k=[21,32,63,74,51,6,11,14,15]
s=0
for i in k:
    s = s+1
print(s)

k=[11,3,2,4,6,8,10]
for j in k:
    j = j ** 2
    print(j)

def fact(z):
    if z == 0:
        return 1
    else:
        return (z * fact(z-1))
print(fact(5))

d= lambda a,b : a+b
print(d(33,99))

d = lambda x,y : x if x>y else y
print(d(36,29))

def even_num(p):
    if p % 2 == 0:
        return p
    else:
        return False

p=[11,32,3,44,52,61,73,88]
f=filter(even_num,p)
print(list(f))

from functools import *
t=[2,3,4,5,6,11,9,1]
rs = reduce(lambda x,y :x+y,t)
print(rs)

def sqr(l):
    return l**2
l=[3,5,7,9]
m = map(sqr,l)
print(list(m))

