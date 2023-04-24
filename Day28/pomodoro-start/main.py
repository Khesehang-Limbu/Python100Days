from tkinter import *
import math

# Dynamic Typing:
# Though Python is strongly typed in the sense that one cannot perform operations outside the scope of the data types
# Like, "hello" + 9, however, we can change what type of data a variable can store, making python a dynamically typed language
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
tick = "✔"
timerStart = None

# ---------------------------- TIMER RESET ------------------------------- #
def resetTimer():
    window.after_cancel(timerStart)
    title.config(text="Timer")
    canvas.itemconfig(timerText, text="00:00")
    checkMarks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer():
    global reps
    reps += 1

    workSecs = WORK_MIN * 60
    shortBreakSecs = SHORT_BREAK_MIN * 60
    longBreakSecs = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title.config(text="Taking a Long Break", fg=RED)
        counter(longBreakSecs)
    elif reps % 2 != 0:
        title.config(text="Working")
        checkMarks.config(text=tick)
        counter(workSecs)
    elif reps % 2 == 0:
        title.config(text="Taking a Short Break", fg=PINK)
        counter(shortBreakSecs)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(count):
    countMin = math.floor(count / 60)
    countSec = math.floor(count % 60)

    if countSec == 0:
        countSec = "00"
    elif countSec <= 9:
        countSec = f"0{countSec}"

    if countMin <= 9:
        countMin = f"0{countMin}"

    canvas.itemconfig(timerText, text=f"{countMin}:{countSec}")
    if count > 0:
        global timerStart
        timerStart = window.after(1000, counter, count - 1)
    else:
        timer()
        global reps
        global tick
        for _ in range(math.floor(reps / 2)):
            tick = tick + "✔"
        checkMarks.config(text=tick)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomadoro App")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

photoImage = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photoImage)
timerText = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

title = Label()
title.config(font=(FONT_NAME, 50, "bold"), fg=GREEN, text="Timer", bg=YELLOW)
title.grid(row=0, column=1)

startBtn = Button()
startBtn.config(font=FONT_NAME, text="Start", fg="black", padx=0, pady=0, bg="white", highlightthickness=0, command=timer)
startBtn.grid(row=2, column=0)

resetBtn = Button()
resetBtn.config(font=FONT_NAME, text="Reset", fg="black", padx=0, pady=0, bg="white", highlightthickness=0, command=resetTimer)
resetBtn.grid(row=2, column=2)

checkMarks = Label()
checkMarks.config(fg=GREEN, bg=YELLOW)
checkMarks.grid(row=2, column=1)

window.mainloop()
