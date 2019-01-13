"""
作者:王小糖
功能：判断密码强弱
日期：12/01/2019
版本：4.0
2.0新增功能:循环的终止;限制密码的设置次数
3.0新增功能:保存密码及强度到文件中
4.0新增功能:读取文件
"""

def main():
#读取文件

	f=open("password_3.0.txt",'r')
	# content=f.read()
	# print(content)
	lines=f.readlines()
	for line in lines:
		print("read:{}".format(line))
	# print(lines)
	f.close()

if __name__=="__main__":
	main()
