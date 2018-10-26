def vocal2X(strText):
	#Daftar huruf vokal
	vowel='aiueo'
	#Konversi string menjadi list agar dapat dimanipulasi
	ans=list(strText)
	for i in range(len(ans)):
		#Jika karakter yang dicek adalah huruf
		if ans[i].lower() in vowel:
			#Ubah karakter tersebut menjadi 'x'
			ans[i]='x'
	#Menggabungkan list menjadi satu string
	return ''.join(ans)
#Driver program
print(vocal2X('Semangat'))

