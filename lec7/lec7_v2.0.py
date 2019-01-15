"""
	作者:王小糖
	功能:模拟掷骰子,记录每次点数的次数
	版本：2.0
	日期：15/1/2019
	2.0新增功能:掷两个骰子,记录结果
"""

import random

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
	total_times=100000
	# 初始化列表[0,0,0,0,0,0]
	ID_list=list(range(2,13))
	result_list=[0]*11
	result_dict=dict(zip(ID_list,result_list))
	for i in range(total_times):
		number1=roll_dice()
		number2=roll_dice()
		result=number1+number2

		for j in range(2,13):
			if result==j:
				result_dict[j] += 1
		# print(number)
	print(result_dict)

	for i,result in result_dict.items():
		print("点数是{}的次数是{},频率为{}".format(i,result,result/total_times))

if __name__=="__main__":
	main()
