from tkinter import *
from tkinter import messagebox

def hello(e):
    print("Hello")

root = Tk()
root.title('Recipe App')
root.geometry('375x667')
root.configure(bg="#FFCD29")
root.resizable(False,False)
# btn = Button(tk, text = "click me", width = 30, height = 5)
# btn.bind("<Button-1>", hello)
# btn.pack()

img = PhotoImage(file='logo.png')
Label(root,image=img,bg='#FFCD29').place(x=50,y=50)



root.mainloop()