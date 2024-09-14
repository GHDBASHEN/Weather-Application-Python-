import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image,ImageTk
import ttkbootstrap

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

