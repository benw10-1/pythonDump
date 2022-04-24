import pygame
import os


def clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)


class Holder(object):
    def __init__(self, r):
        self.held = {}
        r.to_hold.append(self)

    def hold(self):
        for item in self.held:
            if item.rect.center != (
                    int(self.held[item][0]), int(self.held[item][1])) and not item.selected and not item.animated:
                item.startAnimation(self.held[item], 1)


class Hand(Holder):
    def __init__(self, dim, pos, r, sep=65, axis=1):
        super().__init__(r)
        pos = (pos[0] - dim[0] / 2, pos[1] - dim[1] / 2)
        self.rect = pygame.Rect(pos, dim)
        self.sep = clamp(sep, 0, self.rect.width)
        self.cards = []
        self.renderer = r
        self.axis = axis
        r.to_check.append(self)

    def update(self):
        count = len(self.cards)
        # calculate space needed on each side
        side_space = (self.rect.width - (self.sep * (count - 1)))/2
        self.cards = sorted(self.cards, key=lambda z: z.rect.centerx)
        # set position of each item within the holder
        gameDisplay.fill(white, self.rect)
        for i, item in enumerate(self.cards):
            # add center to it
            if self.axis == 1:
                sign = -1
            else:
                sign = 1
            self.held[item] = [self.rect.x + side_space + (self.sep * i), screen_dim[self.axis] + (sign * item.rect.height/2)]

    def add_card(self, c):
        if c.hand:
            c.hand.remove_card(c)
        self.cards.append(c)
        c.hand = self
        self.held[c] = [0, 0]
        self.update()

    def remove_card(self, c):
        del self.cards[self.cards.index(c)]
        c.hand = None
        del self.held[c]
        self.update()

    def check_card(self, c):
        if self.rect.collidepoint(c.rect.centerx, c.rect.centery) and c.hand != self:
            print("yer")
            if c.hand:
                c.hand.remove_card(c)
            self.add_card(c)


class Renderer(object):
    def __init__(self):
        self.to_draw = []
        self.to_animate = []
        self.to_hold = []
        self.to_check = []

    def render(self):
        for o in self.to_hold:
            o.hold()
        for o in self.to_animate:
            o.animate()
        for o in self.to_draw:
            o.draw()

    def push(self, ob):
        self.to_draw.append(ob)

    def ani_push(self, ob):
        self.to_animate.append(ob)

    def to_back(self, ob):
        del self.to_draw[self.to_draw.index(ob)]
        self.to_draw.append(ob)

    def check_card(self, c):
        for item in self.to_check:
            item.check_card(c)


class Clickable(object):
    def __init__(self, image, renderer, position=(0, 0), surface=None, alt=None):
        self.image = image
        self.alt = alt

        self.rect = pygame.Rect(position, (image.get_width(), image.get_height()))

        self.surface = surface

        self.hand = None
        self.selected = False
        self.dMouse = [0, 0]
        self.bool_alt = False

        self.animationStart = None
        self.animationEnd = None
        self.animationTime = None
        self.animationElapsed = None
        self.animated = False
        self.velocity = None

        self.renderer = renderer

        renderer.push(self)

    def draw(self, surface=None):
        if not surface:
            surface = self.surface
        if self.bool_alt:
            surface.blit(self.alt, self.rect)
        else:
            surface.blit(self.image, self.rect)

    def startAnimation(self, end_pos, time, regulated=False):
        # stops if regulated animation
        if self.animated:
            del self.renderer.to_animate[self.renderer.to_animate.index(self)]
            self.animated = False
            return
        self.animationStart = pygame.Vector2(self.rect.centerx, self.rect.centery)
        self.animationTime = self.animationElapsed = time
        self.animationEnd = pygame.Vector2(end_pos[0], end_pos[1])
        self.velocity = 0
        self.renderer.ani_push(self)
        self.animated = True

    def animate(self):
        if self.selected:
            del self.renderer.to_animate[self.renderer.to_animate.index(self)]
            self.animated = False
            return
        used_time = self.animationElapsed / self.animationTime
        # if time is less then zero then essentially break
        if used_time <= 0.0:
            self.rect.centerx = self.animationEnd.x
            self.rect.centery = self.animationEnd.y
        if self.rect.center == (int(self.animationEnd[0]), int(self.animationEnd[1])):
            del self.renderer.to_animate[self.renderer.to_animate.index(self)]
            self.animated = False
            return
        # get pos in between points with time

        lerped = self.animationEnd.lerp(self.animationStart, used_time)

        self.move([lerped.x, lerped.y])

        self.animationElapsed = round(self.animationElapsed - clock.get_time() / 1000 * self.velocity, 5)

        self.velocity += clock.get_time() / 1000 * acceleration

    def move(self, pos, center=True):
        if type(pos) != tuple and type(pos) != list:
            return
        if center:
            self.rect.center = (pos[0], pos[1])
        else:
            self.rect.x = pos[0]
            self.rect.y = pos[1]

    def event_handler(self, event_):
        if event_.type == pygame.MOUSEBUTTONDOWN:
            if event_.button == 1:
                if self.rect.collidepoint(event_.pos):
                    print("yer")
                    self.selected = True
                    self.dMouse = [self.rect.centerx - event_.pos[0], self.rect.centery - event_.pos[1]]
        if event_.type == pygame.MOUSEBUTTONUP:
            self.selected = False


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

    acceleration = 9.8

    # gets path of assets folder
    path_ = os.path.join(os.getcwd(), "images")

    # initialize all images needed in a dict by name without "_large.png"
    image_dict = {}
    # TODO: scale images relative to screen
    for x in os.listdir(path_):
        image_dict[x.replace(".png", "").replace(".jpg", "")] = pygame.image.load(os.path.join("images", x)).convert()

    # vars for rendering and moving
    render = Renderer()

    card = Clickable(image_dict["blue_0"], render, surface=gameDisplay, alt=image_dict["card_back"])
    card1 = Clickable(image_dict["blue_1"], render, surface=gameDisplay, alt=image_dict["card_back"])

    holder = Hand((screen_dim[0], int(screen_dim[1] * .2)), (int(screen_dim[0] / 2), int(screen_dim[1] - 91)), render, 85)
    holder.add_card(card1)
    holder.add_card(card)

    holder1 = Hand((130, 182), (screen_dim[0] / 2, screen_dim[1] / 2), render, 0)

    # game loop
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    for x in render.to_draw:
                        x.startAnimation([screen_dim[0] / 2, screen_dim[1] / 2], 1)
            for obj in render.to_draw:
                obj.event_handler(event)

        mPos = pygame.mouse.get_pos()

        gameDisplay.blit(image_dict["table"], [0, 0])
        last = None
        # get last selected obj (foreground)
        for obj in render.to_draw:
            render.check_card(obj)
            if obj.selected:
                last = obj
        for obj in render.to_draw:
            if obj != last:
                obj.selected = False
        if last:
            gameDisplay.fill(white, last.hand.rect)
            last.move([last.dMouse[0] + mPos[0], last.dMouse[1] + mPos[1]])
            last.hand.update()

        # if there is a selected then move accordingly and move to back(foreground)

        render.render()

        pygame.display.flip()
        clock.tick(255)

    pygame.quit()
    quit()
