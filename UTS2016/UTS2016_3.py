def CaesarChiper(text):
	alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	ls=list(text)
	for i in range(len(ls)):
		#Jika karakter yang dicek adalah alfabet
		if ls[i] in alphabet:
			#Geser ke kiri sebanyak 3 langkah dari index abjad yang ingin dicari
			ls[i]=alphabet[(alphabet.find(ls[i])-3)%len(alphabet)] 
	#Menggabungkan beberapa karakter
	return ''.join(ls)
#Driver program
text='THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'
print('Plain:',text)
print('Ciphertext:',CaesarChiper(text))
