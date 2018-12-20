from tkinter import *
def main():
	main=Tk()
	#Menginisiasi string label dan button di tkinter
	labelText = StringVar()
	labelText.set('Mohon bersabar, ini tryout')
	label=Label(main,textvariable=labelText)
	#Jika button diklik, makan nilai label akan berubah
	button=Button(main,text='Sabar',command=lambda : labelText.set("Terima kasih, Anda sabar"))
	label.pack()
	button.pack()
	main.mainloop()
if __name__=='__main__':
	main()
