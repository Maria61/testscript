from collections import Iterable
# TODO:高级特性

 # 切片

# L = ['AAA','BBB','CCC','DDD','EEE']
# print(L[0:3]) # 取L的 下标范围为[0,3）的元素
# print(L[:3]) # 前面的参数是0可以省略
# print(L[3:]) # 后面的参数是最后一个下标也可以省略
# print('--------------------------------------')
# print(L[:-1]) # 参数可以是负数
# print(L[-1:]) #
# print('---------------------------------------')
# print(L[-2:-1]) # 前面的参数一定要小于后面的参数
# print(L[-1:-2]) # 前面的参数大于后面的参数取到的为空
# print(L[-2:])
# print('---------------------------------------')
# print(L[:]) # 原样复制一个list
# print(L[::2]) # 所有元素中每两个取第一个
# print(L[::3]) # 所有元素中每三个取第一个
# print('-----------------l---------------------')
# l=[1,2,3,4,5,6,7,8,9]
# print(l[:5:2]) # 前五个元素里每两个取第一个

# print('ADFSSD'[1:2])
# print('ABCDEFGH'[::3]) # 切片操作同样适用于字符串，每个字符相当于一个元素

# 迭代

list=[1,2,3,4,5]
for l in list:
    print(l)

dict={'a':'A','b':'B','c':'C'}
for key in dict:
    print(key)
for value in dict.values():
    print(value)
for k,v in dict.items():
    print('k:',k,'v:',v)

for s in 'qwerqwrew':
    print(s)

print(isinstance('asdf',Iterable))
print(isinstance(123,Iterable))