from tkinter import *
def main():
	main=Tk()
	
	labelText = StringVar()
	labelText.set('Mohon bersabar, ini tryout')
	label=Label(main,textvariable=labelText)
	button=Button(main,text='Sabar',command=lambda : labelText.set("Terima kasih, Anda sabar"))
	label.pack()
	button.pack()
	main.mainloop()
if __name__=='__main__':
	main()