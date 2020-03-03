import tkinter as tk
from tkinter import filedialog, PhotoImage, StringVar

from system_hotkey import SystemHotkey

import config
import track_mouse
import draw_pixels

class MainWindow:
    def __init__(self, parent):
        self.config = config.Config()
        self.mt = track_mouse.MouseTracker()

        self.hk = SystemHotkey()
        self.hk.register(self.config.start_tracking_binding,
                callback=self.start_tracking)

        self.is_tracking = False

        self.parent = parent
        parent.title("SMT")
        parent.resizable(False, False)

        self.icon = PhotoImage(file="icon.png")
        parent.tk.call('wm', 'iconphoto', parent._w, self.icon)

        self.screen_size = (parent.winfo_screenwidth(),
                parent.winfo_screenheight())

        self.status_lbl = tk.Label(parent,
                text="● Stopped",
                fg="red",
                bg="#d9d9d9",
                relief=tk.SUNKEN)

        self.status_lbl.pack(side=(tk.BOTTOM), fill=tk.X)

        self.selected_file = StringVar()
        self.selected_file.set("Select file...")

        self.track_btn = tk.Button(parent,
                text="Start tracking",
                command=self.start_tracking,
                bg="#0097A7",
                fg="#FFFFFF",
                relief=tk.FLAT,
                activebackground="#0087A7",
                activeforeground="#FFFFFF",
                width=10)

        self.track_btn.grid_propagate(False)
        self.track_btn.pack(fill=tk.X)

        self.draw_btn = tk.Button(parent,
                text="Export/Show",
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


    def start_tracking(self, event=""):
        if not self.is_tracking:
            self.is_tracking = True
            self.status_lbl.configure(text="● Tracking", fg="green")
            self.track_btn.configure(text="Stop tracking")
            self.mt = track_mouse.MouseTracker(self.config.save_folder)
            self.mt.thread.start()

        else:
            self.is_tracking = False
            self.status_lbl.configure(text="● Stopped", fg="red")
            self.track_btn.configure(text="Start tracking")
            self.mt.terminate()
            self.mt.thread.join()


    def export_png(self):
        draw_pixels.draw(self.selected_file.get(), self.screen_size, True)


    def show_tracked(self):
        draw_pixels.draw(self.selected_file.get(), self.screen_size)


    def select_file(self):
        file_path = filedialog.askopenfilename(
                initialdir = self.config.save_folder,
                title = "Select file",
                filetypes = (("Tracked","*.tracked"),))

        if file_path:
            self.selected_file.set(file_path)


    def show_popup(self):
        popup = tk.Toplevel(self.parent)
        popup.title("Export/Show")
        popup.tk.call('wm', 'iconphoto', popup._w, self.icon)
        x = self.parent.winfo_x()
        y = self.parent.winfo_y()
        popup.geometry("+"+str(x-80)+"+"+str(y))
        popup.resizable(False, False)

        popup_input = tk.Entry(popup, textvariable=self.selected_file)

        popup_select_btn = tk.Button(popup,
                text="Select file",
                command=self.select_file,
                bg="#0097A7",
                fg="#FFFFFF",
                relief=tk.FLAT,
                activebackground="#0087A7",
                activeforeground="#FFFFFF")

        popup_export_btn = tk.Button(popup,
                text="Export png",
                command=self.export_png,
                bg="#0097A7",
                fg="#FFFFFF",
                relief=tk.FLAT,
                activebackground="#0087A7",
                activeforeground="#FFFFFF")


        popup_show_tracked_btn = tk.Button(popup,
                text="Show tracked",
                command=self.show_tracked,
                bg="#0097A7",
                fg="#FFFFFF",
                relief=tk.FLAT,
                activebackground="#0087A7",
                activeforeground="#FFFFFF")

        popup_input.grid(row=0, column=0, sticky="news")
        popup_select_btn.grid(row=0, column=1, sticky="ew")
        popup_export_btn.grid(row=1, column=0, sticky="ew")
        popup_show_tracked_btn.grid(row=1, column=1, sticky="ew")

        popup.grab_set()


    def draw_stuff(self):
        self.show_popup()


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
