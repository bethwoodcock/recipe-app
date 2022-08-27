import re
import tkinter as tk
from tkinter import Tk, StringVar, Entry, Button, Text

import requests

API_URL = "https://pokeapi.co/api/v2/pokemon-species/"


def on_enter(e):
    pokemon_input.delete(0, 'end')


def on_leave(e):
    name = pokemon_input.get()
    if name == '':
        pokemon_input.insert(0, 'Choose your Pokémon')


def search_pokemon(name: str):
    json_response = requests.get(f"{API_URL}{name}").json()
    flavor_text = json_response["flavor_text_entries"][0]["flavor_text"]
    flavor_text = re.sub(r"[\n\s]", " ", flavor_text)
    return flavor_text


def get_description():
    flavor_text = search_pokemon(pokemon_input.get().lower())
    display.delete(1.0, tk.END)
    display.insert(tk.END, flavor_text)


# window
root = Tk()
root.title('Recipe App')
root.geometry('375x667')
root.configure(bg="#FFCD29")
root.resizable(False, False)

pokemon = StringVar()
pokemon_input = Entry(root, textvariable=pokemon, width=32, fg="black", border=1, bg="white",
                      font=('Arial', 12, 'bold',))
pokemon_input.place(x=38, y=300)
pokemon_input.insert(0, 'Choose your Pokémon')
pokemon_input.bind('<FocusIn>', on_enter)
pokemon_input.bind('<FocusOut>', on_leave)

# Search button
search_button = Button(width=41, pady=7, text='Search Pokémon', bg='#00B3F0', fg='white', border=0, cursor='hand2',
                       command=get_description)
search_button.place(x=38, y=400)

# Info Frame
display = Text(root)
display.place(x=38, y=450, relwidth=0.78, relheight=0.3)

# run
root.mainloop()