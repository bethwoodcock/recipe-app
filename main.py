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


def search_recipe(name: str):
    json_response = requests.get(f"{API_URL}").json()
    flavor_text = json_response["flavor_text_entries"][0]["flavor_text"]
    flavor_text = display_recipe_labels(data, index)
    return flavor_text

def display_recipe_labels(data, index):
    """
    Displays all recipe labels from a result of request.
    Returns the max index of list of recipes.
    """
    print()
    for recipe in data:
        index += 1
        print(f"   {index})", recipe['recipe']['label'])
    print()
    return index


def get_description():
    flavor_text = search_recipe(recipe_input.get().lower())
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
recipe_input.place(x=38, y=300)
recipe_input.insert(0, 'Choose your Recipe')
recipe_input.bind('<FocusIn>', on_enter)
recipe_input.bind('<FocusOut>', on_leave)

# Search button
search_button = Button(width=41, pady=7, text='Search Recipes', bg='#00B3F0', fg='white', border=0, cursor='hand2',
                       command=get_description)
search_button.place(x=38, y=400)

# Info Frame
display = Text(root)
display.place(x=38, y=450, relwidth=0.78, relheight=0.3)

# run
root.mainloop()