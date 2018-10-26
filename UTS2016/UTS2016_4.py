def SentencePerRow(filename):
	try:
		#Membaca file input secara keseluruhan
		inpuText=open(filename,'r')
		words=inpuText.read()
		#Membagi menjadi beberapa kalimat
		sentence=words.split('. ')
		for i in range(len(sentence)):
			#Jika ada titik, tidak perlu print titik lagi
			if('.' in sentence[i]):
				print(str(i+1)+'.', sentence[i])
			#Jika tidak ada titik, print titik
			else:
				print(str(i+1)+'.', sentence[i]+'.')
	#Pesan jika file tidak ada
	except FileNotFoundError:
		print('File tidak ditemukan!')
		exit
SentencePerRow('nomor3.txt')