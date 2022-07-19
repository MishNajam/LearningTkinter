import tkinter as tk


# .grid() works by splitting a window/frame into rows and columns
# specify the location by calling grid, and passing row and column indices
window = tk.Tk()

for i in range(3):
    # .columnconfigure() and .rowconfigure() adjusts how the rows and columns of the grid grow as window resized
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)

window.mainloop()

window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky="ne")

label2 = tk.Label(text="B")
label2.grid(row=1, column=0, sticky="sw")

window.mainloop()

window = tk.Tk()

window.rowconfigure(0, minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=50)

label1 = tk.Label(text="1", bg="black", fg="white")
label2 = tk.Label(text="2", bg="black", fg="white")
label3 = tk.Label(text="3", bg="black", fg="white")
label4 = tk.Label(text="4", bg="black", fg="white")

label1.grid(row=0, column=0)
# .pack(fill=tk.X)
label2.grid(row=0, column=1, sticky="ew")
# .pack(fill=tk.Y)
label3.grid(row=0, column=2, sticky="ns")
# .pack(fill=tk.BOTH)
label4.grid(row=0, column=3, sticky="nsew")

window.mainloop()
