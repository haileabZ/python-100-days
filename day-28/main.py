





# Counter app

import math
from tkinter import *
import time
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reseter():
    window.after_cancel(timer)
    canvas.itemconfig(time_holder,text="00:00")
    timer_label.config(text="Timer")
    thick_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break!", fg=RED, font=(FONT_NAME, 30, "bold"))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break!", fg=PINK, font=(FONT_NAME, 30, "bold"))
    else:
        count_down(work_sec)
        timer_label.config(text="Work!", fg=GREEN, font=(FONT_NAME, 30, "bold"))



# ---------------------------- COUNTDOWN MECHANISM --------------------------------- #

def count_down(count):
      global timer
      minute = floor(count/60)
      second = count % 60
      if second < 10 :
          second = f"0{second}"

      canvas.itemconfig(time_holder,text=f"{minute}:{second}")
      if count > 0:
          timer = window.after(1000,count_down,count-1)
      else:
          start()
          mark = ""
          for _ in range(floor(reps/2)):
              mark += "✔"
          thick_mark.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodaro")
window.config(padx=100, pady=100, bg=YELLOW)

timer_label = Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
time_holder = canvas.create_text(110, 130, text="00:00",fill="white", font=(FONT_NAME, 30, "bold"))


start_btn = Button(text="start", command=start)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", command=reseter)
reset_btn.grid(column=2, row=2)

thick_mark = Label(fg=GREEN,bg=YELLOW, font=(FONT_NAME,12, "bold"))
thick_mark.grid(column=1, row=3)


window.mainloop()


