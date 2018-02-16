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
	betty.forward(random.randrange(1,31))
	kaitlyn.forward(random.randrange(1,31))
	betty.forward(random.randrange(1,31))
	kaitlyn.forward(random.randrange(1,31))
	betty.forward(random.randrange(1,31))
	kaitlyn.forward(random.randrange(1,31))
	betty.forward(random.randrange(1,31))
	kaitlyn.forward(random.randrange(1,31))
	betty.forward(random.randrange(1,31))
	kaitlyn.forward(random.randrange(1,31))
	betty.forward(random.randrange(1,31))
	kaitlyn.forward(random.randrange(1,31))
	betty.forward(random.randrange(1,31))
	kaitlyn.forward(random.randrange(1,31))
	betty.forward(random.randrange(1,31))
	kaitlyn.forward(random.randrange(1,31))
	betty.forward(random.randrange(1,31))
	kaitlyn.forward(random.randrange(1,31))
	betty.forward(random.randrange(1,31))
	kaitlyn.forward(random.randrange(1,31))
	betty.goto(-100,20)	
	kaitlyn.goto(-100,-20)
	
	                     #Part. 2 
	betty.up()
	kaitlyn.ht()         
	betty.goto(-100,-200)
	                      #turtle move
	betty.left(60)
	betty.forward(200)
	betty.right(120)
	betty.forward(200)
	betty.right(120)
	betty.forward(200)
	betty.right(90)
	betty.forward(200)
	betty.right(90)
	betty.forward(200)
	betty.right(90)
	betty.forward(200)
	betty.right(90)
	betty.forward(200)
	betty.right(72)
	betty.forward(200)
	betty.right(72)
	betty.forward(200)
	betty.right(72)
	betty.forward(200)
	betty.right(72)
	betty.forward(200)
	betty.right(72)
	betty.forward(200)
	betty.right(60)
	betty.forward(200)
	betty.right(60)
	betty.forward(200)
	betty.right(60)
	betty.forward(200)
	betty.right(60)
	betty.forward(200)
	betty.right(60)
	betty.forward(200)
	betty.right(60)
	betty.forward(200)
	
	betty.up()
	betty.setheading(0)
	betty.goto(-100,20)
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



