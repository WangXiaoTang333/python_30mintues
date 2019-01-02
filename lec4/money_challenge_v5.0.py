"""
	作者：王小糖
	功能：52周存钱挑战
	版本：5.0
	日期：29/12/2018
	新增功能：记录金额,list列表介绍,math库
	新增功能：for循环3.0
	新增功能：封装4.0
	新增功能：根据用户输入的日期，判断是一年中的第几周，然后输出相应的存款金额5.0
"""

import math
import datetime

def main():

	input_str=input("请依次输入存入的金额，每次累加的金额，总共存的周数，用空格键分割：")
	input_data=input("请输入当前日期（yyyy/mm/dd）:")
	now=datetime.datetime.strptime(input_data,format("%Y/%m/%d"))
	week_number=now.isocalendar()[1]
	input_str_s=input_str.split(" ")
	saving_money=float(input_str_s[0])
	increase_money=float(input_str_s[1])
	total_week=int(input_str_s[2])
	account_money=[]
	total_money=[]
	for i in range(total_week):
		account_money.append(saving_money)
		total_money.append(math.fsum(account_money))
		print("第{}周存入{}元，累计存款金额为{}元".format(i+1,account_money[-1],total_money[-1]))
		saving_money=saving_money+increase_money
	print("第{}周的存款金额为{}元".format(week_number,total_money[week_number-1]))

if __name__=="__main__":
	main()
