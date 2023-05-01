from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data_dict = pandas.read_csv("./data/unknown_words.csv")
    if len(data_dict) == 0:
        data_dict = pandas.read_csv("./data/french_words.csv")
except FileNotFoundError:
    data_dict = pandas.read_csv("./data/french_words.csv")
    data_records = data_dict.to_dict(orient="records")
else:
    data_records = data_dict.to_dict(orient="records")

new_word = {}
btn_clicked = False
def update_back():
    canvas.itemconfig(background_image, image=flashBack)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(content, text=new_word["English"], fill="white")

def update_word( ):
    global update_id
    global new_word
    window.after_cancel(update_id)
    new_word = random.choice(data_records)
    canvas.itemconfig(content, text=new_word["French"], fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(background_image, image=flashFront)

    update_id = window.after(3000, update_back)

def update_known():
    # print(type(data_dict))
    # print(new_word)
    # new_data_dict = {row for row in data_dict.iterrows()}
    # print(new_data_dict)
    data_records.remove(new_word)
    new_data_dict_df = pandas.DataFrame(data_records)
    new_data_dict_df.to_csv(path_or_buf="./data/unknown_words.csv", index=False)
    print(new_data_dict_df)
    update_word()

 
window = Tk()
window.title("Flash Card Application")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
update_id = window.after(3000, update_word)

canvas = Canvas(height=526, width=800, background=BACKGROUND_COLOR, highlightthickness=0)

flashFront = PhotoImage(file="./images/card_front.png")
flashBack = PhotoImage(file="./images/card_back.png")

right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")

background_image = canvas.create_image(400, 263, image=flashFront)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
content = canvas.create_text(400, 263, text="Content", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=3)

rightBtn = Button(image=right)
rightBtn.config(command=update_known, highlightthickness=0)

rightBtn.grid(row=1, column=0)

wrongBtn = Button(image=wrong)
wrongBtn.grid(row=1, column=2)
wrongBtn.config(command=update_word, highlightthickness=0)

update_word()
window.mainloop()


