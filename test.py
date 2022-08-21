# imports
import tkinter
import requests
APP_ID = "18002c98"
API_KEY = "46c5a4350bb1b9adaa4e67d27f703c01"
URL = f'https://api.edamam.com/search?/app_id=${APP_ID}&app_key=${API_KEY}&q={city}'

# inistialise a window
root = tkinter.Tk()

# title
root.title('Recipe')

# geometry
# root.geometry('365x100')

def get_city_weather():
    try:
        city = my_city.get()
        api_call = f'https://api.edamam.com/search?/app_id=${APP_ID}&app_key=${API_KEY}&q={city}'
        data = make_request(get_url_q(my_city))
        data = data['hits']
        display.delete('1.0',tkinter.END)
        display.insert('1.0',my_weather)
    except KeyError:
        message = 'PLease enter a valid food name'
        display.delete('1.0',tkinter.END)
        display.insert('1.0',message)

def make_request(url):
    """
    Returns a request response from a given URL.
    """
    response = requests.get(url)
    data = response.json()
    return data

def get_url_q(my_city, _from=0, to=20):
    url = URL + f'&q=${my_city}&to={to}&from={_from}'
    return url

def get_url_r(uri):
    return URL + f'&r={uri}'

# label
city_label = tkinter.Label(root, text='City Name')
city_label.grid(row=0,column=0)

# entry
my_city=tkinter.StringVar()
city_entry = tkinter.Entry(root, textvariable=my_city)
city_entry.grid(row=0, column=1)

# button
my_button = tkinter.Button(root, text='Submit', command=get_city_weather)
my_button.grid(row=0, column=2)

# display
display = tkinter.Text(root, height=4, width=45)
display.grid(row=1,column=0, columnspan=3)

# mainloop
root.mainloop()