import turtle
import time
text = turtle.textinput('Загловок', 'Введите текст')
t=turtle.Pen()
'''
t.penup()
t.left(45)
t.forward(100)
t.pendown()
t.forward(100)

t.penup()
t.goto(100, 100)
t.pendown()
'''

t.speed(1)
t.shape('turtle')

t.color('black', 'red')
t.begin_fill()
t.goto(0, 0)
t.goto(100, 0)
t.goto(50, 50)
t.goto(0, 0)
t.end_fill()


t.write(text, align='right',font=('Arial Bold', 30))


time.sleep(100)

