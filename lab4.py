
'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(turtle, width, top_left_x, top_left_y) - to outline dartboard
  drawLine(turtle, x_start, y_start, x_end, y_end) - to draw axes
  drawCircle(turtle, radius) - to draw the circle
  setUpDartboard(screen, turtle) - to set up the board using the above functions
  inCircle(turtle, circle_center, radius) - determine if dot is in circle
  throwDart(turtle)
  montePi(turtle, num_darts) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

# List constants here (NO MAGIC NUMBERS!):
BATCH_OF_DARTS = 5000
BOARD_WIDTH = 2
RIGHT_ANGLE = 90

#########################################################
#                   Your Code Goes Below                #
#########################################################


def drawSquare(tur, width, top_left_x, top_left_y):
	'''
	to set up outline dartboard
	param list: tur - a Turtle object
		    	width - an integer or a float >= 0 (if given)
		    	top_left_x - a interger or a float >= 0 (if given)
		    	top_left_y - a interger or a float >= 0 (if given)
	return: None
	'''
	tur.up()
	tur.goto(top_left_x, top_left_y)
	tur.down()
	
	for i in range(4):
		tur.forward(width)
		tur.right(90)
 
   
def drawLine(tur, x_start, y_start, x_end, y_end):
	'''
	to draw axes
	param list: tur - a Turtle object
		    	x_start - an integer or a float >= 0 (if given)
		    	y_start - a interger or a float >= 0 (if given)
		    	x_end - a interger or a float >= 0 (if given)
		    	y_end - a interger or a float >= 0 (if given)
	return: None
	'''
	tur.up()
	tur.goto(x_start, 0)  #?
	tur.down()
	tur.goto(x_end, 0)
	tur.up()
	tur.goto(0, y_start)
	tur.down()
	tur.goto(0, y_end)	
	
	
def drawCircle(tur, radius):
	'''
	to draw the circle
	param list: tur - a Turtle object
		    	radius - an integer or a float >= 0 (if given)
	return: None
	'''
	tur.up()
	tur.goto(0, -1)
	tur.down()
	tur.circle(radius, 360, 100)


def setUpDartboard(win, tur):
	'''
	to set up the board using the above functions
	param list: window - a Screen object
		    	tur - a Turtle object
	return: None
	'''
	win.setworldcoordinates(-4, -4, 4, 4)
	drawSquare(tur, 2, -1, 1)
	drawLine(tur, -2, -2, 2, 2)
	drawCircle(tur, 1) 


def throwDart(tur):
	'''
	to throw darts on the Dartboard
	param list: tur - a Turtle object
	return: None
	'''	
	tur.shape("circle")
	tur.shapesize(0.3, 0.3, 0.3)
	tur.up()
	tur.goto(random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0))
	tur.stamp()
	

def inCircle(tur, circle_center, radius):
	'''
	determine if dot is in circle
	param list: tur - a Turtle object
				circle_center - a integer or a float
				radius - a integer or a float >= 0 (if given)
	return: Ture
	'''
	distance = tur.distance(circle_center, circle_center)
	if distance <= radius:
		return True
		

def montePi(number_darts, tur):  
	'''
	simulation algorithm returns the approximation of pi
	param list: number_darts - a integer >= 0 (if given)
 			 	tur - a Turtle object
	return: approx_pi
	'''	 
	tur.ht()				
	tur.clearstamps()
	
	insideCount = 0	
	for i in range(number_darts):
		tur.up()
		tur.goto(random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0))
		if inCircle(tur, 0, 1) is True:
			tur.color("red")
			insideCount = insideCount+ 1
		else:
			tur.color("blue")
		tur.stamp()	
		
	approx_pi = insideCount/number_darts * 4
	return approx_pi


def playDarts(tur):
	'''
	This is a game of 2 players
	param list: tur - a Turtle object
	return: None
	'''
	tur.ht()
	tur.clearstamps()

	player1 = 0
	player2 = 0
	for i in range(10):					
		tur.color("yellow")
		throwDart(tur)            
		if inCircle(tur, 0, 1) is True:
			player1 = player1 + 1		
		tur.color("green")
		throwDart(tur)			
		if inCircle(tur, 0, 1) is True:
			player2 = player2 + 1	
			
	if player1 > player2:
		print("Player 1 won!")
	elif player1 < player2:
		print("Player 2 won!")
	else:
		print("There was a tie.")


#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)

    print("\tPart A Complete...")
    print("=========== Part B ===========")
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(number_darts, darty)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    # Don't hide or mess with window while it's 'working'
    #tur.clearstamps()
    playDarts(darty)
    window.exitonclick()

main()