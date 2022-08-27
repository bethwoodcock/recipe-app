import re
import tkinter as tk
from tkinter import Tk, StringVar, Entry, Button, Text
import requests

APP_ID = "18002c98"
API_KEY = "46c5a4350bb1b9adaa4e67d27f703c01"
API_URL = f'https://api.edamam.com/search?/app_id=${APP_ID}&app_key=${API_KEY}'


def on_enter(e):
    recipe_input.delete(0, 'end')


def on_leave(e):
    name = recipe_input.get()
    if name == '':
        recipe_input.insert(0, 'Enter Your Ingredient')


def search_recipe(recipe_input: str):
    result = requests.get(f'https://api.edamam.com/search?q={recipe_input}&app_id={APP_ID}&app_key={API_KEY}').json()
    flavor_text = result['hits'][0]['recipe']['label']
    flavor_text = re.sub(r"[\n\s]", " ", flavor_text)
    return flavor_text



#PARSING - what do we have / what do we want? f"   {index})", recipe['recipe']['label']) /
#Start ONE thing , then filter it back

#loop through the data, get each label, each ingredients, 'ingredientLines' - save this to another variable, display this. hits.legnth?
#for recipe in data

def get_description():
    flavor_text = search_recipe(recipe_input.get())
    display.delete(1.0, tk.END)
    display.insert(tk.END, flavor_text)


# window
root = Tk()
root.title('Recipe App')
root.geometry('375x667')
root.configure(bg="#FFCD29")
root.resizable(False, False)

recipe = StringVar()
recipe_input = Entry(root, textvariable=recipe, width=32, fg="black", border=1, bg="white",
                      font=('Arial', 12, 'bold',))
recipe_input.place(x=38, y=150)
recipe_input.insert(0, 'Enter an Ingredient')
recipe_input.bind('<FocusIn>', on_enter)
recipe_input.bind('<FocusOut>', on_leave)

# Search button
search_button = Button(width=41, pady=7, text='Search Recipes', bg='#00B3F0', fg='white', border=0, cursor='hand2',
                       command=get_description)
search_button.place(x=38, y=180)

# Info Frame
display = Text(root)
display.place(x=38, y=222, relwidth=0.78, relheight=0.6)

#change4life image
img = tk.PhotoImage(file='logo.png')
tk.Label(root,image=img,bg='#FFCD29').place(x=108,y=20)

# run
root.mainloop()