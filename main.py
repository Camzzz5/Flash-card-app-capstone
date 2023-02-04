BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *

window = Tk()
window.title("Flashy")
canvas = Canvas(height=526, width=800)
logo_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=logo_image)
canvas.create_text(400, 150, text="title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)



#Buttons
my_image_x = PhotoImage(file="./images/wrong.png")
button_x = Button(image=my_image_x, highlightthickness=0)
button_x.grid(row=1, column=0)
my_image_y = PhotoImage(file="./images/right.png")
button_y = Button(image=my_image_y, highlightthickness=0)
button_y.grid(row=1, column=1)
window.mainloop()