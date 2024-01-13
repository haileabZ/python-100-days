
from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
try:
   data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
   original_data = pd.read_csv("data/french_words.csv")
   words_pair = original_data.to_dict(orient="records")
else:
    words_pair = data.to_dict(orient="records")



def flip_card():
    global random_word
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word_text, text=random_word.get("English"))
    canvas.itemconfig(image_background, image=card_back_image)

def next_card():
    global random_word,flip_timer
    window.after_cancel(flip_timer)
    random_word = choice(words_pair)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word_text, text=random_word.get('French'))
    flip_timer = window.after(3000, flip_card)
    canvas.itemconfig(image_background, image=card_front_image)

def is_known():
    words_pair.remove(random_word)
    data = pd.DataFrame(words_pair)
    data.to_csv("data/words_to_learn.csv")
    next_card()


# -----------------------------------UI setup----------------------------------

window = Tk()
window.title("Flash Card")
window.config(pady=10, padx=10, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

image_background = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
title = canvas.create_text(400, 150, text="", font=("Arial", 40))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))




cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card )
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)


next_card()


window.mainloop()
