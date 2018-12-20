def smallest(lst,min_val=None):
	if len(lst)==1 and min_val==None:
		return lst[0]
	if min_val==None:
		min_val=lst[0]
		return smallest(lst[1:],min_val)
	elif len(lst)==1:
		if(lst[0] < min_val):
			min_val=lst[0]
		return min_val
	else:
		if(lst[0] < min_val):
			min_val=lst[0]
		return smallest(lst[1:],min_val)

def biggest(lst,max_val=None):
	if len(lst)==1 and max_val==None:
		return lst[0]
	if max_val==None:
		max_val=lst[0]
		return biggest(lst[1:],max_val)
	elif len(lst)==1:
		if(lst[0] > max_val):
			max_val=lst[0]
		return max_val
	else:
		if(lst[0] > max_val):
			max_val=lst[0]
		return biggest(lst[1:],max_val)
print('Smallest:{}\nBiggest:{}'.format(smallest([-1,2,3,4,-5,-8]),biggest([-1,2,3,4,-5,-8])))
print('\n')
print('Smallest:{}\nBiggest:{}'.format(smallest(['haha','hehe','hihi']),biggest(['haha','hehe','hihi'])))