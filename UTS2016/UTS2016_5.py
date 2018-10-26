def string_match(str1,str2):
	#Set counter ke 0
	ans=0
	#Looping dua lapis untuk mengecek substring str1 dengan str2 
	for i in range(len(str1)-1):
		for j in range(len(str2)-1):
			#Jika ada substring yang sama, counter bertambah
			if(str1[i:i+2]==str2[j:j+2]):
				ans+=1
				
	#Mengembalikan nilai counter
	return ans
#Driver program
print(string_match('xxcaaz','xxbaaz'))