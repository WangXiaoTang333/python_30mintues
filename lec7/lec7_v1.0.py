"""
	作者:王小糖
	功能:模拟掷骰子
	版本：1.0
	日期：14/1/2019
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
	result_list=[0]*6

	for i in range(total_times):
		number=roll_dice()
		for j in range(1,7):
			if number==j:
				result_list[j-1] += 1
		# print(number)
	print(result_list)

	for i,result in enumerate(result_list):
		print("点数是{}的次数是{},频率为{}".format(i+1,result,result/total_times))

if __name__=="__main__":
	main()