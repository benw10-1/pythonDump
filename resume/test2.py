import chess
import time

board = chess.Board()
temp = []
board.push_uci("e2e4")
board.push_uci("e7e5")
board.push_uci("f1c4")
board.push_uci("f8e7")
board.push_uci("g1f3")
board.push_uci("b7b6")
board.push_uci("c4f7")
board.push_uci("e8f7")

q_eval = [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
          -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
          -1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
          -0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
          0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
          -1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
          -1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0,
          -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]


def reverse(li):
    reved = []
    p = 7
    for i, x in enumerate(li):
        reved.append(q_eval[i + p])
        if p == -7:
            p = 9
        p -= 2
    return reved
