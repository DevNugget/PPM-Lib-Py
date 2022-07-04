from PIL import Image
import ppmLib as tg
import pygame

PPM = ""

c_w = 250
c_h = 250

PPM += tg.genHeader(3)
PPM += tg.genImgSize(c_w, c_h)
PPM += tg.genMaxColor(255)

steepness = 2
tg_base = 1
attempt = 1

red = 225
green = 0
blue = 0

def rgb_triangle():
    global c_h, c_w, red, green, blue, PPM, attempt, tg_base, steepness

    for i in range(c_h):
        h_range = int(c_w / 2 - tg_base)
        remainder = int((c_w - h_range - tg_base - tg_base)) 

        for j in range(h_range):
            PPM += tg.genPixel(255, 255, 255)

        for k in range(tg_base):
            PPM += tg.genPixel(red, green, 0)
            if attempt > 0:
                PPM += tg.genPixel(red, green, blue)
                if attempt < 90:
                    blue += 1
                else:
                    blue += 2
            else:
                PPM += tg.genPixel(red, green, 0)
        
        for l in range(remainder):
            PPM += tg.genPixel(255, 255, 255)

        PPM += "\n"
        
        if attempt % steepness == 0:
            tg_base += 1
        
        attempt += 1
        if red > 0:
            red -= 1
        if green < 255 and attempt > 60:
            green += 1
        blue = 0

rgb_triangle()

tg.writeFile("tg.ppm", PPM)

im = Image.open("tg.ppm")
im.save("tg.png")
  
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
running = True

while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    ss = screen.get_size()
    w, h = ss[0] - 40, ss[1] - 40
    screen.blit(pygame.transform.scale(pygame.image.load("tg.png"), (w, h)), (20, 20))
    pygame.display.update()