"""
	作者：王小糖
	功能：52周存钱挑战
	版本：2.0
	日期：29/12/2018
	新增功能：记录金额,list列表介绍,math库
"""

import math

def main():
	money_per_week=10 #每周存入的金额
	i=1               #周计数
	increase_money=10 #递增的金额
	total_week=52     #周数
	account_money=0   #账户初始
	money_lsit=[]     #记录每周存款数的列表
	while i <= total_week:

		money_lsit.append(money_per_week)
		account_money=math.fsum(money_lsit)

		print("第{}周存入{}元，账户金额为：{}元".format(i,money_per_week, account_money))
		money_per_week +=increase_money
		i +=1
	print("一年得任务完成啦")

if __name__=="__main__":
	main()