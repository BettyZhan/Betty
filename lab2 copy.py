import turtle              # 1.  import the modules
import random
import os

def main():
	window = turtle.Screen()       # 2.  Create a screen
	window.bgcolor('lightblue')

	betty = turtle.Turtle()    # 3.  Create two turtles
	kaitlyn = turtle.Turtle()
	betty.color('orange')
	kaitlyn.color('blue')
	betty.shape('turtle')
	kaitlyn.shape('turtle')

	betty.up()          # 4.  Pick up the pen so we don’t get lines
	kaitlyn.up()
	betty.goto(-100,20)
	kaitlyn.goto(-100,-20)
   					  # 5. first race
	betty.forward(random.randrange(1,301))
	kaitlyn.forward(random.randrange(1,301))
	betty.goto(-100,20)	
	kaitlyn.goto(-100,-20)
	
	                   #6. second race
	for i in range(10):
		betty.forward(random.randrange(1,31))
		kaitlyn.forward(random.randrange(1,31))
	
	betty.goto(-100,20)	
	kaitlyn.goto(-100,-20)
	
	                     #Part. 2 
	kaitlyn.ht() 
	betty.home() 
	betty.down()       
	                      #turtle move
	for i in range(3):
			betty.forward(100)
			betty.right(120)
			
	for i in range(4):
			betty.forward(100)
			betty.right(90)
			
	for i in range(5):
			betty.forward(100)
			betty.right(72)
			
	for i in range(6):
			betty.forward(100)
			betty.right(60)
	betty.up()
	betty.goto(-100,20)	
	kaitlyn.goto(-100,-20)
	kaitlyn.st()
    
	window.exitonclick()   
	                     # os model
	os.system("man man")
	os.system("man pwd")
	os.system("man mkdir")
	os.system("man rm")
	os.system("man cd")
	os.system("man ls")
	os.system("man mv")
	os.system("man cp")
	os.system("man python3")                
                       
    
main()