"""
	作者:王小糖
	功能:模拟掷骰子,记录每次点数的次数
	版本：3.0
	日期：16/1/2019
	2.0新增功能:掷两个骰子,记录结果
	3.0新增功能：可视化两个骰子的结果,也就是要绘制出每次投掷的次数
	matplotlib模块，是一个数据可视化函数库，子模块pyplot提供了2D图表制作的基本函数
"""

import random

import matplotlib.pyplot as plt

def roll_dice():
	"""
		模拟掷骰子
	:return:
	"""
	roll=random.randint(1,6)
	return roll


def main():
	"""
		主函数
	:return:
	"""
	total_times=100
	# 初始化列表[0,0,0,0,0,0]
	ID_list=list(range(2,13))
	result_list = [0]*11
	result_dict = dict(zip(ID_list,result_list))
	# 记录第一个骰子的结果
	number1_list = []
	number2_list = []

	for i in range(total_times):
		number1 = roll_dice()
		number2 = roll_dice()
		number1_list.append(number1)
		number2_list.append(number2)
		result = number1+number2

		for j in range(2,13):
			if result==j:
				result_dict[j] += 1
		# print(number)
	print(result_dict)
	# 数据可视化

	for i,result in result_dict.items():
		print("点数是{}的次数是{},频率为{}".format(i,result,result/total_times))
	x=range(1,total_times+1)
	plt.scatter(x, number1_list, alpha=0.5, c="red")
	plt.scatter(x, number2_list, alpha=0.5, c="green")
	plt.show()

if __name__=="__main__":
	main()
