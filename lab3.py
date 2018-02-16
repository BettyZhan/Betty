import math
import turtle

def setUpWindow(window):
	
	window.bgcolor("green")
	window.setworldcoordinates(-2*math.pi,-1,math.pi*2,1)
	
def setUpTurtle(turtle):
	
	turtle.goto(0,1)
	turtle.goto(0,-1)
	turtle.goto(0,0)
	turtle.forward(math.pi*2)
	turtle.backward(2*math.pi)
	
def drawCosineCurve(turtle):
	
	for z in range(360,-361,-1):
		x=math.radians(z)
		y=math.cos(math.radians(z))
		print("x= ",x,"cos(x)= ",y)
		turtle.goto(x,y)

def main():
	wn=turtle.Screen()
	setUpWindow(wn)
	point = turtle.Turtle()
	setUpTurtle(point)
	
	for z in range(-360,361,1):
		x=math.radians(z)
		y=math.sin(math.radians(z))
		print("x= ",x,"sin(x)= ",y)
		point.goto(x,y)
		
	drawCosineCurve(point)
		
	wn.exitonclick()
		
	
main()
