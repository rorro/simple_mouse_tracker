from pymouse import PyMouse
import threading
from datetime import datetime

class MouseTracker():
    def __init__(self):
        now = datetime.now()
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

    def get_tracked(self):
        return self.tracked

    def start(self):
        self.running = True
        last_pos = (-1,-1)
        sf = open(self.file_name, "a")
        while self.running:
            mouse_x, mouse_y = self.mouse.position()

            if last_pos != (mouse_x, mouse_y):
                #print("x = %i y = %i n=%i" % (mouse_x,mouse_y,self.tracked))

                sf.write(str(mouse_x)+","+str(mouse_y)+"\n")
                last_pos = (mouse_x, mouse_y)
                self.tracked+=1

        sf.close()

    def terminate(self):
        self.running = False

