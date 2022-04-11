import json
import tkinter
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    #for char in range(nr_letters):
    #    password_list.append(random.choice(letters))
    #
    #for char in range(nr_symbols):
    #    password_list += random.choice(symbols)
    #
    #for char in range(nr_numbers):
    #    password_list += random.choice(numbers)
    #
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_dara = {
        website: {
            "email": email,
            "password": password,
        }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="ups", message=" u did not filled the fields ")
    #is_ok = messagebox.askokcancel("Information", "zapisac?")
    #if is_ok:
    else:
        try: #witch can fail
            with open("hasla.json", "r") as f:
                #reading old data
                data = json.load(f)
        except FileNotFoundError: #deals with any fail
            with open("hasla.json", "w") as f:
                json.dump(new_dara , f, indent=4)
        else: # if there is no issues
            #reading old data
            data.update(new_dara)
            with open("hasla.json", "w") as f:
                #updating data
                json.dump(data, f, indent=4)
        finally: # runs anyway
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

Window = Tk()  ###
Window.title("password generator ")  ###

Window.config(padx=50, pady=50)  ###

canvas = Canvas(width=200, height=200)  ###
padlock = PhotoImage(file="logo.png")  ###
canvas.create_image(100, 100, image=padlock)  ###
canvas.grid(row=0, column=1)  ###

website_label = Label(text="Website")  ###
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")  ###
email_label.grid(row=2, column=0)
password_label = Label(text="password")  ###
password_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=28)
website_entry.grid(row=1, column=1)
email_entry = Entry(width=42)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "lol@gmail")  # automatycznie wpisuje na poćżatku ten email.
password_entry = Entry(width=28)
password_entry.grid(row=3, column=1)

def find_pass():
    website = website_entry.get()
    try:
        with open("hasla.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(message="this data does not exist")
    else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\n pass{password}")
            else:
                messagebox.showinfo(message=f"no detaild{website}")



# Buttons
find_button = Button(text="search", command=find_pass, width=10)
find_button.grid(row=1, column=2)
generate_button = Button(text="Generate Pass", command=generate_pass)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

Window.mainloop()  ###
