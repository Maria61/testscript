# TODO:递归函数

# 阶乘
def fact(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    else:
        return n*fact(n-1) #返回语句中包含表达式，因此不是尾递归

# 尾递归方式
def fact1(n):
    return fact_iter(n,1)
def fact_iter(n,p):
    if n==1:
        return p
    else:
        return fact_iter(n-1,n*p)

# print(fact(5))
# print(fact(0))
# print(fact(100))
# print('-------------------------------------')
# print(fact1(100))

# 汉诺塔
def move(n,a,b,c): # 将n个盘子从a借助b移动到c
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        print(a,'-->',c)
        move(n-1,b,a,c)

move(3,'A','B','C')