"""
	作者：王小糖
	版本：5.0
	日期：04/01/2019
	功能：输入某年某月某日，判断是第几天
	新增功能:用列表替换元组
	新增功能：用月份划分为不同的集合来操作
	新增功能：将月份及对应天数通过字典表示
	新增功能：一行代码判断是第几天
"""

import time

def main():
	input_days_str=input_date_str = input("请输入日期（yyyy/mm/dd）:")
	input_date = time.strptime(input_date_str, "%Y/%m/%d")
	print(time.strftime("%j",input_date))

if __name__=="__main__":
	main()