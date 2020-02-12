import tkinter as tk

from track_mouse import *

is_tracking = False

window = tk.Tk()
window.geometry("320x300")
window.title("Simple Mouse Tracker")

tracked_lbl = tk.Label(window, text="Status: Inactive")
tracked_lbl.grid(column=1, row=0)

def start_tracking():
    global is_tracking
    if not is_tracking:
        tracked_lbl.configure(text="Status: Tracking")
        track_btn.configure(text="Stop tracking")
        is_tracking = True
    else:
        tracked_lbl.configure(text="Status: Inactive")
        track_btn.configure(text="Start tracking")
        is_tracking = False

def draw_stuff():
    print("Draw stuff")

def quit():
    global window
    window.quit()
    print("exit app")


track_btn = tk.Button(window, text="Start tracking", command=start_tracking)
track_btn.grid(column=0, row=0, sticky="W")

draw_btn = tk.Button(window, text="Draw stuff", command=draw_stuff)
draw_btn.grid(column=0, row=1, sticky="W")

quit_btn = tk.Button(window, text="Quit", command=quit)
quit_btn.grid(column=0, row=2, sticky="W")

window.mainloop()
