import tkinter as tk
from tkinter import filedialog

import track_mouse
import draw_pixels

mt = track_mouse.MouseTracker()

is_tracking = False

window = tk.Tk()
window.geometry("320x300")
window.title("Simple Mouse Tracker")

tracked_lbl = tk.Label(window, text="Status: Inactive")
tracked_lbl.grid(column=1, row=0)

def start_tracking():
    global is_tracking
    global mt

    if not is_tracking:
        is_tracking = True
        tracked_lbl.configure(text="Status: Tracking")
        track_btn.configure(text="Stop tracking")
        mt = track_mouse.MouseTracker()
        mt.thread.start()

    else:
        is_tracking = False
        tracked_lbl.configure(text="Status: Inactive")
        track_btn.configure(text="Start tracking")
        mt.terminate()
        mt.thread.join()

def draw_stuff():
    file_path = filedialog.askopenfilename(
            title = "Select file",
            filetypes = (("Tracked","*.tracked"),))

    if file_path != '' and file_path != None:
        draw_pixels.draw(file_path)

def quit():
    global window
    global is_tracking

    if is_tracking:
        is_tracking = False
        mt.terminate()
        mt.thread.join()

    window.quit()


track_btn = tk.Button(window, text="Start tracking", command=start_tracking)
track_btn.grid(column=0, row=0, sticky="W")

draw_btn = tk.Button(window, text="Draw stuff", command=draw_stuff)
draw_btn.grid(column=0, row=1, sticky="W")

quit_btn = tk.Button(window, text="Quit", command=quit)
quit_btn.grid(column=0, row=2, sticky="W")

window.mainloop()
