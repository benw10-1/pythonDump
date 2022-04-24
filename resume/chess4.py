import math
import time


def opposite_color(color):
    if color == "w":
        return "b"
    return "w"


"""class Piece:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.first = True

    def __str__(self):
        return self.color + self.name

    def __repr__(self):
        return self.color + self.name"""


class Game:
    def __init__(self):
        self.board = ["/", "/", "/", "/", "/", "/", "/", "/", "/", "/",
                      "/", "/", "/", "/", "/", "/", "/", "/", "/", "/",
                      None, None, None, None, None, None, None, None, "/", "/",
                      None, None, None, None, None, None, None, None, "/", "/",
                      None, None, None, None, None, None, None, None, "/", "/",
                      None, None, None, None, None, None, None, None, "/", "/",
                      None, None, None, None, None, None, None, None, "/", "/",
                      None, None, None, None, None, None, None, None, "/", "/",
                      None, None, None, None, None, None, None, None, "/", "/",
                      None, None, None, None, None, None, None, None, "/", "/"]

        self.moves = {"k": [-11, -10, -9, -1, 1, 9, 10, 11],
                      "q": [-11, -10, -9, -1, 1, 9, 10, 11],
                      "n": [-19, -21, 12, -8, 21, 19, 8, -12],
                      "b": [-11, 11, -9, 9],
                      "r": [-1, 1, -10, 10]}

        self.l_movers = ["q", "b", "r"]

        self.turn = "w"
        self.p_pieces = ["q", "n", "r", "b"]
        self.check = None

        self.min = 0
        self.max = 99
        self.last = None

        self.ranges = [range(20, 28), range(30, 38), range(40, 48), range(50, 58), range(60, 68), range(70, 78),
                       range(80, 88), range(90, 98)][::-1]

        self.kings = {}
        self.k_moved = {"w": False, "b": False}
        self.r_moved = {"w": {"left": False, "right": False}, "b": {"left": False, "right": False}}

    def get_y(self, pos):
        for i, x in enumerate(self.ranges):
            if pos in x:
                return i + 1

    def format_move(self, t, f, promote=None, castle=False, double=False, en_passant=False):
        return {"to": t, "from": f, "piece": self.board[f], "promotion": promote, "castle": castle, "double": double,
                "en_passant": en_passant}

    def get_reg_board(self):
        board = [[None] * 8 for x in range(0, 8)]
        for i, x in enumerate(self.ranges):
            for j, y in enumerate(x):
                board[j][i] = self.board[y]
        return board

    def move(self, move):
        # after check for castle
        if move["piece"] == "wk":
            self.kings["w"] = move["to"]
            self.k_moved["w"] = True
        if move["piece"] == "bk":
            self.kings["b"] = move["to"]
            self.k_moved["b"] = True

        # check if it is a rook
        if move["piece"] == "br" and move["from"] == 20:
            self.r_moved["b"]["left"] = True
        if move["piece"] == "br" and move["from"] == 27:
            self.r_moved["b"]["right"] = True
        if move["piece"] == "wr" and move["from"] == 100:
            self.r_moved["w"]["left"] = True
        if move["piece"] == "wr" and move["from"] == 107:
            self.r_moved["w"]["right"] = True

        # get en passant
        if move["en_passant"]:
            if move["piece"][1] == "w":
                self.board[move["to"] - 10] = None

        if move["castle"] == "k_castle":
            self.board[move["to"] - 1] = move["piece"][1] + "r"
            self.board[move["to"] + 1] = None
            self.r_moved[move["piece"][1]]["right"] = True

        if move["castle"] == "q_castle":
            self.board[move["to"] - 1] = move["piece"][1] + "r"
            self.board[move["to"] + 1] = None
            self.r_moved[move["piece"][1]]["left"] = True

        self.board[move["to"]] = move["piece"]
        self.board[move["from"]] = None
        self.last = move

    def setup_board(self):
        # white
        """for x in self.ranges[1]:
            self.board[x] = Piece("p", "w")
        for i, x in enumerate(self.ranges[0]):
            if i == 0:
                self.board[x] = Piece("r", "w")
            if i == 1:
                self.board[x] = Piece("n", "w")
            if i == 2:
                self.board[x] = Piece("b", "w")
            if i == 3:
                self.board[x] = Piece("q", "w")
            if i == 4:
                self.board[x] = Piece("k", "w")
                self.kings["w"] = x
            if i == 5:
                self.board[x] = Piece("b", "w")
            if i == 6:
                self.board[x] = Piece("n", "w")
            if i == 7:
                self.board[x] = Piece("r", "w")"""
        for x in self.ranges[1]:
            self.board[x] = "pw"
        for i, x in enumerate(self.ranges[0]):
            if i == 0:
                self.board[x] = "rw"
            if i == 1:
                self.board[x] = "nw"
            if i == 2:
                self.board[x] = "bw"
            if i == 3:
                self.board[x] = "qw"
            if i == 4:
                self.board[x] = "kw"
                self.kings["w"] = x
            if i == 5:
                self.board[x] = "bw"
            if i == 6:
                self.board[x] = "nw"
            if i == 7:
                self.board[x] = "rw"
        # black
        """for x in self.ranges[6]:
            self.board[x] = Piece("p", "b")
        for i, x in enumerate(self.ranges[7]):
            if i == 0:
                self.board[x] = Piece("r", "b")
            if i == 1:
                self.board[x] = Piece("n", "b")
            if i == 2:
                self.board[x] = Piece("b", "b")
            if i == 3:
                self.board[x] = Piece("q", "b")
            if i == 4:
                self.board[x] = Piece("k", "b")
                self.kings["b"] = x
            if i == 5:
                self.board[x] = Piece("b", "b")
            if i == 6:
                self.board[x] = Piece("n", "b")
            if i == 7:
                self.board[x] = Piece("r", "b")"""
        for x in self.ranges[6]:
            self.board[x] = "pb"
        for i, x in enumerate(self.ranges[7]):
            if i == 0:
                self.board[x] = "rb"
            if i == 1:
                self.board[x] = "nb"
            if i == 2:
                self.board[x] = "bb"
            if i == 3:
                self.board[x] = "qb"
            if i == 4:
                self.board[x] = "kb"
                self.kings["b"] = x
            if i == 5:
                self.board[x] = "bb"
            if i == 6:
                self.board[x] = "nb"
            if i == 7:
                self.board[x] = "rb"

    def get_all_legal_moves(self):
        moves = []

        for i, x in enumerate(self.board):
            if x and x != "/":
                name = x[0]
                color = x[1]
                if name in self.l_movers:
                    # gets all moves from previous list
                    for move in self.moves[name]:
                        val = i
                        val += move
                        # search through until hits wall or another piece
                        while self.max >= val >= self.min and self.board[val] != "/":
                            if self.board[val]:
                                if self.board[val][1] == color:
                                    break
                                # if it isn't same color add to moves still
                                moves.append(self.format_move(val, i))
                                break
                            # if nothing on space then add to move
                            moves.append(self.format_move(val, i))
                            val += move
                elif name == "p":
                    if color == "w":
                        # regular move
                        if not self.board[i - 10]:
                            moves.append(self.format_move(i - 10, i))
                            if self.get_y(i) == 2 and not self.board[i - 20]:
                                moves.append(self.format_move(i - 20, i, double=True))
                        # diagonal
                        if self.board[i - 9] and self.board[i - 9] != "/" and self.board[i - 9][1] != color:
                            moves.append(self.format_move(i - 9, i))

                        if self.board[i - 11] and self.board[i - 11] != "/" and self.board[i - 11][1] != color:
                            moves.append(self.format_move(i - 11, i))
                        # en passants, checking if the last move was a double pawn move
                        if self.last and self.last["double"]:
                            if self.last["to"] == i - 1 and self.board[i - 1] == "bp":
                                moves.append(self.format_move(i - 11, i, en_passant=True))

                        if self.last and self.last["double"]:
                            if self.last["to"] == i + 1 and self.board[i + 1] == "bp":
                                moves.append(self.format_move(i - 9, i, en_passant=True))
                        # check promotion
                        for o in moves:
                            if self.get_y(o["to"]) == 8:
                                moves.remove(o)
                                for k in self.p_pieces:
                                    o["promotion"] = k
                                    moves.append(o)

                    if color == "b":
                        if not self.board[i + 10]:
                            moves.append(self.format_move(i + 10, i))
                            if self.get_y(i) == 7 and not self.board[i + 20]:
                                moves.append(self.format_move(i + 20, i, double=True))
                        # diagonals
                        if self.board[i + 9] and self.board[i + 9] != "/" and self.board[i + 9][1] != color:
                            moves.append(self.format_move(i + 9, i))

                        if self.board[i + 11] and self.board[i + 11] != "/" and self.board[i + 11][1] != color:
                            moves.append(self.format_move(i + 11, i))

                        # en passants for black
                        if self.last and self.last["double"]:
                            if self.last["to"] == i - 1 and self.board[i - 1] == "wp":
                                moves.append(self.format_move(i + 9, i, en_passant=True))

                        if self.last and self.last["double"]:
                            if self.last["to"] == i + 1 and self.board[i + 1] == "wp":
                                moves.append(self.format_move(i + 11, i, en_passant=True))

                        for o in moves:
                            if self.get_y(o["to"]) == 8:
                                moves.remove(o)
                                for k in self.p_pieces:
                                    o["promotion"] = k
                                    moves.append(o)

                else:
                    for move in self.moves[name]:
                        val = i
                        val += move
                        if not self.max >= val >= self.min:
                            continue
                        if self.board[val] and self.board[val] != "/":
                            if self.board[val][1] == color:
                                continue
                        else:
                            moves.append(self.format_move(val, i))

                    # castle check
                    if x == "wk" and self.check != "w":
                        if not self.board[i + 1] and not self.board[i + 2] and not self.k_moved["w"] and not self.r_moved["w"]["right"]:
                            moves.append(self.format_move(i + 2, i, castle="k_side"))

                        if not self.board[i - 1] and not self.board[i - 2] and not self.board[i - 3] and not self.k_moved["w"] and not self.r_moved["w"]["left"]:
                            moves.append(self.format_move(i - 2, i, castle="q_side"))
                    # check if can castle
                    if x == "bk" and self.check != "b":
                        if not self.board[i + 1] and not self.board[i + 2] and not self.k_moved["w"] and not self.r_moved["w"]["right"]:
                            moves.append(self.format_move(i + 2, i, castle="k_side"))

                        if not self.board[i - 1] and not self.board[i - 2] and not self.board[i - 3] and not self.k_moved["w"] and not self.r_moved["w"]["left"]:
                            moves.append(self.format_move(i - 2, i, castle="k_side"))
        return moves


g = Game()
g.setup_board()
t1 = time.time_ns()
i = 0
while i < 10000:
    l_m = g.get_all_legal_moves()
    i += 1
"""for x in l_m:
    print(str(x["piece"]) + " to " + str(x["to"]) + " from " + str(x["from"]))"""
print(time.time_ns() - t1)
