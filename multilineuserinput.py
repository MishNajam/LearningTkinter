import tkinter as tk


def retrieve():
    half_first_word = text_box.get("1.0", "1.5")
    half_second_word = text_box.get("2.0", "2.5")
    everything = text_box.get("1.0", tk.END)
    print(f'{half_first_word}')
    print(f'{half_second_word}')
    print(everything)


def delete():
    text_box.delete("1.0", "1.4")


def clear():
    text_box.delete("1.0", tk.END)
    text_box.insert("1.0", "Hello")
    # text_box.insert("2.0", "\nWorld")
    text_box.insert(tk.END, "\nWorld")


window = tk.Tk()
text_box = tk.Text()
text_box.pack()
print_button = tk.Button(text="Print", command=retrieve)
print_button.pack()
delete_button = tk.Button(text="Delete", command=delete)
delete_button.pack()
clear_button = tk.Button(text="Clear", command=clear)
clear_button.pack()
window.mainloop()
