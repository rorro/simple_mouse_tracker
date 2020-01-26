import numpy
from PIL import Image

COORDINATES_FILE = "mouse_positions.txt"

def main():
    data = numpy.zeros((1080, 1920, 3), dtype=numpy.uint8)

    cf = open(COORDINATES_FILE, "r")
    for line in cf:
        pos = line.rstrip().split(",")
        pos = (int(pos[1]), int(pos[0]))
        data[pos] = [255,0,0]
    image = Image.fromarray(data)
    image.show()
main()

