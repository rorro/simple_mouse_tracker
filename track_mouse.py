from pymouse import PyMouse
import threading
from datetime import datetime

class MouseTracker():
    def __init__(self, save_folder=""):
        now = datetime.now()
        self.save_folder = save_folder
        self.file_name = "mouse_track-{}{}{}_{}{}{}.tracked".format(
                now.year,
                now.month,
                now.day,
                now.hour,
                now.minute,
                now.second)
        self.mouse = PyMouse()

        self.running = False
        self.thread = threading.Thread(target=self.start)

        self.tracked = 0


    def start(self):
        self.running = True
        last_pos = (-1,-1)

        if self.save_folder:
            file_path = self.save_folder + "/" + self.file_name
        else:
            file_path = self.file_name

        try:

            sf = open(file_path, "a")
            while self.running:
                mouse_x, mouse_y = self.mouse.position()

                if last_pos != (mouse_x, mouse_y):
                    sf.write(str(mouse_x)+","+str(mouse_y)+"\n")
                    last_pos = (mouse_x, mouse_y)
                    self.tracked+=1

            sf.close()
        except FileNotFoundError:
            print("Save folder does not exist.")


    def terminate(self):
        self.running = False

