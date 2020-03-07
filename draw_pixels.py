from PIL import Image, ImageDraw

def draw(coordinates_file, screen_size, export=False):
    # Create image
    img = Image.new('RGBA', screen_size, (255,255,255,0))
    draw = ImageDraw.Draw(img)

    try:
        cf = open(coordinates_file, "r")
        prev_pos = format_pos(cf.readline())

        for line in cf:
            if line.rstrip() == "paused":
                prev_pos = format_pos(cf.readline())
                curr_pos = format_pos(cf.readline())
            else:
                curr_pos = format_pos(line)

            draw.line((prev_pos, curr_pos), fill="black")
            prev_pos = curr_pos

        cf.close()
        if export:
            img.save(coordinates_file.split(".")[0] + ".png")
        else:
            img.show(coordinates_file)

    except:
        print("File is empty or has bad contents!")

def format_pos(line):
    split = line.rstrip().split(",")
    return int(split[0]), int(split[1])
