# passing a dictonary as a argument 
def cheeseshop(kind , *arguments ,**keywords):
	print("I would like to have " , kind , "?")
	print("Sorry ! OUT OF STOCK OF" , kind )
	for arg in arguments : # *name must occur before **name 
		print(arg)
	print('-'*50)
	for kw in keywords: # its a dictonary that is passed as a argument
		print(kw , ":" , keywords[kw])


cheeseshop('pasta' , "its funny " , "its very funny " , 
			"It really very funy" , shopkeeper="Depak",
			client="anay" , amount="0$")


																	