"""
	作者：王小糖
	功能：BMR计算器
	版本：2.0（1.0太简单了，不写了）
	日期：28/12/2018
    新增功能：用户交互
"""


def main():
	"""
	主函数
	"""
	y_or_n=input("是否退出程序（y/n）?")
	while y_or_n=='n':
		gender=input("性别：")
		print(type(gender))
		weight=float(input("体重（kg）："))
		height=float(input("身高（cm）："))
		age=int(input("年龄："))
		if gender=="男":
			BMR=(13.7 * weight)+(5*height)-(6.8*age)+66
		elif gender=="女":
			BMR=(9.6*weight)+(1.8*height)-(4.7*age)+655
		else:
			BMR=-1

		if BMR != -1:
			print("基础代谢率(大卡)为：",BMR)
		else:
			print("暂不支持该性别！")

		print('***********************************')
		y_or_n = input("是否退出程序（y/n）?")
	print("程序退出!")


if __name__=='__main__':
	main()
