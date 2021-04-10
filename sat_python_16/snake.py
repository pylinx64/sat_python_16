import turtle
import time

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
snake_segment.color('#FF00F7')
# добавляет в список голову
snake.append(snake_segment)
#--------------------змея------------------------------------

#--------------------управление------------------------------
screen.onkeypress(lambda: snake[0].setheading(180), 'Left')
screen.listen()
#--------------------управление------------------------------

while True:
    # заставляет двигаться вперед
	snake[0].forward(50)
	
	# обновление экрана
	screen.update()
	
	# управление fps (40 кадров)
	time.sleep(0.01)
