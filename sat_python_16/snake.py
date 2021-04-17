import turtle
import time
import random

#--------------------экран-----------------------------------
screen = turtle.Screen()
screen.bgcolor('#A3FFF7')
# размер экрана
screen.setup(650, 650)
#--------------------экран-----------------------------------

#--------------------змея------------------------------------
snake = []
snake_segment = turtle.Turtle()
snake_segment.shape('square')
snake_segment.color('#000000')
snake_segment.penup()
# добавляет в список голову
snake.append(snake_segment)
#--------------------змея------------------------------------

#--------------------еда-------------------------------------
food = turtle.Turtle()
food.shape('turtle')
food.color('#008000')
food.penup()
# рандомно телепортирует еду (x, y)
food.goto(random.randint(-300, 300), random.randint(-300, 300))
#--------------------еда-------------------------------------

#--------------------управление------------------------------
screen.onkeypress(lambda: snake[0].setheading(180), 'Left')
screen.onkeypress(lambda: snake[0].setheading(0), 'Right')
screen.onkeypress(lambda: snake[0].setheading(90), 'Up')
screen.onkeypress(lambda: snake[0].setheading(270), 'Down')
screen.listen()
#--------------------управление------------------------------

while True:
	if snake[0].distance(food) < 20:
		# рандомно телепортирует еду (x, y)
		food.goto(random.randint(-300, 300), random.randint(-300, 300))
		snake_segment = turtle.Turtle()
		snake_segment.shape('square')
		snake_segment.color('#00FF00')
		snake_segment.penup()
		# добавляет в список голову
		snake.append(snake_segment)
	
	# передвигает туловище за головой по частям
	for segment in range(len(snake)-1, 0, -1):
		x = snake[segment-1].xcor()
		y = snake[segment-1].ycor()
		snake[segment].goto(x, y)
	
	# заставляет двигаться вперед
	snake[0].forward(20)
	
	# обновление экрана
	screen.update()
	
	# управление fps (40 кадров)
	time.sleep(0.1)
