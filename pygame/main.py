import pygame
import numpy as np

pygame.init()

display_width = 1000
display_height = 1000

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Peenam')

black = (0, 0, 0)
white = (255, 255, 255)
random = (255, 0, 0)
clock = pygame.time.Clock()
crashed = False

x = 0
y = 0
draw = False

gameDisplay.fill(white)
scale = 10
i = 0
for x in range(0, 1001):
    if i == 500:
        pygame.draw.line(gameDisplay, black, (i, 0), (i, 1000), 2)
        pygame.draw.line(gameDisplay, black, (0, i), (1000, i), 2)
    elif i % scale == 0:
        pygame.draw.line(gameDisplay, black, (i, 0), (i, 1000))
        pygame.draw.line(gameDisplay, black, (0, i), (1000, i))
    i += 1
pygame.display.update()
clock.tick(60)
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
        """if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 5:
                gameDisplay.fill(white)
                i = 0
                print(scale)
                for x in range(0, 1001):
                    if i % scale == 0:

                        pygame.draw.line(gameDisplay, black, (i, 0), (i, 1000))
                        pygame.draw.line(gameDisplay, black, (0, i), (1000, i))

                    i += 1
                pygame.display.update()
                clock.tick(60)
                if scale > 1:
                    scale -= 1
                else:
                    scale = 1
            elif event.button == 4:
                gameDisplay.fill(white)
                i = 0
                print(scale)

                for x in range(0, 1001):
                    if i % scale == 0:
                        pygame.draw.line(gameDisplay, black, (i, 0), (i, 1000))
                        pygame.draw.line(gameDisplay, black, (0, i), (1000, i))

                    i += 1
                pygame.display.update()
                clock.tick(60)
                if scale > 500:
                    scale = 500
                else:
                    scale += 1"""

    s = "x^2+2x+1"
    s = s.replace("-", "+-")
    s = s.split("+")

    if draw == False:
        p = 0
        old = (500, 500)
        for y in range(-100, 100):
            total = 0
            num = str(y)
            for x in s:
                if "x" in x:
                    if "^" in x:
                        total += float(x.split("^")[0].replace("x", num)) ** float(x.split("^")[1])
                    else:
                        total += float(x.split("x")[0]) * float(num)
                else:
                    total += float(x)

            current = ((int(num)*scale)+500, int(-int(total)*scale)+500)
            if p != 0:
                pygame.draw.line(gameDisplay, random, old, current, 2)
                gameDisplay.set_at(current, black)

            old = current
            p += 1
        pygame.display.update()
        clock.tick(30000)
        draw = True

pygame.quit()
