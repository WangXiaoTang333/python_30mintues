"""
	作者：王小糖
	功能：分形树的绘制
	版本：1.0
	日期：28/12/2018
	
"""
import turtle

def draw_branch(branch_length):
	"""
	绘制分形树
	
	"""
	if branch_length >= 5:
		#绘制右侧树枝
		if branch_length < 20:
			turtle.pencolor('green')
		else:
			turtle.pencolor('red')

		turtle.forward(branch_length)
		turtle.right(25)
		draw_branch(branch_length - 10)

		#绘制左侧树枝
		turtle.left(50)
		draw_branch(branch_length - 10)

		if branch_length < 20:
			turtle.color('green')

		else:
			turtle.color('red')

		#返回之前的树枝
		turtle.right(25)
		turtle.backward(branch_length)




def main():
	turtle.left(90)
	turtle.penup()
	turtle.backward(150)
	turtle.pendown()
	turtle.pensize(2)
	# turtle.pencolor('darkgreen')
	draw_branch(100)
	turtle.exitonclick()

if __name__ == '__main__':
	main()