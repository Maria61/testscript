# 调用sklearn库实现线性回归
import numpy as np
import matplotlib.pyplot as plt

# 1.导入数据
points = np.genfromtxt('data.csv',delimiter=',')
x = points[:,0]
y = points[:,1]

# 2.定义损失函数
def compute_cost(w,b,points):
    total_cost = 0
    M = len(points)

    # 逐点计算平均损失误差，然后求平均数
    for i in range(M):
        x = points[i,0]
        y = points[i,1]
        total_cost += (y - w * x - b) ** 2
    return total_cost/M

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

x_new = x.reshape(-1,1)
y_new = y.reshape(-1,1)
lr.fit(x_new,y_new)

# 从训练好的模型中提取系数和截距
w = lr.coef_[0][0]
b = lr.intercept_[0]
print('w = ',w)
print('b = ',b)
cost = compute_cost(w, b, points)
print('cost = ',cost)

pred_y = w*x + b #对于每个x的理想值
plt.scatter(x,y)
# plt.show()
plt.plot(x,pred_y,c='r')
plt.show()