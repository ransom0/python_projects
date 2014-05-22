

def fibplace():
	nth = int(input("What place in the sequence would you like to know: "))
	x = [1,1]
	for i in range(nth):
		x.append(x[-1]+x[-2])
	x.insert(0,0)
	return x[nth]


