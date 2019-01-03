"""
	作者：王小糖
	版本：3.0
	日期：03/01/2019
	功能：输入某年某月某日，判断是第几天
	新增功能:用列表替换元组
	新增功能：用月份划分为不同的集合来操作
"""
from datetime import datetime
def is_leap_year(year):
	"""
	判断是否是闰年
	"""
	leap_year=False
	if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
		leap_year=True
	return leap_year

def main():
	"""
	主函数
	"""
	input_date_str=input("请输入日期（yyyy/mm/dd）:")
	input_date=datetime.strptime(input_date_str,"%Y/%m/%d")
	# print(input_date)

	year=input_date.year
	month=input_date.month
	day=input_date.day
	# 包含30天和31天的月份集合
	_30_days_month_set={4,6,9,11}
	_31_days_month_set={1,3,5,7,8,10,12}

	days=0
	for i in range(1,month):
		if i in _30_days_month_set:
			days += 30
		if i in _31_days_month_set:
			days += 31
		else:
			days += 28

	if is_leap_year(year) and month >2 :
		days=days+1

	days=days+day

	print("这是{}年第{}天".format(year,days))

if __name__=="__main__":
	main()