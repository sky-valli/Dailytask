def prac(name):
    print(name)
prac("cohort")

def exam(e,c,p,j,t):
    total=e+c+p+j+t
    print(total)
    print ((total/tm)*100)
e=80
c=70
p=85
j=78
t=90
tm=500
exam(e,c,p,j,t)
e=70
c=80
p=95
j=83
t=85
exam(e,c,p,j,t)


def adding(m,n):
    return m+n
print(adding(67,55))

def count(d):
    l=len(d)
    d1={}
    for i in d:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    return d1
d="pythonknowledgetransferteam"
print(count(d))