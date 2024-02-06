


from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = []

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list.extend([choice(numbers) for char in range(randint(2, 4))])
    password_list.extend([choice(symbols) for char in range(randint(2, 4))])

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_value = website_entry.get()
    password_value = password_entry.get()
    email_value = email_entry.get()
    if len(website_value) == 0 or len(password_value) == 0 or email_value == 0:
        messagebox.showerror(title="Error message", message="fill all empty fields")
    else:
        response = messagebox.askokcancel(title=website_value, message=f"do you wanna save\nwebsite: {website_value}\nemail:{email_value}\npassword:{password_value}")
        if response:
            with open("Data.txt", "a") as file:

                file.write(f"{website_value}|{email_value}|{password_value}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                email_entry.delete(0, END)
                

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=20, pady=20)
window.title("Password Generator")

canvas = Canvas(width=200, height=200)
canvas.grid(column=1, row=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
label1 = Label(text="Website")
label1.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

label2 = Label(text="Email\\Username")
label2.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

label3 = Label(text="Password")
label3.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

btn1 = Button(text="Generate Password", width=15, command=generate)
btn1.grid(column=2, row=3)

btn2 = Button(text="Add", width=30, command=save)
btn2.grid(column=1, row=4, columnspan=2)



window.mainloop()



