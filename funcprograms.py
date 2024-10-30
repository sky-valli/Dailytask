#define function name greet that takes name as argument and print a greeting message
def greet(name):
    return name
print('Hello,[name]!')

#write function 'add_numbers' that takes 2 numbers as argument nd returns their sum.
def add_num(i,u):
    return i+u
print(add_num(78,16))

#create function 'is_even' that takes number as argument nd return 'True' if number is even otherwise false
def is_even(num):
    if num % 2 == 0:
        return True
    else:
         return False
print(is_even(22))
print(is_even(77.9))
print(is_even(10000))

#write function on factorial takes positive integer as input nd returns factorial of number
def fac(s):
    if s == 0:
        return 1
    else:
        return s * fac(s-1)
print(fac(5))

#define function find_max that takes 3 numbers as input nd returns largest of 3.
"""
def find_max():
    k=int(input('enter :'))
    j=int(input('enter :'))
    h=int(input('enter :'))
    return max(k,j,h)
print(find_max())


#write fun 'count_vowels' takes string as input nd returns no.of voewls
def count_vowels():
    i=input('enter vowels :')
    v='aeiou'
    count = 0
    for c in i:
        if c in v:
            count = count+1
    return count
print(count_vowels())
"""
#wirite function 'is_prime' that takes num as input nd returns True if num is prime
def is_prime(u):
    u=11
    if u>1:
        for i in range(2,int(u/2)+1):
            if (u%i)==0:
                print('not a prime')
                break
        else:
            print('is a prime')
    else:
        print('not prime')
is_prime(22)

#write recursive fun 'recursive_sum' takes positive integer n ns return sum of all numbers1 to n
def recursive_sum(n):
    if n==0 :
        return 1
    else:
        return n+recursive_sum(n-1)
print(recursive_sum(7))

#write fun 'cal' takes 3 parameters 2 num nd an operator(as string )
def cal(n1,n2,o):
    if o == '+':
        return n1 + n2
    elif o == '-':
        return n1 - n2
    elif o == '*':
        return n1 * n2
    elif o == '/':
        if n2 != 0:
            return n1/n2
        else:
            return 'Error: Division by zero'
    else:
        return 'Error: o is Invalid'
print(cal(16,3,'*'))

#write a fun 'reverse_str' takes str as input nd returns list of elements in both sets
def reverse_str(d):
    return d[::-1]
print(reverse_str('reverse string using function'))

#write a function sort_dict_by_value takes dict as input 
def sort_dict(v):
    return sorted(v.items(),key=lambda x:x[1])
