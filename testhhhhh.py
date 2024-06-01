#
import numpy as np

# 对价格表进行遍历，相邻的价格分别为买入卖出，相邻两个，多个价格为买入卖出
# list = {1,2,3,4,5}
#
# for j in range(len(list)):
#     for k in range(5 - j - 1):
#         if(j>k+1):
#             break
#         print(j,k+1,end=' ')
#     print('')

# import numpy as np
# import pandas as pd
#
# # 创建一个包含多维数组的列表
# arr = np.array([[70, 9, 1], [6, 99, 4], [9, 8, 7]])
#
# # 按第一列排序
# sorted_arr = arr[arr[:, 1].argsort()]
#
# # sorted_arr[:,2] = sorted_arr[:,2].astype(float)
# # arr.dtype = 'float-32'
#
# # data[‘second’] = data[‘second’].astype(int)
# arr[1][1] = arr[1][1].astype(float)
#
#
# print("按第一列排序后的数组：")
#
# print(type(arr[1][1]))
# print(type(arr[1][0]))
# print(type(arr[1][2]))
# print(sorted_arr)
# # #[[ 9  8  7]
#  # [70  9  1]
#  # [ 6 99  4]]
#
import numpy as np

a = np.array([0.88518868, 0.4527473  ,0.61944059 ,0.1480421 ])
print(a)
print(a.dtype)

print('\n'+'-'*50+'\n')

a.dtype = 'float32'
print(a)
print(a.dtype)


# import numpy as np
#
# # 创建一个浮点型矩阵
# x = np.array([[1.2, 2.5], [3.4, 4.9]])
#
# # 将矩阵转置后，将每一列的元素转换为整型
# x_int = np.array([x[:, i].astype(int) for i in range(x.shape[1])]).T
#
# print("原矩阵：", x)
# print("转换后矩阵：", x_int)

