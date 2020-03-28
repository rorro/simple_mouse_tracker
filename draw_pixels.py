from PIL import Image, ImageDraw, ImageColor
import math

GRADIENT = [
            "#00008b",
            "#530089",
            "#7c0084",
            "#9d007c",
            "#b90072",
            "#d10067",
            "#e4005c",
            "#f4004f",
            "#ff2f42",
            "#ff5335",
            "#ff7025",
            "#ff8b12",
            "#ffa600",
            "#ffbf00",
            "#ffd700",
        ]

SPEED_LIMIT = 5000
GRADIENT_SIZE = len(GRADIENT)
SPEED_GRADER = SPEED_LIMIT/GRADIENT_SIZE

def draw(coordinates_file, screen_size, export=False):
    # Create image
    img = Image.new('RGBA', screen_size, (255,255,255,0))
    draw = ImageDraw.Draw(img)

    cf = open(coordinates_file, "r")

    prev_line = format_line(cf.readline())
    prev_pos = (prev_line[0], prev_line[1])
    prev_time = prev_line[2]

    for line in cf:
        if line.rstrip() == "paused":
            break
            prev_line = format_line(cf.readline())
            prev_pos = (prev_line[0], prev_line[1])
            prev_time = prev_line[2]

            curr_line = format_line(cf.readline())
            curr_pos = (curr_line[0], curr_line[1])
            curr_time = curr_line[2]
        else:
            curr_line = format_line(line)
            curr_pos = (curr_line[0], curr_line[1])
            curr_time = curr_line[2]

        speed = get_speed(prev_pos[0], prev_pos[1], prev_time,
                            curr_pos[0], curr_pos[1], curr_time)

        color_index = int(speed/SPEED_GRADER)

        if color_index >= GRADIENT_SIZE:
            color_index = GRADIENT_SIZE-1

        color = ImageColor.getrgb(GRADIENT[color_index])

        draw.line((prev_pos, curr_pos), fill=color)
        prev_pos = curr_pos
        prev_time = curr_time

    cf.close()
    if export:
        img.save(coordinates_file.split(".")[0] + ".png")
    else:
        img.show(coordinates_file)


def format_line(line):
    split = line.rstrip().split(",")
    return int(split[0]), int(split[1]), float(split[2])

def get_speed(x1, y1, t1, x2, y2, t2):
    dx = x2 - x1
    dy = y2 - y1
    dist = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
    dt = t2 - t1

    return dist/dt

