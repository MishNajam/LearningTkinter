import tkinter as tk


# .pack() geometry managers uses a packing algorithm to place widgets in a frame of window in a specifed order

# Step 1, compute a rectangular area called a parcel that's just tall (or wide)
# enough to hold the widget and fills the reamining width (or height) in the window with blank space.

# Step 2 center the widget in the parcel unless a different location is specified
# tk.X fill in horizontally
# tk.Y fill in vertically
# tk.BOTH fill in both directions
window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()

