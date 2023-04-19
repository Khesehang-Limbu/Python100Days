import tkinter

window = tkinter.Tk()
window.config(padx=20, pady=20)
window.title("Miles to KM converter")

miles_input = tkinter.Entry()
miles_input.insert(tkinter.END, string="0")
miles_input.config(width=10)
miles_input.grid(row=0, column=1)

miles = tkinter.Label()
miles.config(text="Miles")
miles.grid(row=0, column=2)

equals = tkinter.Label()
equals.config(text="is equal to")
equals.grid(row=1, column=0)

value = tkinter.Label()
value.config(text="0")
value.grid(row=1, column=1)

km = tkinter.Label()
km.config(text="km")
km.grid(row=1, column=2)

def calculate():
    result = round(1.609 * float(miles_input.get()), 2)
    value.config(text=str(result))


calculate_btn = tkinter.Button()
calculate_btn.config(text="Calculate", command=calculate)
calculate_btn.grid(row=2, column=1)




window.mainloop()