import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap as ttk

def get_weather(city):
    API_key = "32e39786cf0534a500018a5da36cb943"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None

    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)

def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description.capitalize()}")

# Set up the window using ttkbootstrap with a light theme
style = ttk.Style(theme="flatly")  # Choose a light theme (e.g., "flatly", "minty")
root = style.master
root.title("Weather App")
root.geometry("400x500")
root.configure(bg='#E0F7FA')  # Light background color

# City Entry
city_entry = ttk.Entry(root, font=("Helvetica", 18), bootstyle="info")
city_entry.pack(pady=20, padx=10)

# Search Button
search_button = ttk.Button(root, text="Search", command=search, bootstyle="success-outline")
search_button.pack(pady=10)

# Weather Information Labels
location_label = ttk.Label(root, font=("Helvetica", 25), foreground='#00796B', background='#E0F7FA')
location_label.pack(pady=20)

icon_label = ttk.Label(root, background='#E0F7FA')
icon_label.pack(pady=10)

temperature_label = ttk.Label(root, font=("Helvetica", 20), foreground='#00796B', background='#E0F7FA')
temperature_label.pack(pady=5)

description_label = ttk.Label(root, font=("Helvetica", 20), foreground='#00796B', background='#E0F7FA')
description_label.pack(pady=5)

# Run the application
root.mainloop()
