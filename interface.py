import random
from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for _ in range(nr_letters):
        password_list.append(random.choice(letters))

    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))

    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    email = email_entry.get()
    password = password_entry.get()
    if email and password:
        with open("passwords.txt", "a") as file:
            file.write(f"Email: {email} | Password: {password}\n")
        messagebox.showinfo(title="Success", message="Password saved successfully!")
    else:
        messagebox.showwarning(title="Warning", message="Please enter an email and generate a password!")

# ---------------------------- RESET ------------------------------- #
def reset():
    email_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")  # Add your own logo image
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

email_label = Label(text="Email:")
email_label.grid(row=1, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=1, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=2, column=0)

password_entry = Entry(width=35)
password_entry.grid(row=2, column=1, columnspan=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(row=3, column=1)

save_button = Button(text="Save", command=save_password)
save_button.grid(row=3, column=2)

window.mainloop()
