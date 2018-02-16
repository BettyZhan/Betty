import turtle


#seq3np1 function keeps track of and returns the count (3 points)
def seq3np1(n):
    """ 
    Print the 3n+1 sequence from n, terminating when it reaches 1.
    param list: n - an integer >= 0 (if given)
    result: count
    """
    count = 0 
    while(n != 1):
        count += 1
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    return count                  # the last print is 1


# Has a drawing function that takes the number of iterations as a parameter (3 points)
def drawing(tur1, tur2, win, times):
	"""
	Graph the number of iterations and print max_so_far in the graph.
	param list: tur1 - a Turtle object
				tur2 - a Turtle object
				win - a Screen object
				times - an interger (the number of iterations)
	return: None
	"""
	max_so_far = 0
	for start in range(1, times):	# uses the range (inclusively) (1 point)
		result = seq3np1(start)
		print("the value of start:", start, "the number of iterations: ",result)
		
		# Print max_so_far in the graph (2 points)
		if result > max_so_far:
			max_so_far = result
			tur2.clear()
			tur2.up()
			tur2.goto(0, max_so_far) 
			tur2.write("iteration: " + str(start) + " " + "max so far: " + str(max_so_far), font = ("Arial",20))
		
		# Graph the results and update the world coordinates(3 points)
		win.setworldcoordinates(0, 0, start + 10, max_so_far + 10)
		tur1.up()
		tur1.goto(start, 0)
		tur1.down()
		tur1.goto(start, result) 
	
	
def main():
	window = turtle.Screen()
	darty = turtle.Turtle()
	betty = turtle.Turtle()
	window.setworldcoordinates(0, 0, 10, 10)
	
	# asks user for an upper bound for the range value (1 point)
	upper_bound = int(input("please enter a number: "))
	drawing(darty, betty, window, upper_bound + 1)
	
	window.exitonclick()
		
main()








































