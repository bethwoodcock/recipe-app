from tkinter import *
from tkinter import messagebox

def hello(e):
    print("Hello")

#window
root = Tk()
root.title('Recipe App')
root.geometry('375x667')
root.configure(bg="#FFCD29")
root.resizable(False,False)

#change4life image
img = PhotoImage(file='logo.png')
Label(root,image=img,bg='#FFCD29').place(x=50,y=50)

#ingredient frame
frame=Frame(root,width=300,height=35,bg="white")
frame.place(x=38, y=300)

#run
root.mainloop()