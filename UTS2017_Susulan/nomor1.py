def median(lst):
	lst.sort()
	#Jika banyak elemen adalah genap
	if(len(lst)%2==0):
		#Ambil nilai mean dari nilai tengah
		return (lst[len(lst)//2]+lst[(len(lst)//2)-1])/2
	#Jika banyak elemen adalah ganjil
	else:
		#Ambil nilai tengah
		return float(lst[((len(lst)-1)//2)])
#Driver program
print(median([2,1,4]))
print(median([6,1,9,2]))