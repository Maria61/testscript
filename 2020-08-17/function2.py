from my_function import my_abs
from my_function import my_nop
from my_function import quadratic
from my_function import add_end
from my_function import add_end1
from my_function import cal
from my_function import person
from my_function import person1
from my_function import person2
from my_function import person3
# print(my_abs(-38768))
# my_nop()
# print("nop执行后")


# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')


# print(quadratic(1,1,1))
# x,y = quadratic(2,3,1)
# print(x,y)


# print(add_end()) #执行之后默认参数的内容已经改变
# print(add_end())
# print(add_end())
# print('--------------------------')
# print(add_end1())
# print(add_end1())
# print(add_end1())

# num=[4,5,6]
# print(num)

# print(cal())
# print(cal(1,2,3))
# print(cal(*num))

# ex = {'city':'BeiJing','job':'A'}
# person('zhangsan',23, **ex)

# person1('zhangsan',24,city='ShangHai',job='B')
# person1('lisi',25,city='HangZhou',job='C')
#
# person2('wangwu',26,[1,2,3],city='d',job='e')

# person3('zhaoliu',27,job='f')
# person3('xxx',28,city='NanJing',job='w')


a=(1,2,3)
b={'c':4,'d':5}
person2(*a,**b)