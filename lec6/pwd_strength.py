"""
作者:王小糖
功能：判断密码强弱
日期：12/01/2019
版本：5.0
2.0新增功能:循环的终止;限制密码的设置次数
3.0新增功能:保存密码及强度到文件中
4.0新增功能:读取文件
5.0新增功能:定义一个password相关的类
"""
class PasswordTool:
	def __init__(self,password):
		self.password=password
		self.strength_level=0

	def check_number_exist(self):
		has_number=False
		for c in self.password:
			if c.isnumeric():
				has_number=True
				break
		return has_number

	def check_letter_exist(self):
		has_letter=False
		for c in self.password:
			if c.isalpha():
				has_letter=True
				break
		return has_letter

	def password_process(self):
		if len(self.password) >= 8:
			self.strength_level += 1
		else:
			print("密码长度至少8位")

		if self.check_number_exist():
			self.strength_level += 1
		else:
			print("密码须包含数字")
		if self.check_letter_exist():
			self.strength_level += 1
		else:
			print("密码须包含字母")




def main():
	try_time=5
	while try_time>0:

		password=input("请输入密码：")
		password_tool=PasswordTool(password)

		password_tool.password_process()

		if password_tool.strength_level==3:
			strength = "强"

		elif password_tool.strength_level == 2:
			strength = "中"

		else:
			strength = "弱"

		f=open("password_3.0.txt","a")
		f.write("密码：{}，强度：{}\n".format(password,strength))
		f.close()


		if password_tool.strength_level==3:
			print("ok")
			break
		else:
			print("请重新检查")
			try_time -= 1


	if try_time <= 0:
		print("尝试次数过多,密码设置失败")

	f = open("password_3.0.txt", 'r')
	content=f.read()
	print(content)
	f.close()


if __name__=="__main__":
	main()