import tkinter as tk
import requests
from tkinter import font


HEIGHT = 700
WIDTH = 800

def  test_function(entry):
    print("This is the entry", entry)


def format_response(loc):
    try:

        IP_address = loc['ip']
        country = loc['country_name']
        City_name = loc['city']
        lati = loc['latitude']
        long = loc['longitude']
        flag = loc['country_flag']

        final_str = (IP_address, country, City_name, lati, long, flag)
    except KeyError:
        msg = loc['message']
        final_str =(msg)

    return final_str




def get_location(ip_add):


    location_key ='c61890aacc2b428799cefb295c1aeeb7'
    url = 'https://api.ipgeolocation.io/ipgeo'
    params = {'APPID': location_key, 'apiKey':location_key , 'ip':ip_add}
    response = requests.get(url, params)
    loc=(response.json())


    label['text'] = format_response(loc)







root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH).pack()

background_img = tk.PhotoImage(file='back.png')
background_label=tk.Label(root, image=background_img)
background_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root, bg= '#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame, text="Get Location", bg='gray', font=40, command=lambda:get_location(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame=tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Arial', 10))
label.place(relwidth=1, relheight=1)

tk.font.families()

root.mainloop()
