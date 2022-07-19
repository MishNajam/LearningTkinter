import tkinter as tk
import random


def roll():
    lbl_value["text"] = f"{random.randint(1,6)}"

window = tk.Tk()
window.rowconfigure(1, minsize=50)
window.columnconfigure(0, minsize=150)

btn_roll = tk.Button(master=window, text="Roll", command=roll)
btn_roll.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window)
lbl_value.grid(row=1, column=0)

window.mainloop()

