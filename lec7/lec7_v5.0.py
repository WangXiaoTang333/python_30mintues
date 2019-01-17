"""
	作者:王小糖
	功能:模拟掷骰子,记录每次点数的次数
	版本：3.0
	日期：17/1/2019
	2.0新增功能:掷两个骰子,记录结果
	3.0新增功能：可视化两个骰子的结果,也就是要绘制出每次投掷的次数
	matplotlib模块，是一个数据可视化函数库，子模块pyplot提供了2D图表制作的基本函数
	4.0新增功能：画直方图，显示频率
	5.0新增功能:科学计算numpy
"""



import matplotlib.pyplot as plt
import numpy as np
#解决中文显示问题
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False



def main():
	"""
		主函数
	:return:
	"""
	total_times=100000

	roll1_arr=np.random.randint(1,7,size=total_times)
	roll2_arr=np.random.randint(1,7,size=total_times)
	roll3_arr = np.random.randint(1, 7, size=total_times)
	results_arr=roll1_arr+roll2_arr+roll3_arr

	hist,bins=np.histogram(results_arr,bins=range(2,19))
	print(hist)
	print(bins)
	# 数据可视化


	plt.hist(results_arr, bins=range(2, 19), normed=1, edgecolor="black", linewidth=1)
	tick_labels = ["2点", "3点", "4点", "5点", "6点", "7点", "8点", "9点", "10点", "11点", "12点","13","14","15","16","17","18"]
	tick_pos = np.arange(2, 19)+0.5
	plt.xticks(tick_pos,tick_labels)
	plt.title("骰子点数统计")
	plt.xlabel("点数")
	plt.ylabel("频率")
	plt.show()
if __name__=="__main__":
	main()
