import tkinter as tk

window = tk.Tk()
entry = tk.Entry()


def delete():
    # Deletes first character from entry
    entry.delete(0)

    # Deletes up till (exclusively) the 5th character
    entry.delete(0, 4)


def insert():
    entry.insert(0, "Python")


def input_text():
    label = tk.Label(text="Name")
    label.pack()
    entry.pack()
    button = tk.Button(text="Delete", command=delete)
    button.pack()
    window.mainloop()



