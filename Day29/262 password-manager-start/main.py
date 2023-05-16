from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    randomLetters = [random.choice(letters) for char in range(nr_letters)]
    # print(randomLetters)
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    randomSymbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    # print(randomSymbols)
    randomNumbers = [random.choice(numbers) for number in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    # print(randomNumbers)
    password_list = randomNumbers + randomSymbols + randomLetters
    random.shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #     password += char

    # print(f"Your password is: {password}")
    passwordEntry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def addToFile(website, email, password):
    if (len(website) == 0 or len(password) == 0):
        messagebox.showerror(title="Oops", message="You cannot leave either of the feilds empty")
    else:
        isOk = messagebox.askokcancel(title=website, message=f"The entered website is {website}\nEmail: {email}\nPassword: {password}")
        if (isOk):
            with open("data.txt", "a") as data:
                dataLine = f"{website} | {email} | {password} \n"
                data.writelines(dataLine)
                websiteEntry.delete(0, END)
                passwordEntry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
photoImage = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=photoImage)
canvas.grid(row=0, column=1)

websiteLabel = Label(text="Website:")
websiteLabel.grid(row=1, column=0)
emailLabel = Label(text="Email/Username")
emailLabel.grid(row=2, column=0)
passwordLabel = Label(text="Password")
passwordLabel.grid(row=3, column=0)

websiteEntry = Entry(width=35)
websiteEntry.focus()
websiteEntry.grid(row=1, column=1, columnspan=2)
emailEntry = Entry(width=35)
emailEntry.insert(END, "khesehang81@gmail.com")
emailEntry.grid(row=2, column=1, columnspan=2)
passwordEntry = Entry(width=18)
passwordEntry.grid(row=3, column=1)


generateBtn = Button(text="Generate Password", width=14, command=generate)
generateBtn.grid(row=3, column=2)
addBtn = Button(text="Add", width=32, command=lambda : addToFile(website=websiteEntry.get(), email=emailEntry.get(), password=passwordEntry.get()))
addBtn.grid(row=4, column=1, columnspan=2)



window.mainloop()
