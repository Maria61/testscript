#简单线性回归（最小二乘法）
import numpy as np
import matplotlib.pyplot as plt

# 1.提取矩阵中的数据为x，y
# 2.定义损失函数
# 3.定义算法拟合函数
# 4.测试
# 5.画拟合曲线图

points = np.genfromtxt('data.csv',delimiter=',')#points可以看作多行两列的矩阵
# print(points)
# print(points[0,1]) #取矩阵的坐标为（0，1）处的值
# print(points[0,0:2])#取矩阵中坐标为（0，0）到（0，1）的所有点的值
# print(points[0,:2])#同上
# print(points[0,:])#同上
# 1.取矩阵中的两列数据
x = points[:,0]#矩阵的第一列数据
y = points[:,1]#矩阵的第二列数据
plt.scatter(x,y)
# plt.show()

# 2.定义损失函数
# 损失函数是系数的函数，需要传入数据
def compute_cost(w,b,points):
    total_cost = 0
    M = len(points)

    # 逐点计算平均损失误差，然后求平均数
    for i in range(M):
        x = points[i,0]
        y = points[i,1]
        total_cost += (y - w * x - b) ** 2
    return total_cost/M

# 3.定义算法拟合函数
# 定义均值函数
def average(data):
    sum = 0
    for i in range(len(data)):
        sum += data[i]
    return sum/len(data)
# 定义核心拟合函数
def fit(points):
    x_bar = average(points[:,0])
    m = len(points)
    sumyx = 0
    sumx2 = 0
    for i in range(m):
        sumyx += points[i,1] * (points[i,0] - x_bar)
        sumx2 += points[i,0]**2
    w = sumyx / (sumx2 - m * (x_bar**2))
    sum_delta = 0
    for i in range(m):
        x = points[i,0]
        y = points[i,1]
        sum_delta += y - w*x
    b = sum_delta / m
    return w,b

# 4.测试
w,b = fit(points)
cost = compute_cost(w,b,points)
print("w = ",w)
print("b = ",b)
print("cost = ",cost)

# 5.画出拟合曲线
pred_y = w*x + b #对于每个x的理想值
plt.plot(x,pred_y,c='r')
plt.show()

