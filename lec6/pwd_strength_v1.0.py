"""
作者:王小糖
功能：判断密码强弱
日期：12/01/2019
版本：1.0
"""
def check_number_exist(password):
	"""
	判断字符串中是否含有数字
	"""
	for c in password:
		if c.isnumeric():
			return True
	return False


def check_letter_exist(password):
	"""
	判断字符串中是否含有数字
	"""
	for c in password:
		if c.isalpha():
			return True
	return False


def main():
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
	else:
		print("请重新检查")
if __name__=="__main__":
	main()
