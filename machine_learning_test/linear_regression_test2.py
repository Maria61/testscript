# 简单线性回归（梯度下降法）
import numpy as np
import matplotlib.pyplot as plt

# 1.导入数据
points = np.genfromtxt('data.csv',delimiter=',')
x = points[:,0]
y = points[:,1]
plt.scatter(x,y)