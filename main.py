import tkinter as t
from tkinter import messagebox, simpledialog
import string
import random
import pyperclip

string.punctuation
PATH = "Day_29//"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    possible_chars = string.ascii_letters + string.digits + string.punctuation
    password_lenght = simpledialog.askinteger("Password Lenght", "How many characters should the password contain?", minvalue=1, initialvalue=20)
    generated_password  = [random.choice(possible_chars) for _ in range(password_lenght)]
    random.shuffle(generated_password)
    password_entry.delete(0, len(password_entry.get()))
    password_entry.insert(0, "".join(generated_password))
    pyperclip.copy(password_entry.get())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_passwords():
    password = password_entry.get()
    email = user_entry.get()
    website = website_entry.get()
    if len(password) == 0 or len(website) == 0 or len(email) == 0:
        messagebox.showinfo(title="Error", message="Please do not leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"""These are the details entered: \nEmail:{email}
Password: {password_entry.get()} \n Is it ok to save? """)
        if is_ok:
            with open(PATH + 'data.txt', "a+") as f:
                f.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, len(website_entry.get()))
                password_entry.delete(0, len(password))
                website_entry.focus()
                f.close()


# ---------------------------- UI SETUP ------------------------------- #
window = t.Tk()
window.title("Pssword Manager")
window.config(padx=30, pady=50)
canvas = t.Canvas(width=200, height=200, highlightthickness=0)
logo = t.PhotoImage(file=PATH + "logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = t.Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = t.Entry(width=51)
website_entry.grid(row=1, column=1, columnspan=2, padx=2, pady=5)
website_entry.focus()

user_label = t.Label(text="Email/Username:")
user_label.grid(row=2, column=0)
user_entry = t.Entry(width=51)
user_entry.grid(row=2, column=1, columnspan=3, padx=2, pady=5)
user_entry.insert(0, 'default@example.com')

password_label = t.Label(text='Password:')
password_label.grid(row=3, column=0)
password_entry = t.Entry(width=32)
password_entry.grid(row=3, column=1, padx=2, pady=5)

generate_buttom = t.Button(text="Generate Password", command=generate_password)
generate_buttom.grid(row=3, column=2, padx=2, pady=5)

add_buttom = t.Button(text="Add", width=43, command=add_passwords)
add_buttom.grid(row=4, column=1, columnspan=2, padx=2, pady=5)

window.mainloop()
