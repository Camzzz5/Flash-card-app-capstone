BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random

current_card = {}
try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("./data/french_words.csv")
    df = df.to_dict(orient="records")
else:
    df = df.to_dict(orient="records")
finally:
    df2 = df.copy()



def flip_card():
    canvas.itemconfig(im, image=logo_image2)
    canvas.itemconfig(card_title, fill="white", text="English")
    canvas.itemconfig(card_word, fill="white", text=current_card["English"])


def is_known():
    next_card()
    x = current_card["French"]
    for i in df2:
        if i["French"] == x:
            df2.remove(i)
    print(len(df2))
    new_data_frame = pd.DataFrame(df2)
    new_data_frame.to_csv("./data/words_to_learn.csv", index=0)


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(df)
    x = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=x, fill="black")
    canvas.itemconfig(im, image=logo_image)
    timer = window.after(3000, func=flip_card)


window = Tk()
window.title("Flashy")
canvas = Canvas(height=526, width=800)
logo_image = PhotoImage(file="./images/card_front.png")
logo_image2 = PhotoImage(file="./images/card_back.png")
im = canvas.create_image(400, 263, image=logo_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

timer = window.after(3000, func=flip_card)

canvas.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
my_image_x = PhotoImage(file="./images/wrong.png")
button_x = Button(image=my_image_x, highlightthickness=0, command=next_card)
button_x.grid(row=1, column=0)
my_image_y = PhotoImage(file="./images/right.png")
button_y = Button(image=my_image_y, highlightthickness=0, command=is_known)
button_y.grid(row=1, column=1)

next_card()

window.mainloop()
