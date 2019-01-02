"""
	作者：王小糖
	功能：52周存钱挑战
	版本：3.0/4.0
	日期：29/12/2018
	新增功能：记录金额,list列表介绍,math库
	新增功能：for循环3.0
	新增功能：封装4.0
"""

import math

def save_money_in_n_weeks(money_per_week,increase_money,total_week):
	"""
	计算n周内的存款金额
	"""
	account_money = 0  # 账户初始
	money_lsit = []  # 记录每周存款数的列表
	for i in range(total_week):
		money_lsit.append(money_per_week)
		account_money = math.fsum(money_lsit)
		#print("第{}周存入{}元，账户金额为：{}元".format(i + 1, money_per_week, account_money))
		money_per_week = money_per_week + increase_money
	return account_money

def main():
	input_str=input("请以此输入每周存入的金额，递增的金额，周数，并用空格键分隔:")
	input_str_use=input_str.split(" ")
	money_per_week=float(input_str_use[0]) #每周存入的金额
	increase_money=float(input_str_use[1])  #递增的金额
	total_week=int(input_str_use[2])      #周数
	account_money=0   #账户初始
	account_money=save_money_in_n_weeks(money_per_week,increase_money,total_week)
	print("一年得存款金额为{}元".format(account_money))

if __name__=="__main__":
	main()
