BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random


df = pd.read_csv("./data/french_words.csv")
df = df.to_dict(orient="records")


def next_card():
    x = random.choice(df)
    random_french_word = x["French"]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=random_french_word)





window = Tk()
window.title("Flashy")
canvas = Canvas(height=526, width=800)
logo_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=logo_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
my_image_x = PhotoImage(file="./images/wrong.png")
button_x = Button(image=my_image_x, highlightthickness=0, command=next_card)
button_x.grid(row=1, column=0)
my_image_y = PhotoImage(file="./images/right.png")
button_y = Button(image=my_image_y, highlightthickness=0, command=next_card)
button_y.grid(row=1, column=1)

next_card()









window.mainloop()
