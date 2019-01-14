"""
作者:王小糖
功能：判断密码强弱
日期：12/01/2019
版本：6.0
2.0新增功能:循环的终止;限制密码的设置次数
3.0新增功能:保存密码及强度到文件中
4.0新增功能:读取文件
5.0新增功能:定义一个password相关的类
6.0新增功能:将文件操作封装到类中
"""
class PasswordTool:
	"""
	#密码工具类
	"""
	def __init__(self,password):
		# 类的属性
		self.password=password
		self.strength_level=0

	# 类的方法
	def check_number_exist(self):
		"""
		判断字符串中是否含有数字
		"""
		has_number = False
		for c in self.password:
			if c.isnumeric():
				has_number = True
				break
		return has_number

	def check_letter_exist(self):
		"""
		判断字符串中是否含有数字
		"""
		has_letter = False
		for c in self.password:
			if c.isalpha():
				has_letter = True
				break
		return has_letter

	def process_password(self):
		# 规则1：密码长度大于8
		if len(self.password) >= 8:
			self.strength_level += 1
		else:
			print("密码长度至少8位")
		# 规则2：需要包含数字
		if self.check_number_exist():
			self.strength_level += 1
		else:
			print("密码需要包含数字")
		# 规则3：需要包含字母
		if self.check_letter_exist():
			self.strength_level += 1
		else:
			print("密码需要包含字母")


class FileTool:

	def __init__(self,filepath):
		self.filepath=filepath

	def write_to_file(self,line):
		f=open(self.filepath,"a")
		f.write(line)
		f.close()

	def read_from_file(self):
		f=open(self.filepath,"r")
		lines=f.readlines()
		f.close()
		return lines


def main():

	#实例化文件工具
	file_path='password_6.0.txt'
	file_tool=FileTool(file_path)

	try_time=5
	while try_time>0:
		password_str=input("请输入密码：")

		# 实例化密码工具对象
		passwor_tool=PasswordTool(password_str)
		passwor_tool.process_password()

		if passwor_tool.strength_level==3:
			strength="强"
		elif passwor_tool.strength_level==2:
			strength="中"
		else:
			strength="弱"

		# 写文件
		line="密码：{}，强度：{}\n".format(password_str,strength)
		file_tool.write_to_file(line)

		if passwor_tool.strength_level==3:
			print("ok")

			break
		else:
			print("请重新检查")
			try_time-=1
		print()

	if try_time<=0:
		print("尝试次数过多,密码设置失败")

	# 读文件
	lines=file_tool.read_from_file()
	print(lines)

if __name__=="__main__":
	main()
