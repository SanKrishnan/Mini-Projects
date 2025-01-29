import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
import io

def get_weather():
    city = city_name.get().strip()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    my_api = "35f4e77c137e0108200f1ab75484e567"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_api}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            weather_desc = data["weather"][0]["description"].capitalize()
            code = data["weather"][0]["icon"]

            
            icon_url = f"http://openweathermap.org/img/wn/{code}@2x.png"
            icon_response = requests.get(icon_url)
            icon_image = Image.open(io.BytesIO(icon_response.content))
            icon_image = icon_image.resize((100, 100))
            icon = ImageTk.PhotoImage(icon_image)
            icon_label.config(image=icon)
            icon_label.image = icon

            result_label.config(text=f"{city.upper()}\n{weather_desc}\n🌡 {temp}°C", font=("Comic Sans MS", 16, "bold"))
        else:
            messagebox.showerror("Error", "City not found! Please check the city name.")
    except Exception as e:
        messagebox.showerror("Error", "Failed to retrieve weather data.")

# GUI
root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("500x600")
root.configure(bg="#023047")

style = ttk.Style()
style.configure("TButton", font=("Comic Sans MS", 12), padding=5)

title_label = tk.Label(root, text=" Weather Dashboard", font=("Comic Sans MS", 18, "bold"), bg="#023047", fg="white")
title_label.pack(pady=15)

city_name = ttk.Entry(root, font=("Comic Sans MS", 14), width=20)
city_name.pack(pady=10)

get_weather_btn = ttk.Button(root, text="Get Weather", command=get_weather)
get_weather_btn.pack(pady=10)

icon_label = tk.Label(root, bg="#023047")
icon_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Comic Sans MS", 14), bg="#023047", fg="white")
result_label.pack(pady=20)

root.mainloop()
