# Generate rgb triangle in ppm format
# Triangle should be 500x500 pixels

def genHeader(header: int):
    return "P" + str(header) + "\n"

def genImgSize(width, height):
    return str(width) + " " + str(height) + "\n"

def genMaxColor(maxColor):
    return str(maxColor) + "\n"

def genPixel(r, g, b):
    return str(r) + " " + str(g) + " " + str(b) + "\n"

def writeFile(filename, content):
    with open(filename, "w") as f:
        f.write(content)