def add(x,y):
    print("x -" , x)
    print("y -" , y)
    print(x-y)
add(19,20)
add(34,16)

def wish(msg,name):
    print(msg+name)
wish(name='hi',msg='sai')
wish(msg='hi',name='ram')

def variable(*l):
    t=0
    for i in l:
        t = t+1
    return t
print(variable(11,45,67,8,3,9,18))


def data(email,firstname,Llastname=False):
    print(email)
    print(firstname)
    print(Llastname)
data("ravi@gmail.com","ravi")
data("sai@gmail.com","sai","kanakala")