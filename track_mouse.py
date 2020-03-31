from pymouse import PyMouse
import threading
from datetime import datetime
import time

class MouseTracker():
    def __init__(self, save_folder):
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

        self.tracking = False
        self.paused = False
        self.thread = threading.Thread(target=self.start)

        self.tracked = 0
        self.sf = None
        self.is_last_paused = False


    def start(self):
        self.tracking = True
        last_pos = (-1,-1)

        file_path = self.save_folder + "/" + self.file_name

        try:
            self.sf = open(file_path, 'a')
            while self.tracking:
                if not self.paused:
                    mouse_x, mouse_y = self.mouse.position()
                    now = time.time()


                    if last_pos != (mouse_x, mouse_y):
                        self.sf.write(str(mouse_x) + ',' + str(mouse_y) + "," + str(now) + "\n")
                        self.is_last_paused = False
                        last_pos = (mouse_x, mouse_y)
                        self.tracked += 1

            self.sf.close()
        except FileNotFoundError:
            print("Save folder does not exist.")

    def terminate(self):
        self.tracking = False
        self.paused = False

