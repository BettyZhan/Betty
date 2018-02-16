import turtle
import random
import math


'''
to set up outline dartboard
parameter(
'''
def drawSquare(betty, width, top_left_x, top_left_y):
	betty.up()
	betty.goto(top_left_x, top_left_y)
	betty.down()
	for i in range(4):
		betty.forward(width)
		betty.right(90)
  
  
'''
to draw axes
'''  
def drawLine(betty, x_start, y_start, x_end, y_end):
	betty.up()
	betty.goto(x_start, 0)  #?
	betty.down()
	betty.goto(x_end, 0)
	betty.up()
	betty.goto(0, y_start)
	betty.down()
	betty.goto(0, y_end)	

'''
to draw the circle
'''
def drawCircle(betty, radius):
	betty.up()
	betty.goto(0, -1)
	betty.down()
	turtle.circle(radius, 360, 100)
'''
to set up the board using the above functions
'''
def setupDartboard(window, betty):
	window.setworldcoordinates(-4, -4, 4, 4)
	drawSquare(betty, 2, -1, 1)
	drawLine(betty, -2, -2, 2, 2)
	drawCircle(betty, 1) 
	turtle.speed(0)
'''
determine if dot is in circle
'''
def inCircle(betty, circle_center, radius):
	radius = turtle.distance(0, 0)
	if radius<circle_center:		
	
def throwDart(betty):
	betty.up()
	betty.stamp()
	

'''
simulation algorithm returns the approximation of pi
'''
def montePi(turtle, num_darts)










def throwDart(xcor,ycor,turtle,\
	inside,outside):
	turtle.up()
	for i in range(1000):
		xcor = random.uniform(-1.0,1.0)
		ycor = random.uniform(-1.0,1.0)
		turtle.goto(xcor,ycor)
		
		dis = turtle.distance(0,0)
		if dis<1:
			turtle.color("red")
			inside = inside+1
		else:
			turtle.color("green")
			outside = outside+1
		turtle.stamp()
		print(xcor,ycor)
	print(inside,outside)
	
def countprocess(num,inside):
	num = inside/1000 * 4
	print(num)
	
def main():
	betty = turtle.Turtle()
	wn = turtle.Screen()
	setupDartboard(betty,wn)
	x=0
	y=0
	insidecount=0
	outsidecount=0
	throwDart(x,y,betty,insidecount,outsidecount)
	pi=0
	countprocess(pi,insidecount)
	wn.exitonclick()
	
main()
		
'''
 - simulation algorithm returns the approximation of pi
'''	
def montePi(betty, num_darts):
	insideCount = 0
	outsidecCount = 0
	inCircle(darty, 0,  1)
		insideCount = insideCount + 1
	else:
		darty.color("blue")
		outsideCount = outsideCount + 1
		
		
		
		
		
		
'''
determine if dot is in circle
'''
def inCircle(darty, circle_center, radius):
	distance = turtle.distance(circle_center, circle_center)
	if distance<radius:
		darty.color("red")
		
		
		def throwDart(darty):
	darty.up(darty)
	darty.goto(random.uniform(-1.0,1.0), random.uniform(-1.0,1.0))
	darty.stamp()


		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		