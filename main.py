from tkinter import *
from PIL import Image, ImageTk
import requests

response = requests.get("https://api.kanye.rest")
response.raise_for_status()
data = response.json()
actual_quote = data["quote"]


def get_quotes():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    actual_quote = data["quote"]
    canvas.itemconfig(quote_text, text=actual_quote)


window = Tk()
window.title("Kanye Quotes")
window.config(padx=50, pady=50)


canvas = Canvas(width=300, height=414)
background_image = PhotoImage(file=r"C:\Users\yusuf\PycharmProjects\Day33\kanye-quotes-start\background.png")
canvas.create_image(150, 207, image=background_image)
quote_text = canvas.create_text(150, 207, text=actual_quote, width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)


image = Image.open("kanye-quotes-start/kanye.png")
kanye_img = ImageTk.PhotoImage(image)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quotes)
kanye_button.grid(row=1, column=0)


window.mainloop()