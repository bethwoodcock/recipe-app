# imports
import tkinter
import requests

APP_ID = "18002c98"
API_KEY = "46c5a4350bb1b9adaa4e67d27f703c01"

# inistialise a window
root = tkinter.Tk()

# title
root.title('Recipe App')

def get_recipe():
    print()
    command = ''
    while command.lower() != 'q':
        print("1) Find New Recipe")
        print("2) Search Saved Recipes")
        command = input("\t>> ")
        print()
        if command == '1':
            query_recipes()
        elif command == '2':
            search_my_recipes()



#ingredient entry
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Type Ingredient Here')

type.StringVar()
user = Entry(root, textvariable=type, width=32,fg="black", border=1,bg="white",font=('Arial',12,'bold',))
user.place(x=38, y=300)
user.insert(0,'Type Ingredient Here')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

#Lets Eat Button


eat = Button(width=41,pady=7,text='Lets Eat!',bg='#00B3F0',fg='white', border=0,cursor='hand2', command=lambda: query_recipes(textbox.get())).place(x=38, y=400)

#Info Frame
display = Text(root)
display.place(x=38, y=450, relwidth=0.78,relheight=0.3)

# mainloop
root.mainloop()