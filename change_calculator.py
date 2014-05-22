def coins():
	'''Return the amount of change a person should give to a customer based on
	the price of the item and currency given by the customer as inputted by the user.'''
	r = 1
	while r == 1:
		cost = input("What does the item cost? ")
		tend = input("How much did the customer give you? ")
		change = (float(tend) - float(cost))
		change = int(change*100)
		dollars = int(change / 100)
		quarters = int(((change - (dollars*100))/25))
		dimes = int(((change - (dollars*100) - (quarters*25))/10))
		nickels = int(((change - (dollars*100) - (quarters*25) - (dimes*10))/5))
		pennies = int((change - (dollars*100) - (quarters*25) - (dimes*10) - (nickels*5)))
		print("Give the customer {0} dollars, {1} quarters, {2} dimes, {3} nickels, and {4} pennies".format(str(dollars),str(quarters),str(dimes),str(nickels),str(pennies)))
		again = input("Do you want to calculate another? y/n ")
		if 'n' in again:
			return r == 0



