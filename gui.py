from tkinter import *
from tkinter import messagebox

#window
root = Tk()
root.title('Recipe App')
root.geometry('375x667')
root.configure(bg="#FFCD29")
root.resizable(False,False)

#change4life image
img = PhotoImage(file='logo.png')
Label(root,image=img,bg='#FFCD29').place(x=50,y=50)

#ingredient entry
user = Entry(width=32,fg="black", border=2,bg="white",font=('Arial',12,'bold',))
user.place(x=38, y=300)
user.insert(0,'Type Ingredient Here')



#run
root.mainloop()