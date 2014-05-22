'''Print the number, value, and amount of wrapperes needed of pennies, nickels, dimes, and quarters
based on the weight of each coin provided by user.'''

coin_types = [
['pennies',2.5,50,0.01],
['nickels',5.0,40,0.05],
['dimes',2.268,50,0.1],
['quarters',5.67,40,0.25]
]

for coin,weight,roll,worth in coin_types:
	wt = input("What's the weight of your {0} ?".format(coin))
	bgwt = input("Please enter the unit of your coins in 'g' or 'lbs': ")
	if bgwt.lower() == 'lbs':
		wt = float(wt)*453.592

	amount = round(float(wt)/weight)
	wrappers = round(amount/roll)
	total = amount*worth
	print("You have {0} {1}, which is worth ${2}, and it will take {3} wrappers.".format(amount,coin,total,wrappers))
