# imports
import tkinter as tk

# define the click button
def click_button():
    global click_count
    click_count += 1
    label.config(text=f'You currently have {click_count} Clicks!')

# define click count
click_count = 0

# create the window
root = tk.Tk()
root.title("Basic Python Clicker")

# windows width and height
root.geometry("400x200")

frame = tk.Frame(root)
frame.pack(expand=True)

# the label for your click count
label = tk.Label(frame, text=f'You currently have {click_count} Clicks!')
label.pack()

# spacing between da text and da buttons
spacer = tk.Label(frame, text='', height=2)
spacer.pack()

# the button to click
button = tk.Button(frame, text="Click Me", command=click_button)
button.pack()

# the main loop
root.mainloop()
