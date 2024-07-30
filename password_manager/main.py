from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generator_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = [random.choice(letters) for char in range(nr_letters)] + [random.choice(symbols) for char in
                                                                              range(nr_symbols)] + [
                        random.choice(numbers) for char in range(nr_numbers)]

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    print(f"Your password is: {password}")
    entry_password.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_information():
    website = entry_website.get()
    email = entry_user_email.get()
    password = entry_password.get()
    new_data = {
        website:{
            "Email:": email,
            "Password:": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="", message="Please don't leave any fields empty!")
    else:
        try:
            with open("passwords.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("passwords.json", "w") as data_file:
                json.dump(new_data, data_file,indent=4)
        else:
            data.update(new_data)
            with open("passwords.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry_password.delete(0, END)
            entry_website.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    try:
        with open("passwords.json","r") as file:
            data = json.load(file)
            existing_email = data[entry_website.get()]["Email:"]
            existing_password = data[entry_website.get()]["Password:"]
            messagebox.showinfo(title="", message=f"Email: {existing_email}\nPassword: {existing_password}")
    except:
        messagebox.showinfo(title="", message="No data found")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

# canvas = Canvas()
# photo = PhotoImage(file = "logo.png")
# canvas.create_image(50,50, image = photo)
# canvas.grid(row=0, column=1)


website_label = Label(text="Website:")
website_label.grid(row=0, column=0)
user_email_label = Label(text="Email/Username:")
user_email_label.grid(row=1, column=0)
password_label = Label(text="Password:")
password_label.grid(row=2, column=0)

entry_website = Entry(width=30)
entry_website.grid(row=0, column=1)
entry_website.focus()
entry_user_email = Entry(width=50)
entry_user_email.grid(row=1, column=1, columnspan=2)
entry_user_email.insert(END, "sthomas2357@gmail.com")
entry_password = Entry(width=30)
entry_password.grid(row=2, column=1)

generate_button = Button(text="Generate Password",width=15,command=generator_password)
generate_button.grid(row=2, column=2)
add_button = Button(text="Add", width=42, command=save_information)
add_button.grid(row=3, column=1, columnspan=2)
search_button = Button(text = "Search",width=15, command=find_password)
search_button.grid(row=0, column= 2)
window.mainloop()
