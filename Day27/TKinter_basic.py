import tkinter

window = tkinter.Tk()
window.title("First GUI")
window.minsize(width=500, height=300)

txt = "I Am a Label"

label = tkinter.Label(text=txt, font=("Montserrat", 24, "bold"))
label.pack()

def btnClicked():
    label["text"] = input.get()

button = tkinter.Button(text="Click Me", command=btnClicked)
button.pack()

input = tkinter.Entry()
input.pack()







window.mainloop()

