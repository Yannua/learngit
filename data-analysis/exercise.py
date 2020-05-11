import numpy as np
#给定一个一维数组，将元素值在3至8之间的元素置为其原本的相反数
x = np.arange(10)
x[(x>3)&(x<8)]=-1*x[(x>3)&(x<8)]
print(x)

#How to swap two rows of an array? (如何交换一个数组的两行？) 交换第一行和第三行
y = np.arange(20).reshape(4,5)
y[[0,2]]=y[[2,0]]
print(y)