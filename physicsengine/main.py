import pygame
from pygame import display
from squarea import sqarea, pixel
from exceptions import spaceoccupied
from threading import Thread

colors = {"black": (0, 0, 0), "white": (255, 255, 255)}


def worker(queue):
    while True:
        item = queue.get()

        surface = item[0]
        pos = item[1]
        obj = item[2]
        color = item[3]
        background = item[4]

        if obj:
            surface.set_at(pos, color)
        else:
            surface.set_at(pos, background)
        if queue.empty():
            return


class window:
    def __init__(self, screen, background):
        self.background = background
        self.surface = screen

        self.surface.fill(background)

        self.pixd = {}
        for x in range(1, 1001):
            for y in range(1, 1001):
                self.pixd[(x, y)] = None

    def addobj(self, obj, pos):
        if self.pixd[pos]:
            raise spaceoccupied
        else:
            self.pixd[pos] = obj

    def clearpos(self, pos):
        if self.pixd[pos]:
            self.pixd[pos] = None

    def moveobj(self, obj, pos):
        if self.pixd[pos]:
            raise spaceoccupied
        else:
            self.pixd[(obj.x, obj.y)] = None
            self.pixd[pos] = obj

    def render(self, area):
        ar1 = area[0]
        ar2 = area[1]

        for x in range(1, ar1+1):
            for y in

        display.update()


class block:
    def __init__(self, surface, center, length):
        # length only takes integar values
        if type(length) != int or type(center) != tuple:
            raise TypeError

        self.parray = []
        self.surface = surface
        self.center = center
        self.length = length

        # for x, + is right and - is left; for y, + is down and - is up

        sarray = sqarea(self.center, length)
        for x in sarray:
            p = pixel(x, colors["black"], self.surface, colors["white"])
            self.surface.addobj(p, x)
            self.parray.append(p)

    def down(self, num):
        pass


def main():
    pygame.init()

    surface = display.set_mode((1000, 1000))
    screen = window(surface, colors["white"])

    block1 = block(screen, (100, 100), 10)
    screen.render()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.display.update()
                screen.render()
                print("done")

            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()
