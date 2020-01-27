from Xlib import display

SAVE_FILE = "mouse_positions.txt"
SAVE_BEFORE_WRITE = 1000

def main():
    last_pos = (-1,-1)
    last_1000 = []
    while last_pos != (0,0):
        data = display.Display().screen().root.query_pointer()._data
        mouse_x = data["root_x"]
        mouse_y = data["root_y"]

        if last_pos != (mouse_x, mouse_y):
            last_pos = (mouse_x, mouse_y)
            if last_pos not in last_1000:
                last_1000.append(last_pos)

            print("x = %i y = %i n=%i" % (mouse_x,mouse_y,len(last_1000)))

        if len(last_1000) == SAVE_BEFORE_WRITE:
            sf = open(SAVE_FILE, "a")
            for pos in last_1000:
                sf.write(str(pos[0])+","+str(pos[1])+"\n")
            sf.close()
            last_1000.clear()

if __name__ == '__main__':
    main()
