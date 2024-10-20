d={'name':'sai','age':30}
d['gender']='male'
print(d)
d={'name':'sai','age':30}
f=tuple(d)
print('age' in f)
s={i: i**2 for i in range(1,16)}
print(s)
j={'a':1,'s':2,'d':3}
o={'q':5,'w':6}
p=j.copy()
p.update(o)
print(p)
