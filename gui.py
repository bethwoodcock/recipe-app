from tkinter import *
import requests

# ID set is used to ensure all recipes have unique ID
APP_ID = "18002c98"
API_KEY = "46c5a4350bb1b9adaa4e67d27f703c01"

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
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Type Ingredient Here')

food = StringVar()
user = Entry(root, textvariable=food, width=32,fg="black", border=1,bg="white",font=('Arial',12,'bold',))
user.place(x=38, y=300)
user.insert(0,'Type Ingredient Here')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

def get_recipe():
    response = None
    success = False
    index = 0
    while not success:
        print("Please enter a keyword")
        key_word = input("\t>> ")
        data = make_request(get_url_q(key_word))
        data = data['hits']
        if len(data) > 0:
            success = True
        else:
            print(f'0 results for "{key_word}"')
            input("")
    index = display_recipe_labels(data, index)


    display.delete(1.0, END)
    display.insert(1.0,recipe)

#Lets Eat Button
eat_button = Button(width=41,pady=7,text='Lets Eat!',bg='#00B3F0',fg='white', border=0,cursor='hand2', command=get_recipe)
eat_button.place(x=38, y=400)

#Info Frame
display = Text(root)
display.place(x=38, y=450, relwidth=0.78,relheight=0.3)


#run
root.mainloop()