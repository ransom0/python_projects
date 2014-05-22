def mean(numlist):
	'''Return the mean of a list of numbers.'''
	return sum(numlist)/len(numlist)

def median(numlist):
	'''Return the median of a list of numbers.'''
	srt = sorted(numlist)
	if len(numlist) % 2 == 0:
		return (srt[int(len(numlist)-1)] + srt[int(len(numlist)-2)]) / 2.0
	else:
		return srt[int(len(numlist)/2)]

def mode(numlist):
	'''Return the mode of a list of numbers.'''
	counts = {}
	themode = 0
	for i in numlist:
		counts[i] = numlist.count(i)
	return max(counts, key=counts.get)

		
	
	



