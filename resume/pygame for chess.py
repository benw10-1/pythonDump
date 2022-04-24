import threading
import string
import pygame as pygame
import queue
import chess
import sys
import random

sys.setrecursionlimit(10 ** 5)

white, black, red, soft_white, b_green, h_blue, l_blue = (255, 255, 255), (0, 0, 0), (255, 0, 0), (211, 211, 211), (
    31, 97, 0), (100, 170, 255), (68, 85, 110)
empty = pygame.Color(0, 0, 0, 0)
ab = string.ascii_uppercase
squares = []
visited = {}
zobTable = [[[random.randint(1,2**64 - 1) for i in range(13)]for j in range(8)]for k in range(8)]


def reverse(li):
    reved = []
    p = 7
    for i, x in enumerate(li):
        reved.append(li[i + p])
        if p == -7:
            p = 9
        p -= 2
    return reved


total = 0

pieces = []
spaces = {"a8": None, "b8": None, "c8": None, "d8": None, "e8": None, "f8": None, "g8": None, "h8": None,
          "a7": None, "b7": None, "c7": None, "d7": None, "e7": None, "f7": None, "g7": None, "h7": None,
          "a6": None, "b6": None, "c6": None, "d6": None, "e6": None, "f6": None, "g6": None, "h6": None,
          "a5": None, "b5": None, "c5": None, "d5": None, "e5": None, "f5": None, "g5": None, "h5": None,
          "a4": None, "b4": None, "c4": None, "d4": None, "e4": None, "f4": None, "g4": None, "h4": None,
          "a3": None, "b3": None, "c3": None, "d3": None, "e3": None, "f3": None, "g3": None, "h3": None,
          "a2": None, "b2": None, "c2": None, "d2": None, "e2": None, "f2": None, "g2": None, "h2": None,
          "a1": None, "b1": None, "c1": None, "d1": None, "e1": None, "f1": None, "g1": None, "h1": None}

spaces_ar = ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",
             "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
             "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
             "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
             "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
             "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
             "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
             "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]

p_eval = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
          5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
          1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0,
          0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5,
          0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0,
          0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5,
          0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5,
          0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

n_eval = [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
          -4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0,
          -3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0,
          -3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0,
          -3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0,
          -3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0,
          -4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0,
          -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]

b_eval = [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
          -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
          -1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0,
          -1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0,
          -1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0,
          -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0,
          -1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0,
          -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]

r_eval = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
          0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
          -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
          -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
          -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
          -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
          -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
          0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0]

q_eval = [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
          -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
          -1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
          -0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
          0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
          -1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
          -1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0,
          -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]

k_eval = [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
          -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
          -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
          -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
          -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
          -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
          2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0,
          2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0]

evals = {"♚": reverse(k_eval), "♛": reverse(q_eval), "♜": reverse(r_eval), "♝": reverse(b_eval), "♞": reverse(n_eval),
         "♟": reverse(p_eval), "♙": p_eval, "♘": n_eval, "♗": b_eval, "♖": r_eval,
         "♕": q_eval, "♔": k_eval, "⭘": [0] * 64}

indices = {"♚": -200, "♛": -9, "♜": -5, "♝": -3, "♞": -3, "♟": -1, "♙": 1, "♘": 3, "♗": 3, "♖": 5,
           "♕": 9, "♔": 200, "⭘": 0}

hash_indeces = {"♚": 0, "♛": 1, "♜": 2, "♝": 3, "♞": 4, "♟": 5, "♙": 6, "♘": 7, "♗": 8, "♖": 9,
           "♕": 10, "♔": 11, "⭘": -1}


def eval_board(w):
    unicode = board.unicode()
    i = 0
    total_ = 0
    for row in unicode.split("\n"):
        for space in row.split():
            pos_eval = evals[space][i]
            if indices[space] < 0:
                pos_eval *= -1
            total_ += indices[space] + pos_eval
            i += 1
    if w:
        return total
    return -total


def get_center(_img):
    return _img.get_rect().center


class Space:
    def __init__(self, pos, size, color, surface, space):
        self.size = size
        self.color = color
        self.pos = pos
        self.surface = surface
        self.space = space
        self.left_x = int(pos[0])
        self.top_y = int(pos[1])
        self.right_x = int(pos[0] + size)
        self.bottom_y = int(pos[1] + size)
        self.holding = None
        self.center = [pos[0] + size / 2, pos[1] + size / 2]
        spaces[space] = self

    def highlight(self):
        highlighted.append([int(self.pos[0]), int(self.pos[1])])

    def unhighlight(self):
        global highlighted
        highlighted = []

    def is_in(self, pos):
        if self.left_x < pos[0] < self.right_x:
            if self.bottom_y > pos[1] > self.top_y:
                return True
        return False

    def start_holding(self, piece):
        piece.holder = self
        self.holding = piece

    def stop_holding(self):
        self.holding.holder = None
        self.holding = None


class Piece:
    def __init__(self, space, surface, _image, color, name):
        self.space = space
        self.surface = surface
        self.legal = []
        spaces[space].start_holding(self)
        self.image = _image
        self.size = _image.get_rect().size
        self.pos = [0, 0]
        self.held = False
        self.og = [0, 0]
        self.color = color
        self.name = name

    def add_legal(self, moves):
        self.legal = moves

    def highlight_legal(self):
        for x in self.legal:
            spaces[x].highlight()
        self.holder.highlight()

    def unhighlight_legal(self):
        for x in self.legal:
            spaces[x].unhighlight()
        self.holder.unhighlight()

    def move_rel_center(self, center):
        self.pos = [round(center[0] - self.size[0] / 2), round(center[1] - self.size[1] / 2)]

    def make_move(self, f, t, bot_=False, mock=False):
        move_ = f + t
        global turn
        if spaces[t].holding:
            spaces[t].holding.del_self()
        if not bot_:
            try:
                if spaces[move_[0:2]].holding.name == "k":
                    if spaces_ar[spaces_ar.index(move_[0:2]) + 2] == move_[2:4]:
                        spaces["h" + move_[1]].holding.make_move("h" + move_[1], "f" + move_[1], mock=True)
                    if spaces_ar[spaces_ar.index(move_[0:2]) - 2] == move_[2:4]:
                        spaces["a" + move_[1]].holding.make_move("a" + move_[1], "d" + move_[1], mock=True)
            except Exception as e:
                print("except: " + str(e))
            if not mock:
                board.push_uci(move_)
                turn = bt
            spaces[move_[0:2]].stop_holding()
            self.og = self.pos
            spaces[move_[2:4]].start_holding(self)

        else:
            try:
                if spaces[move_[0:2]].holding.name == "k":
                    if spaces_ar[spaces_ar.index(move_[0:2]) + 2] == move_[2:4]:
                        spaces["h" + move_[1]].holding.make_move("h" + move_[1], "f" + move_[1], mock=True)
                    if spaces_ar[spaces_ar.index(move_[0:2]) - 2] == move_[2:4]:
                        spaces["a" + move_[1]].holding.make_move("a" + move_[1], "d" + move_[1], mock=True)
            except IndexError:
                pass
            spaces[move_[0:2]].stop_holding()
            self.og = self.pos
            spaces[move_[2:4]].start_holding(self)

    def animated(self, _pos, time):
        _pos = [round(_pos[0]), round(_pos[1])]
        center = [round(self.pos[0] + self.size[0] / 2), round(self.pos[1] + self.size[1] / 2)]
        a_frames = time / timedelta
        d_x = abs(round(_pos[0]) - round(self.og[0]))
        d_y = abs(round(_pos[1]) - round(self.og[1]))
        if d_x < 15:
            d_x = 15
        if d_y < 15:
            d_y = 15
        x_inc = d_x / a_frames
        y_inc = d_y / a_frames
        if _pos != center:
            if _pos[0] < center[0]:
                self.pos[0] -= x_inc
            if _pos[0] > center[0]:
                self.pos[0] += x_inc
            if _pos[1] < center[1]:
                self.pos[1] -= y_inc
            if _pos[1] > center[1]:
                self.pos[1] += y_inc

        if _pos[0] + x_inc * 1.5 > center[0] > _pos[0] - x_inc * 1.5 and _pos[1] + y_inc * 1.5 > center[1] > _pos[
            1] - y_inc * 1.5:
            self.pos = [_pos[0] - self.size[0] / 2, _pos[1] - self.size[1] / 2]
            self.og = self.pos

    def back_to_holder(self):
        self.animated(self.holder.center, .05)

    def blit_self(self):
        n_rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.surface.blit(self.image, n_rect)

    def del_self(self):
        pieces.remove(self)
        self.holder.stop_holding()


def parse_space(space):
    return ab[space[0]] + str(space[1])


def create_board(start_pos, size, surface):
    x = start_pos[0]
    y = start_pos[1]
    i, g, p, total = 0, 0, 0, 0
    while True:
        if i == 8:
            i = 0
            p += 1
            y += size
            x = _x
            if g == 1:
                g = 0
            else:
                g = 1
        if p == 8:
            break

        rect = pygame.Rect(x, y, size, size)
        if g == 1:
            color = b_green
            g -= 1
        else:
            color = soft_white
            g += 1
        Space([x, y], size, color, surface, spaces_ar[total])
        pygame.draw.rect(surface, color, rect)
        i += 1
        x += size

        squares.append(rect)

        total += 1
        pygame.display.flip()


def redraw_board(surface):
    g = 0
    i = 0
    for x in squares:
        i += 1
        if g == 1:
            color = b_green
            g -= 1
        else:
            color = soft_white
            g += 1
        if list(x.topleft) in highlighted:
            if color == soft_white:
                color = h_blue
            else:
                color = l_blue
        if i == 8:
            i = 0
            if g == 1:
                g = 0
            else:
                g = 1

        pygame.draw.rect(surface, color, x)


def init_pieces(surface):
    bp = pygame.image.load("images/bpawn.png")
    bk = pygame.image.load("images/bking.png")
    bn = pygame.image.load("images/bknight.png")
    bb = pygame.image.load("images/bbishop.png")
    bq = pygame.image.load("images/bqueen.png")
    br = pygame.image.load("images/brook.png")
    wb = pygame.image.load("images/wbishop.png")
    wk = pygame.image.load("images/wking.png")
    wn = pygame.image.load("images/wknight.png")
    wp = pygame.image.load("images/wpawn.png")
    wq = pygame.image.load("images/wqueen.png")
    wr = pygame.image.load("images/wrook.png")

    for space in spaces_ar[8:16]:
        p = Piece(space, surface, bp, "b", "p")
        pieces.append(p)
    for space in spaces_ar[48:56]:
        p = Piece(space, surface, wp, "w", "p")
        pieces.append(p)
    for i, space in enumerate(spaces_ar[56:64]):
        if i == 0 or i == 7:
            p = Piece(space, surface, wr, "w", "r")
        if i == 1 or i == 6:
            p = Piece(space, surface, wn, "w", "n")
        if i == 2 or i == 5:
            p = Piece(space, surface, wb, "w", "b")
        if i == 3:
            p = Piece(space, surface, wq, "w", "q")
        if i == 4:
            p = Piece(space, surface, wk, "w", "k")
        pieces.append(p)
    for i, space in enumerate(spaces_ar[0:8]):
        if i == 0 or i == 7:
            p = Piece(space, surface, br, "b", "r")
        if i == 1 or i == 6:
            p = Piece(space, surface, bn, "b", "n")
        if i == 2 or i == 5:
            p = Piece(space, surface, bb, "b", "b")
        if i == 3:
            p = Piece(space, surface, bq, "b", "q")
        if i == 4:
            p = Piece(space, surface, bk, "b", "k")
        pieces.append(p)


# def quiesce_search(alpha, beta, moving):
#     standing_pat = eval_board(moving)
#
#     if standing_pat >= beta:
#         return beta
#
#     if alpha < standing_pat:
#         alpha = standing_pat
#
#     captures = [m.uci() for m in board.generate_legal_captures()]
#
#     for cap in captures:
#         board.push_uci(cap)
#         evaluation = -quiesce_search(-beta, -alpha, -moving)
#         board.pop()
#
#         if evaluation >= beta:
#             return beta
#
#         if evaluation > alpha:
#             alpha = evaluation
#
#     return alpha


def random_arr():
    return [[[random.randint(1, 2 ** 64 - 1) for i in range(12)] for j in range(8)] for k in range(8)]


def alpha_beta(alpha, beta, depth, max_player):
    if depth == 0:
        return eval_board(not max_player)

    moves = [mo.uci() for mo in board.generate_legal_moves()]

    if max_player:
        branch = -float('inf')
        for move in moves:
            board.push_uci(move)
            branch = max(branch, alpha_beta(alpha, beta, depth - 1, False))
            board.pop()

            if branch >= beta:
                break
            alpha = max(alpha, branch)
        return branch
    else:
        branch = float('inf')
        for move in moves:
            board.push_uci(move)
            branch = min(branch, alpha_beta(alpha, beta, depth - 1, True))
            board.pop()

            if branch <= alpha:
                break
            beta = min(beta, branch)
        return branch


def computeHash(b, d):
    unicode = b.unicode()
    h = 0
    for i in range(8):
        for j in range(8):
            if unicode[i][j] != '⭘':
                p = hash_indeces[unicode[i][j]]
                h ^= zobTable[i][j][p]
    h ^= int(b.turn() == chess.BLACK)
    return h


def bot():
    d = 3
    global turn
    while True:
        if turn == bt:
            if board.is_checkmate() or board.can_claim_draw():
                print("gg")
                break
            best_move = ""
            best_eval = -1000
            move_list = [m.uci() for m in board.generate_legal_moves()]
            for move in move_list:
                board.push_uci(move)
                eval_ = alpha_beta(-float('inf'), float('inf'), d, True)
                board.pop()
                if eval_ >= best_eval:
                    best_move = move
                    best_eval = eval_

            board.push_uci(best_move)
            boardQueue.put([best_move])
            turn = player


if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode((500, 500))

    board = chess.Board()

    player = "w"
    bt = "b"

    if bt == "b":
        bf = -1
    else:
        bf = 1

    turn = "w"

    pygame.display.set_caption("ChessBoard")

    boardQueue = queue.Queue()

    holding = False
    gameExit = False
    found = False
    update = False
    done = False
    p_update = False
    highlighted = []

    clock = pygame.time.Clock()
    rect = pygame.Rect(0, 0, gameDisplay.get_width(), gameDisplay.get_height())
    pygame.draw.rect(gameDisplay, white, rect)
    # height / width ratio
    ratio = gameDisplay.get_height() / gameDisplay.get_width()

    # start of board
    _x = 30
    _y = _x * ratio
    # so squares can be relative to image size
    img = pygame.image.load('images/bbishop.png')
    create_board([_x, _y], img.get_size()[1] + 5, gameDisplay)
    # initialize pieces
    init_pieces(gameDisplay)
    pygame.display.flip()
    timedelta = .005
    # initial fill
    gameDisplay.fill(white)
    redraw_board(gameDisplay)
    pygame.display.flip()
    botThread = threading.Thread(target=bot, daemon=True)
    botThread.start()

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check if already holding down mouse
                if not holding:
                    pos = pygame.mouse.get_pos()
                    holding = True
                    held = None
                    for x in spaces:
                        # if mouse is in a square with a piece in it
                        if spaces[x].is_in(pos):
                            if spaces[x].holding:
                                # puts it as the last thing drawn
                                pieces.remove(spaces[x].holding)
                                pieces.append(spaces[x].holding)
                                spaces[x].holding.held = True
                                spaces[x].holding.highlight_legal()
                                held = spaces[x].holding
                                break

            if event.type == pygame.MOUSEBUTTONUP:
                holding = False
                if held:
                    mouse_pos = pygame.mouse.get_pos()
                    held.og = mouse_pos
                    # if space is in the previous spaces legal moves
                    for x in spaces:
                        if spaces[x].is_in(mouse_pos):
                            if x in held.legal:
                                held.make_move(held.holder.space, x)
                    held.held = False

                    held.unhighlight_legal()
                    held = None
        # draw each frame
        gameDisplay.fill(white)
        redraw_board(gameDisplay)

        if turn == bt:
            if f:
                f = not f
                p_update = True
            found = False
        if turn == player and not found:
            # get uci of each move in Move format
            l_moves = [x.uci() for x in board.generate_legal_moves()]
            found = True
            update = True
            f = True
        for piece in pieces:
            # if update then reset legal moves
            if update or p_update:
                piece.legal = []
            if not piece.held:
                piece.back_to_holder()
            else:
                piece.move_rel_center(pygame.mouse.get_pos())
            piece.blit_self()

        if p_update:
            p_update = False

        if update:
            update = False
            for x in l_moves:
                spaces[x[0:2]].holding.legal.append(x[2:4])

        if boardQueue.qsize():
            r = boardQueue.get()
            f = r[0][0:2]
            t = r[0][2:4]
            spaces[f].holding.make_move(f, t, True)
            turn = player

        timedelta = clock.tick(250)

        timedelta /= 1000

        pygame.display.flip()
