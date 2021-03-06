import turtle

t=turtle.Pen()
#---------------

colors = ['lime', 'black', 'red', 'green']

while True:
	for color in colors:
		t.pencolor(color)
		t.forward(100)
		t.left(95)
	
#----------------
turtle.done()
