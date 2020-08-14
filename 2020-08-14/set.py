# s1=set([1,2,3])
# print(s1)
# s2=set([4,5,[6,7,8]])  #set中key必须是不可变对象
# print(s2)
# s3=set([4,5,(6,7,8)])
# print(len(s3)) # 3
# print(s3)

# s4=set([(1,2,3)])
# print(len(s4))
# print(s4)
# s5=set([(1,[2,3])]) #即使tuple是不可变的，但其内部可变也无法确定hash值
# print(s5)

# l1=[(1,[2,3])]
# print(len(l1))#长度是1
# print(l1)
# s6=set(l1) # TODO 设置set里存放一个tuple对象，他本身是不可变的，这种的如何确定hash值
# print(len(s6))


# {}和set()两种创建方式的比较
s7={}
print(len(s7))
print(s7)
s8=set()
print(len(s8))
print(s8)

s9={1,2,4,5,'ads'}
print(len(s9))
print(s9)


