from tkinter import *
from random import randint, choice, shuffle
from tkinter import messagebox
import pyperclip

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
    if len(website) ==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Error", message="Your entries cannot be empty.")
    else:
        want_to_save= messagebox.askokcancel(title=website, message=f"Your entries are:\nEmail: {email}\nPassword: {password}\nDo you want to save?")
        if want_to_save:
            with open("data.txt", "a") as datafile:
                datafile.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            
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

website_entry = Entry(width=51, highlightthickness=2)
website_entry.grid(row=1, column=1, columnspan=2)
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

window.mainloop()