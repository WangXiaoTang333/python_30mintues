"""
	作者:王小糖
	功能:模拟掷骰子,记录每次点数的次数
	版本：3.0
	日期：16/1/2019
	2.0新增功能:掷两个骰子,记录结果
	3.0新增功能：可视化两个骰子的结果,也就是要绘制出每次投掷的次数
	matplotlib模块，是一个数据可视化函数库，子模块pyplot提供了2D图表制作的基本函数
	4.0新增功能：画直方图，显示频率
"""

import random

import matplotlib.pyplot as plt
#解决中文显示问题
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
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
	total_times=10000
	# 初始化列表[0,0,0,0,0,0]
	ID_list=list(range(2,13))
	result_list = [0]*11
	result_dict = dict(zip(ID_list,result_list))
	# 记录第一个骰子的结果
	number_list = []


	for i in range(total_times):
		number1 = roll_dice()
		number2 = roll_dice()
		result = number1+number2
		number_list.append(result)

	# 数据可视化


	plt.hist(number_list,bins=range(2,14),normed=1,edgecolor="black",linewidth=1)
	plt.title("骰子点数统计")
	plt.xlabel("点数")
	plt.ylabel("频率")
	plt.show()
if __name__=="__main__":
	main()
