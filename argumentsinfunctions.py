#now taking arguments in  functions
def ask_ok(prompt , retries = 4 , reminder="Please try again"): 
	#Defining a functions with arguments and their default values
	ok = input(promt) # taking input from user
	if ok in ('Y' , 'y' , 'yes'):
		return True
	if ok in ('F' , 'f' , 'false'):
		return False
	retries = retries -1 
	if retries < 0:
		raise ValueError('Invalid user response')
	print(reminder)		

	# input(anay)
	ask_ok('anay')	

	# keyword arguments must follow after positional arguments
	# keyword arguments -> those arguments like name=''
	# positional arguments -> those arguments like '' only value is given