import numpy as np
#encoding utf-8
# 13 - Create a 10x10 array with random values and find the minimum and maximum values
# (创建一个10x10的随机数组，并找出最小值和最大值)

arr = np.random.randint(1,100,(10,10))
print("随机数组的最小值为：{}".format(arr.min()))
print("随机数组的最大值为：{}\n".format(arr.max()))

#14 - Create a random vector of size 30 and find the mean value
# (创建一个有30个随机元素的数组并计算其平均值)
arr1 = np.random.random(30)
print("随机数组的平均值为：{}\n".format(arr1.mean()))

#40 - Create a random vector of size 10 and sort it
# (创建一个有10个随机元素的数组并对其排序)
arr2 = np.random.random(10)
print(arr2)
arr2.sort()
print(arr2)
print("\n")

#45 - Create random vector of size 10 and replace the maximum value by 0
# (创建一个有10个随机元素的数组并将最大值修改为0)
arr3 = np.random.random(10)
print(arr3)
arr3[arr3.argmax()] =0
print(arr3)