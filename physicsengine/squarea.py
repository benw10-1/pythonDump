import pygame


class pixel(object):
    def __init__(self, start, color, surface, background):
        self.x = start[0]
        self.y = start[1]
        self.color = color
        self.surface = surface
        self.background = background


def sqarea(center, length):
    cx = int(center[0])
    cy = int(center[1])

    hlength = int(length / 2)

    posin = (cx, cy + hlength + 1)
    posout = (cx, cy - hlength + 1)

    coordinates = []
    for x in list(range(min(posin), max(posin))):
        for y in list(range(min(posin), max(posin))):
            coordinates.append((x, y))

    for x in list(range(min(posin), max(posin))):
        for y in list(range(min(posout), max(posout))):
            coordinates.append((x, y))

    for x in list(range(min(posout), max(posout))):
        for y in list(range(min(posin), max(posin))):
            coordinates.append((x, y))

    for x in list(range(min(posout), max(posout))):
        for y in list(range(min(posout), max(posout))):
            coordinates.append((x, y))

    return coordinates


sqarea((100, 0), 5)
