"""
作者:王小糖
功能：判断密码强弱
日期：12/01/2019
版本：2.0
2.0新增功能:循环的终止;限制密码的设置次数
"""
def check_number_exist(password):
	"""
	判断字符串中是否含有数字
	"""
	has_number=False
	for c in password:
		if c.isnumeric():
			has_number=True
			break
	return has_number


def check_letter_exist(password):
	"""
	判断字符串中是否含有数字
	"""
	has_letter=False
	for c in password:
		if c.isalpha():
			has_letter=True
			break
	return has_letter


def main():

	try_time=5
	while try_time>0:
		password_str=input("请输入密码：")
		# 密码强度
		strength_level=0
		#规则1：密码长度大于8
		if len(password_str)>=8:
			strength_level+=1
		else:
			print("密码长度至少8位")
		# 	规则2：需要包含数字
		if check_number_exist(password_str):
			strength_level+=1
		else:
			print("密码需要包含数字")
		#规则3：需要包含字母
		if check_letter_exist(password_str):
			strength_level+=1
		else:
			print("密码需要包含字母")

		if strength_level==3:
			print("ok")
			break
		else:
			print("请重新检查")
			try_time-=1
		print()
	if try_time<=0:
		print("尝试次数过多,密码设置失败")
if __name__=="__main__":
	main()
