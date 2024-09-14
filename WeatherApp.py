import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image,ImageTk
import ttkbootstrap

def get_weather(city):
    API_key ="32e39786cf0534a500018a5da36cb943"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found") 
        return None

def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return 

root = ttkbootstrap.window(themname="morph")
root.title("Weather App")
root.geometry("400x400")

city_entry =ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)

search_button =ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

location_label = tk.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)

icon_label =tk.Label(root)
icon_label.pack()

temperature_label =tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

description_label =tk.Label(root, font="Helvetica, 20")
description_label.pack()

root.mainloop()
