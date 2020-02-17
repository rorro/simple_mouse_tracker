import tkinter as tk
from tkinter import filedialog

import track_mouse
import draw_pixels

class MainWindow:
    def __init__(self, parent):
        self.mt = track_mouse.MouseTracker()

        self.is_tracking = False

        self.parent = parent
        parent.title("SMT")
        parent.configure(bg="red")
        parent.resizable(False, False)

        self.status_lbl = tk.Label(parent, text="Status: Stopped", fg="red", bg="#FFFFFF")
        self.status_lbl.pack(side=(tk.BOTTOM), fill=tk.X)

        self.track_btn = tk.Button(parent,
                text="Start tracking",
                command=self.start_tracking,
                bg="#0097A7",
                fg="#FFFFFF",
                relief=tk.FLAT,
                activebackground="#0087A7",
                activeforeground="#FFFFFF")
        self.track_btn.grid_propagate(False)

        self.track_btn.pack(fill=tk.X)

        self.draw_btn = tk.Button(parent,
                text="Draw stuff",
                command=self.draw_stuff,
                bg="#0097A7",
                fg="#FFFFFF",
                relief=tk.FLAT,
                activebackground="#0087A7",
                activeforeground="#FFFFFF")

        self.draw_btn.pack(fill=tk.X)

        self.quit_btn = tk.Button(parent,
                text="Quit",
                command=self.quit,
                bg="#0097A7",
                fg="#FFFFFF",
                relief=tk.FLAT,
                activebackground="#0087A7",
                activeforeground="#FFFFFF")

        self.quit_btn.pack(fill=tk.X)

    def start_tracking(self):
        if not self.is_tracking:
            self.is_tracking = True
            self.status_lbl.configure(text="Status: Tracking", fg="green")
            self.track_btn.configure(text="Stop tracking")
            self.mt = track_mouse.MouseTracker()
            self.mt.thread.start()

        else:
            self.is_tracking = False
            self.status_lbl.configure(text="Status: Stopped", fg="red")
            self.track_btn.configure(text="Start tracking")
            self.mt.terminate()
            self.mt.thread.join()

    def draw_stuff(self):
        file_path = filedialog.askopenfilename(
                title = "Select file",
                filetypes = (("Tracked","*.tracked"),))

        if file_path:
            draw_pixels.draw(file_path)

    def quit(self):
        if self.is_tracking:
            self.is_tracking = False
            self.mt.terminate()
            self.mt.thread.join()

        self.parent.quit()


if __name__ == '__main__':
    root = tk.Tk()
    main_window = MainWindow(root)
    root.mainloop()