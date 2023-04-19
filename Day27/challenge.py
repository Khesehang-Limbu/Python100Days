import tkinter

window = tkinter.Tk()
window.minsize(500, 500)
label = tkinter.Label(text="This is a label")
label.grid(row=0, column=0)

button = tkinter.Button(text="click me")
button.grid(row=1, column=1)

input = tkinter.Entry()
input.grid(row=3, column=3)

new_btn = tkinter.Button(text="new button")
new_btn.grid(row=0, column=2)


window.mainloop()