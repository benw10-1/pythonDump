import pygame
import os

objdict = {}
imagedict = {}
shownlist = []
render = []
cards = []
timedelta = 0
screend = (1000, 1000)


# blit with opacity
def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)


class objholder:
    def __init__(self, pos, image, name, shown=True):
        global objdict

        self.pos = list(pos)
        self.image = image
        self.name = name
        self.shown = shown

        self.fcalled = False
        self.holding = []

        self.opacity = 100

        self.dim = (image.get_width(), image.get_height())

        objdict[name] = self

        if self.shown:
            shownlist.append(self.name)

    def addhold(self, obj1):
        if obj1 not in self.holding:
            self.holding.append(obj1)

    def remhold(self, obj1):
        if obj1 in self.holding:
            self.holding.remove(obj1)

    def hold(self):
        ratio = len(self.holding)
        parts = []
        # gets divided locations
        for m in range(1, ratio+1):
            parts.append((self.pos[0]+self.dim[0])/(ratio+1)*m)

        for i, z in enumerate(self.holding):
            # check in it is held by mouse
            if not z.held:
                z.animate((parts[i]-z.getcenter()[0]+z.pos[0], self.dim[1]/2+self.pos[1]-z.getcenter()[1]+z.pos[1]))



    def hide(self):
        global shownlist
        self.shown = False
        shownlist.remove(self.name)

    def fadein(self, surface):
        if self.fcalled:
            if self.pos[0] < 0:
                self.pos[0] = 0
            if self.pos[0] + self.dim[0] > screend[0]:
                self.pos[0] = screend[0] - self.dim[0]
            if self.pos[1] < 0:
                self.pos[1] = 0
            if self.pos[1] + self.dim[1] > screend[1]:
                self.pos[1] = screend[1] - self.dim[1]

            blit_alpha(surface, self.image, (self.pos[0], self.pos[1]), self.opacity)
            if self.opacity < 500:
                self.opacity += 10

    def fadeout(self, surface):
        if self.fcalled:
            if self.pos[0] < 0:
                self.pos[0] = 0
            if self.pos[0] + self.dim[0] > screend[0]:
                self.pos[0] = screend[0] - self.dim[0]
            if self.pos[1] < 0:
                self.pos[1] = 0
            if self.pos[1] + self.dim[1] > screend[1]:
                self.pos[1] = screend[1] - self.dim[1]

            blit_alpha(surface, self.image, (self.pos[0], self.pos[1]), self.opacity)
            if self.opacity > 0:
                self.opacity -= 10

    def show(self):
        global shownlist
        self.shown = True
        shownlist.append(self.name)

    def inself(self, pos):
        # checking if position is in area of the image without using the built-in range() function
        if ((pos[0] < self.pos[0] + self.dim[0]) and (pos[0] > self.pos[0])) and (
                (pos[1] < self.pos[1] + self.dim[1]) and (pos[1] > self.pos[1])):
            return True
        else:
            return False


class obj:
    def __init__(self, pos, image, name, shown=False):
        global objdict

        self.pos = list(pos)
        self.image = image
        self.name = name
        self.shown = shown

        self.ani = False

        self.held = False
        self.holdpos = None
        self.holder = None

        self.dim = (image.get_width(), image.get_height())

        objdict[self.name] = self

    def animate(self, pos):
        global clock
        timedelta = clock.get_time()/1000
        if pos != self.pos:
            # if pos in x or y is greater than the position passed subtract
            if self.pos[0] > pos[0]:
                self.pos[0] -= 100*timedelta
            if self.pos[0] < pos[0]:
                self.pos[0] += 100*timedelta
            if self.pos[1] > pos[1]:
                self.pos[1] -= 100*timedelta
            if self.pos[1] < pos[1]:
                self.pos[1] += 100*timedelta

    def getcenter(self, index=None):
        return (self.dim[0])/2 + self.pos[0], (self.dim[1])/2 + self.pos[1]

    def hide(self):
        global shownlist
        self.shown = False
        shownlist.remove(self.name)

    def show(self):
        global shownlist
        self.shown = True
        shownlist.append(self.name)

    def inself(self, pos):
        # checking if position is in area of the image without using the built-in range() function
        if ((pos[0] < self.pos[0] + self.dim[0]) and (pos[0] > self.pos[0])) and (
                (pos[1] < self.pos[1] + self.dim[1]) and (pos[1] > self.pos[1])):
            return True
        else:
            return False

    def setpos(self, pos):
        self.pos[0], self.pos[1] = pos


    def hide(self):
        global shownlist
        self.shown = False
        shownlist.remove(self.name)

    def show(self):
        global shownlist
        self.shown = True
        shownlist.append(self.name)

    def blitself(self, surface):
        if self.pos[0] < 0:
            self.pos[0] = 0
        if self.pos[0] + self.dim[0] > screend[0]:
            self.pos[0] = screend[0] - self.dim[0]
        if self.pos[1] < 0:
            self.pos[1] = 0
        if self.pos[1] + self.dim[1] > screend[1]:
            self.pos[1] = screend[1] - self.dim[1]

        surface.blit(self.image, (self.pos[0], self.pos[1]))
        # blit_alpha(surface, self.image, (self.pos[0], self.pos[1]), 1000)

    def scale(self, scale):
        x = int(self.image.get_width() * scale)
        y = int(self.image.get_height() * scale)
        self.image = pygame.transform.scale(self.image, (x, y))


def initpics(folder):
    global imagedict
    global cards
    for file in os.listdir(folder):
        fullpath = folder + "\\" + file
        image = pygame.image.load(fullpath)

        scale = .1
        x = int(image.get_width() * scale)
        y = int(image.get_height() * scale)

        if file.replace(".png", "") != "rectlol":
            cards.append(file.replace(".png", ""))
            image = pygame.transform.scale(image, (x, y))
        else:
            image = pygame.transform.scale(image, (screend[0]-40, 100))

        imagedict[file.replace(".png", "")] = image


def main():
    folder = r"C:\Users\benja\PycharmProjects\cardcade\PNG"
    initpics(folder)

    pygame.init()
    screen = pygame.display.set_mode(screend)
    clock = pygame.time.Clock()

    play = True

    for key in imagedict:
        if key != "rectlol":
            card = obj((0, 0), imagedict[key], key)
        else:
            objholder((20, screend[1]-100), imagedict[key], key)
        if key == "JS":
            card.setpos((50,50))
            card.show()
        if key == "KS":
            card.setpos((100, 100))
            card.show()
        if key == "QS":
            card.setpos((0, 0))
            card.show()

    while play:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    inlist = []
                    for k in shownlist:
                        if type(objdict[k]) == obj:
                            if objdict[k].inself((x, y)):
                                inlist.append(k)
                    if inlist:
                        last = inlist[len(inlist) - 1]
                        shownlist.remove(last)
                        shownlist.append(last)

                        objdict[last].holdpos = (x - objdict[last].pos[0], y - objdict[last].pos[1])
                        objdict[last].held = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    for k in shownlist:
                        objdict[k].held = False

        screen.fill((200, 200, 200))
        for k in shownlist:
            if type(objdict[k]) == obj:
                # check if object is in range of holder
                if objdict["rectlol"].inself((objdict[k].getcenter()[0], objdict[k].getcenter()[1])):
                    objdict["rectlol"].addhold(objdict[k])
                else:
                    objdict["rectlol"].remhold(objdict[k])
                # check if object is being held by mouse
                if objdict[k].held:
                    objdict[k].setpos((x - objdict[k].holdpos[0], y - objdict[k].holdpos[1]))
                # blits where the object currently is (see method)
                objdict[k].blitself(screen)
            if type(objdict[k]) == objholder:
                objdict[k].fcalled = True
                if objdict[k].holding:
                    objdict[k].hold()
                    # fades in if it is in range (see method)
                    objdict[k].fadein(screen)

                else:
                    objdict[k].fadeout(screen)

        pygame.display.update()
        timedelta = clock.tick(250)

        timedelta /= 1000
        # print(clock.get_fps())


if __name__ == "__main__":
    main()
