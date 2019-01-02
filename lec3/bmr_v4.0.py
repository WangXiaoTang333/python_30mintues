"""
	作者：王小糖
	功能：BMR计算器
	版本：4.0
	日期：29/12/2018
    新增功能：用户交互
    新增功能:用户可以在一行输入所有信息；带单位的信息输出
    新增功能：异常处理，函数调用
"""


def BMR_process():

		input_str = input("请输入您的信息：")
		try:
			get_str = input_str.split(" ")
			gender = get_str[0]
			weight = float(get_str[1])
			height = float(get_str[2])
			age = int(get_str[3])
			if gender == "男":
				BMR = (13.7 * weight) + (5 * height) - (6.8 * age) + 66
			elif gender == "女":
				BMR = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
			else:
				BMR = -1

			if BMR != -1:
				print("您的性别为{},体重为{}kg,身高为{}cm,年龄为{}".format(gender, weight, height, age))
				print("基础代谢率为{}大卡：".format(BMR))
			else:
				print("暂不支持该性别！")

		except ValueError:
			print("您输入了不正常的信息！")
		except:
			print("程序异常")


def main():
	"""
	主函数
	"""
	y_or_n=input("是否退出程序（y/n）?")
	while y_or_n=='n':
		print("请您依次输入性别，体重（kg）,身高（cm），年龄，并用空格分割")
		# 函数调用
		BMR_process()
		print('***********************************')
		y_or_n = input("是否退出程序（y/n）?")
	print("程序退出!")


if __name__=='__main__':
	main()
