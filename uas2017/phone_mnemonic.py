num={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqr',8:'stu',9:'vwxyz'}
'''Mengecek apakah karakter ada dalam daftar phone mnemonic'''
def check(a,lst):
	#Inisiasi dictionary
	global num
	#Jika tidak ada, kembalikan nilai 0 (Base Case 1)
	if not lst:
		return 0
	#Jika ada, kembalikan nilai angka dari karakter tersebut yang berupa key dari dictionary (Base Case 2)
	if a in num[lst[0]]:
		return str(lst[0])
	#Jika tidak ditemukan, lanjutkan rekursi
	else:
		return check(a,lst[1:])
'''Fungsi ini akan menerjemahkan string berdasarkan phone mnemonic'''
def translate(s):
	#Inisiasi dicitonary
	global num
	#Inisiasi list berisi key
	key=list(num.keys())
	#Jika panjang elemen terdiri 1, keluarkan representasi phone mnemonic dari karakter tersebut (Base Case)
	if len(s)==1:
		ans=check(s.lower(),key)
		if ans != 0:
			return ans
		else:
			return s
	#Kondisi jika panjang elemen list lebih dari 1, mengeluarkan hasil concatenate antara representasi dari karakter yang saat ini sedang dicek dengan hasil rekursi sisa elemen dari list
	if check(s[0].lower(),key)==0:
		return s[0]+conv(s[1:])
	else:
		return check(s[0].lower(),key)+conv(s[1:])
#Program Driver
print(conv('MaI-sakurajima'))