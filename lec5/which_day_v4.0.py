"""
	作者：王小糖
	版本：4.0
	日期：04/01/2019
	功能：输入某年某月某日，判断是第几天
	新增功能:用列表替换元组
	新增功能：用月份划分为不同的集合来操作
	新增功能：将月份及对应天数通过字典表示
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

	# # month_day_dict={1:31,
	# 				2:28,
	# 				3:31,
	# 				4:30,
	# 				5:31,
	# 				6:30,
	# 				7:31,
	# 				8:31,
	# 				9:30,
	# 				10:31,
	# 				11:30,
	# 				12:31}

	day_month_set={31:[1,3,5,7,8,10,12],30:[4,6,9,11],28:[2]}

	days=0
	for i in range(1,month):
		if i in day_month_set[31]:
			days =days+ 31
		if i in day_month_set[30]:
			days =days+30
		if i in day_month_set[28]:
			days =days+ 28
		# days += month_day_dict(i)

	if is_leap_year(year) and month >2 :
		days=days+1

	days=days+day

	print("这是{}年第{}天".format(year,days))

if __name__=="__main__":
	main()