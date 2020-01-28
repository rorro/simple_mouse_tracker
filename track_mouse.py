from pymouse import PyMouse

SAVE_FILE = "mouse_positions.txt"

def main():
    mouse = PyMouse()

    sf = open(SAVE_FILE, "a")
    tracked = 0

    last_pos = (-1,-1)
    while last_pos != (0,0):
        mouse_x, mouse_y = mouse.position()

        if last_pos != (mouse_x, mouse_y):
            print("x = %i y = %i n=%i" % (mouse_x,mouse_y,tracked))

            sf.write(str(mouse_x)+","+str(mouse_y)+"\n")
            last_pos = (mouse_x, mouse_y)
            tracked+=1

    sf.close()

if __name__ == '__main__':
    main()
