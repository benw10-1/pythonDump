import pygame
import os


def clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)


def index(lst, i):
    h = 0
    for g in lst:
        if g == i:
            return h
        h += 1
    return -1


class AccelAnimation:
    def __init__(self, start, end, time):
        self.start = pygame.Vector2(start)
        self.end = pygame.Vector2(end)
        self.velocity = 0
        self.start_time = time
        self.time = time
        self.distance = self.start.distance_to(self.end)
        self.acceleration = self.distance / time / time
        self.current = self.distance

    def nextFrame(self, elapsed):
        self.time -= elapsed
        used = self.start_time - self.time
        if self.time <= 0:
            return self.end

        return self.start.lerp(self.end, (used * used * self.acceleration) / self.distance)


class Animation:
    def __init__(self, start, end, time):
        self.start = pygame.Vector2(start)
        self.end = pygame.Vector2(end)
        self.start_time = time
        self.time = time

    def nextFrame(self, elapsed):
        self.time -= elapsed

        if self.time <= 0:
            return self.end

        return self.end.lerp(self.start, self.time/self.start_time)


class Holder(object):
    def __init__(self, pos, dim, sep=65, background=None):
        self.held = []
        self.rect = pygame.Rect((0, 0), (dim[0], dim[1]))
        self.rect.center = pos
        self.sep = sep
        self.image = background

    def hold(self):
        for g in render.to_render:
            if self.rect.collidepoint(g.rect.center):
                self.add(g)
        side_space = (self.rect.width - (self.sep * (len(self.held) - 1))) / 2
        for i, g in enumerate(self.held):
            calc = [self.rect.x + side_space + (self.sep * i), self.rect.centery]
            calc = [int(_) for _ in calc]
            if calc != list(g.rect.center) and not g.selected and not g.animation:
                ani = AccelAnimation(g.rect.center, calc, .4)
                g.startAnimation(ani)

    def add(self, c):
        if type(c) == list:
            for g in c:
                if g.holder:
                    g.holder.held.remove(g)
                g.holder = self
                self.held.append(g)
        else:
            if c not in self.held:
                if c.holder:
                    c.holder.held.remove(c)
                c.holder = self
                self.held.append(c)


class Card(object):
    def __init__(self, name, image, pos, r=None, alt=None):
        self.name = name
        self.image = image
        self.alt = alt

        self.rect = pygame.Rect((0, 0), (image.get_width(), image.get_height()))
        self.rect.center = pos

        self.r = r

        if r:
            r.add(self)

        self.selected = False
        self.dMouse = [0, 0]
        self.alt_bool = False
        self.hand = None
        self.animation = None
        self.clickable = True

        self.holder = None

    def draw(self, surface):
        self.rect = self.rect.clamp(screen_rect)
        if self.alt_bool:
            surface.blit(self.alt, self.rect)
        else:
            surface.blit(self.image, self.rect)

    def startAnimation(self, animation):
        if not self.animation:
            self.animation = animation

    def animate(self):
        if self.animation:
            frame = self.animation.nextFrame(clock.get_time() / 1000)
            if frame == self.animation.end:
                self.animation = None
            self.move(frame)

    def move(self, pos):
        if type(pos) == pygame.Vector2:
            self.rect.center = (pos.x, pos.y)
        else:
            self.rect.center = pos

    def handleEvent(self, e):
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                if self.rect.collidepoint(e.pos) :
                    self.selected = True
                    if self.r:
                        self.r.foreground(self)
                    self.animation = None
                    self.dMouse = [self.rect.centerx - e.pos[0], self.rect.centery - e.pos[1]]
        if e.type == pygame.MOUSEBUTTONUP:
            self.selected = False

    def destroy(self):
        if self.r:
            self.r.remove(self)
        if self.holder:
            self.holder.held.remove(self)


class Renderer(object):
    def __init__(self, surface, to_render=[]):
        self.to_render = to_render
        self.backgrounds = []
        self.surface = surface

    def render(self):
        gameDisplay.blit(image_dict["table"], [0, 0])
        used = None
        for g in self.to_render:
            if g.selected:
                used = g
        if used:
            used.move([used.dMouse[0] + mPos[0], used.dMouse[1] + mPos[1]])
        self.to_render.sort(key=lambda z: (index(play_area.held, z), z.rect.centerx))
        self.foreground(used)
        for g in self.backgrounds[:]:
            if g.image:
                self.surface.blit(g.image, g.rect)
        for g in self.to_render[:]:
            g.animate()
            g.draw(self.surface)

    def add(self, obj):
        self.to_render.append(obj)

    def remove(self, obj):
        del self.to_render[self.to_render.index(obj)]

    def checkLast(self, obj):
        return obj == self.to_render[-1]

    def foreground(self, obj):
        for i, g in enumerate(self.to_render):
            if obj == g:
                del self.to_render[i]
                self.to_render.append(obj)
                break

    def handleEvents(self, e):
        for g in self.to_render[:]:
            if type(g) == Card:
                g.handleEvent(e)


if __name__ == "__main__":
    pygame.init()

    # colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    infoObject = pygame.display.Info()

    h_w = infoObject.current_h / infoObject.current_w

    height = 1320
    screen_dim = (height, int(1320 * h_w))
    print("Screen dim: ", screen_dim)
    screen_rect = pygame.Rect((0, 0), screen_dim)

    gameDisplay = pygame.display.set_mode(screen_dim)

    game = True
    clock = pygame.time.Clock()

    # gets path of assets folder
    path_ = os.path.join(os.getcwd(), "images")

    # initialize all images needed in a dict by name without "_large.png"
    image_dict = {}
    # TODO: scale images relative to screen
    for x in os.listdir(path_):
        image_dict[x.replace(".png", "").replace(".jpg", "")] = pygame.image.load(os.path.join("images", x)).convert()

    # vars for rendering and moving
    render = Renderer(gameDisplay)
    c1 = Card("blue_0", image_dict["blue_0"], [0, 0], render)
    c2 = Card("green_0", image_dict["green_0"], [0, 0], render)
    c3 = Card("blue_1", image_dict["blue_1"], [0, 0], render)
    c4 = Card("green_1", image_dict["green_1"], [0, 0], render)
    c5 = Card("blue_2", image_dict["blue_2"], [0, 0], render)
    c6 = Card("green_2", image_dict["green_2"], [0, 0], render)

    holder = Holder((int(screen_dim[0] / 2), int(screen_dim[1] - 91)), (screen_dim[0], int(screen_dim[1] * .2)), 85)
    holder.add(c1)

    play_area = Holder((screen_dim[0] / 2, screen_dim[1] / 2), (130, 182), 0, background=image_dict["blue_7"])
    play_area.add(c2)

    render.backgrounds.append(play_area)

    # game loop
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            render.handleEvents(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    for x in render.to_render:
                        print(x.rect.center)

        mPos = pygame.mouse.get_pos()

        if play_area.held:
            play_area.held[:]
        holder.hold()
        play_area.hold()

        render.render()
        pygame.display.flip()
        clock.tick(255)
