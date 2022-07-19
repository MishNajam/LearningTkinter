import tkinter as tk


# .place() controls the precise location that a widget should occupy in a window/frame
# Must provide x and y coordinates from the top left - measured in pixels

# drawbacks - not responsive, difficult manage if lots of widgets
window = tk.Tk()

frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="I'm at (0,0)", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, text="I'm at (75,75)", bg="yellow")
label2.place(x=75, y=75)

window.mainloop()

