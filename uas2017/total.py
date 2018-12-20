'''Nested list sum using recursion'''
def total(lst):
	#Jika list hanya mempunyai 1 elemen
	if len(lst)==1:
		#Jika elemen berupa angka, maka keluarkan nilai(Base Case) 
		if type(lst[0])==int:
			return lst[0]
		#Jika tidak lakukan rekursi dengan argumen berupa elemen tersebut
		else:
			return total(lst[0])
	#Kondisi jika list mempunyai lebih dari satu elemen
	else:
		#Jika elemen awal berupa angka, maka jumlahkan dengan hasil rekusi elemen selanjutnya
		if type(lst[0])==int:
			return lst[0]+total(lst[1:])
		#Jika elemen awal adalah list, maka jumlahkan hasil rekursi dari kedua list
		else:
			return total(lst[0])+total(lst[1:])
#Program driver
print(total([[3,2],[[4]],[[5,2,1]],2,3,2,[[[1]]]]))