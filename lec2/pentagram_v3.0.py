"""
	作者：王小糖
	功能：五角星的绘制
	版本：3.0
	日期：28/12/2018
	新增功能：加入循环绘制不同大小的五角星
	新增功能:使用递归
"""
import turtle


def draw_recursive_pentagram(size):
	count = 1
	while count <= 5:
		turtle.forward(size)
		turtle.right(144)
		# count = count + 1
		count += 1
	size += 10
	if size <= 100:# 设置的终止条件
		draw_recursive_pentagram(size)


def main():
	"""
	主函数
	"""
	turtle.penup()
	turtle.backward(200)
	turtle.pendown()
	turtle.pensize(2)
	turtle.pencolor('red')

	size=50
	draw_recursive_pentagram(size)
	turtle.exitonclick()


if __name__ == '__main__':
	main()