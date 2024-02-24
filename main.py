from tkinter import *
from random import randint, choice, shuffle
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', "-"]

    password_letters = [choice(letters) for number in range(randint(8, 10))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]
    password_symbols = [choice(symbols) for number in range(randint(2, 4))]
    password_list =password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website= website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "Email": email,
            "Password": password,
        }
    }
    if len(website) ==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Error", message="Your entries cannot be empty.")
    else:
        try: #runs always
            with open("dataentered.json", "r") as datafile:
             data = json.load(datafile)
        except FileNotFoundError: #runs when try fails(as no file is found)
           with open("dataentered.json", "w") as datafile:
               json.dump(new_data, datafile, indent=4)
        else: #runs when except error donot occur
           data.update(new_data)
           with open("dataentered.json", "w") as datafile:
                json.dump(data, datafile, indent=4)
        finally:      #runs always
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("dataentered.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No file found.")
    else:
        if website in data:
            email = data[website]['Email']
            password = data[website]['Password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No information about '{website}' exists.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(background="white")
window.title("Password Manager")
canvas = Canvas()
canvas.config(width=200, height=200, background="white", highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)
window.config(padx= 50, pady=60)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

website_entry = Entry(width=32, highlightthickness=2)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=51, highlightthickness=2)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "@gmail.com")

password_entry = Entry(width=32, highlightthickness=2)
password_entry.grid(row=3, column=1)

password_generator = Button(text= "Generate Password", command=generate_password)
password_generator.grid(row=3, column=2)

add_buttom = Button(text= "Add", width=43, command=save)
add_buttom.grid(row=4, column=1, columnspan=2)

search_button = Button(text= "Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
