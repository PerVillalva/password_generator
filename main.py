from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    gen_letter = [choice(letters) for _ in range(randint(8, 10))]
    gen_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    gen_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = gen_letter + gen_symbols + gen_number
    shuffle(password_list)

    password = "".join(password_list)
    password_e.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_e.get()
    username = username_e.get()
    password = password_e.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
    }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please, fill in all the fields before adding a new entry.")
    else:
        try:
            with open("my_passwords.json", "r") as file:
                # read the old data
                data = json.load(file)
                # update the old data
                data.update(new_data)
        except FileNotFoundError:
            with open("my_passwords.json", "w") as file:
                # Create a file
                json.dump(new_data, file, indent=4)
        else:
            with open("my_passwords.json", "w") as file:
                # Save updated data
                json.dump(data, file, indent=4)
        finally:
            website_e.delete(0, END)
            password_e.delete(0, END)

# ---------------------------- SEARCH DATA ------------------------------- #


def search():
    info_website = website_e.get()
    try:
        with open("my_passwords.json") as data:
            stored_data = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No datafile found")
    else:
        if info_website in stored_data:
            info_username = stored_data[info_website]["username"]
            info_password = stored_data[info_website]["password"]
            messagebox.showinfo(title=f"{info_website} Username and Password ",
                                message=f"Username: {info_username}\nPassword: {info_password}")
        else:
            messagebox.showinfo(title="Oops", message=f"No details for {info_website} exists.")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(heigh=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels

website_l = Label(text="Website:")
website_l.grid(column=0, row=1)

username_l = Label(text="Email/Username:")
username_l.grid(column=0, row=2)

password_l = Label(text="Password:")
password_l.grid(column=0, row=3)

# Entries

website_e = Entry(width=21)
website_e.focus()
website_e.grid(column=1, row=1, columnspan=2, sticky="EW")

username_e = Entry(width=35)
username_e.insert(END, "username")
username_e.grid(column=1, row=2, columnspan=2, sticky="EW")

password_e = Entry(width=21)
password_e.grid(column=1, row=3, sticky="EW")


# Buttons


add_b = Button(text="Add", width=36, command=save_password)
add_b.grid(column=1, row=4, columnspan=2, sticky="EW")

generate_b = Button(text="Generate Password", command=generate_password)
generate_b.grid(column=2, row=3, sticky="EW")

search_b = Button(text="Search", command=search)
search_b.grid(column=2, row=1, sticky="EW")


window.mainloop()
