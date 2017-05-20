def fib(n):
	a , b = 0 , 1
	while a < n :
		print(a, end= ' ') # here end means that the output will not be in the next line always 
		a , b = b , a+b
	
fib(2000)  # the fucntion calling must be itended 