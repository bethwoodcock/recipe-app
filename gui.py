from tkinter import *
from tkinter import messagebox

#window
root = Tk()
root.title('Recipe App')
root.geometry('375x667')
root.configure(bg="#FFCD29")
root.resizable(False,False)

#Eat Click
def Eat():
    window=Toplevel(root)
    window.title("Results")
    window.geometry('375x667')
    window.configure(bg="#FFCD29")
    window.resizable(False, False)

#change4life image
img = PhotoImage(file='logo.png')
Label(root,image=img,bg='#FFCD29').place(x=50,y=50)

#ingredient entry
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Type Ingredient Here')

user = Entry(width=32,fg="black", border=1,bg="white",font=('Arial',12,'bold',))
user.place(x=38, y=300)
user.insert(0,'Type Ingredient Here')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

#Lets Eat Button
eat=Button(width=41,pady=7,text='Lets Eat!',bg='#00B3F0',fg='white',command=Eat,border=0,cursor='hand2').place(x=38, y=400)

#run
root.mainloop()