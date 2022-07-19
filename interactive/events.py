import tkinter as tk


window = tk.Tk()
events = []


# Create an event handler
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)


def handle_click(event):
    print("The button was clicked!")

button = tk.Button(text="Click me!")

button.bind("<Button-1>", handle_click)
button.pack()
# always takes 2 arguments
# an event represented by "<event_name>" - Tkinter events
# an event handler - function to be called whenever event occurs
window.bind("<Key>", handle_keypress)

window.mainloop()

# Bind handling keypress equivalent to the below:
# Run the event loop
while True:
    #  If event list is empty, no events have occurred
    #  and skips to next iteration of the loop
    if events == []:
        continue

    # If execution reaches this point, there is at least one
    # event object in the event list
    event = events[0]

    # If event is a keypress event object
    if event.type == "keypress":
        # Call the keypress event handler
        handle_keypress(event)
