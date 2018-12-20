'''Fungsi mencari nilai minimum dengan rekursi'''
def smallest(lst,min_val=None):
	#Jika list hanya mengandung 1 elemen, maka cukup keluarkan elemen yang ada  (Base case 1)
		return lst[0]
	#Jika belum dilakukan pengecekan, maka inisiasi nilai minimum sebagai nilai awal dari elemen lst
	if min_val==None:
		min_val=lst[0]
		return smallest(lst[1:],min_val)
	#Pengecekan final (Base case 2)
	elif len(lst)==1:
		if(lst[0] < min_val):
			min_val=lst[0]
		return min_val
	#Pengecekan, apabila terdapat nilai dari elemen lst yang lebih kecil dari nilai min sementara, maka nilai minimum sementara adalah nilai yang sedang dicek tersebut
	else:
		if(lst[0] < min_val):
			min_val=lst[0]
		return smallest(lst[1:],min_val)

'''Fungsi mencari maksimum dengan rekursi'''
def biggest(lst,max_val=None):
	#Jika list hanya mengandung 1 elemen, maka cukup keluarkan elemen yang ada  (Base case 1)
	if len(lst)==1 and max_val==None:
		return lst[0]
	#Jika belum dilakukan pengecekan, maka inisiasi nilai maksimum sebagai nilai awal dari elemen lst
	if max_val==None:
		max_val=lst[0]
		return biggest(lst[1:],max_val)
	#Pengecekan final (Base case 2)
	elif len(lst)==1:
		if(lst[0] > max_val):
			max_val=lst[0]
		return max_val
	#Pengecekan, apabila terdapat nilai dari elemen lst yang lebih besar dari nilai max sementara, maka nilai maksimum sementara adalah nilai yang sedang dicek tersebut
	else:
		if(lst[0] > max_val):
			max_val=lst[0]
		return biggest(lst[1:],max_val)
'''Driver program'''
print('Smallest:{}\nBiggest:{}'.format(smallest([-1,2,3,4,-5,-8]),biggest([-1,2,3,4,-5,-8])))
print('\n')
print('Smallest:{}\nBiggest:{}'.format(smallest(['haha','hehe','hihi']),biggest(['haha','hehe','hihi'])))
