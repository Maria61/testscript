import math

# print(abs(-2.34))
# print(max(-1,-2,-3))
# print(abs('a'))

#
# str2 = "ab"
# str3 = "cd"
# str4 = str2 + str3
# str5 = "abcd"
# print(str4 is str5)

# print(hex(10))
# print(hex(1))
# h=hex # 可重命名
# print(h(10))


def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# print(my_abs(-323))

def my_nop():
    pass

# 求一元二次方程的解
def quadratic(a,b,c):
    if not isinstance((a),(int,float)):
        raise TypeError('bad operand type')
    if not isinstance((b),(int,float)):
        raise TypeError('bad operand type')
    if not isinstance((c),(int,float)):
        raise TypeError('bad operand type')
    if b*b-4*a*c < 0:
        print('方程无解')
        return
    x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x1,x2


def add_end(L=[]):
    L.append('end')
    return L


def add_end1(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L

def cal(*num):
    s = 0
    for n in num:
        print(n)
        s += n
    return s

def person(name,age,**kw):
    print('name:',name,',age:',age,',other:',kw)

def person1(name,age,*,city,job):
    print(name,age,city,job)

def person2(name,age,*zzz,city,job):
    print(name,age,zzz,city,job)

def person3(name,age,*,city='ShanXi',job):
    print(name,age,city,job)