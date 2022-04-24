import math
import numpy as np
from array import array
import itertools
import string
import concurrent.futures

with open("outputs/output5.txt", "r") as file:
    text = file.read().strip()

split = text.split("\n\n")
p1_cards = list(map(int, split[0].split("\n")[1:]))
p2_cards = list(map(int, split[1].split("\n")[1:]))

while True:
    try:
        if p1_cards[0] > p2_cards[0]:
            s = p1_cards[0]
            del p1_cards[0]
            p1_cards.append(s)
            p1_cards.append(p2_cards[0])
            del p2_cards[0]
        if p1_cards[0] < p2_cards[0]:
            s = p2_cards[0]
            del p2_cards[0]
            p2_cards.append(s)
            p2_cards.append(p1_cards[0])
            del p1_cards[0]
    except IndexError:
        break

if p1_cards:
    cards = p1_cards
else:
    cards = p2_cards

total = 0
print(cards)
for i, x in enumerate(cards[::-1]):
    total += (i + 1) * x

print(total)


# day 24
"""tiles = {}

for line in split:
    temp = list(line)
    holder = []
    ign = False
    store = ""
    x = y = 0

    for i, char in enumerate(line):
        if not ign:
            if store:
                holder.append(store)
            if char == "s" or char == "n":
                ign = True
            store = char

        else:
            ign = False
            store += char
    holder.append(store)

    for item in holder:
        if len(item) == 2:
            for g in item:
                if g == "s":
                    y -= 1
                if g == "e":
                    x += 1
                if g == "n":
                    y += 1
                if g == "w":
                    x -= 1
        else:
            if item == "e":
                x += 1
            if item == "w":
                x -= 1

    strg = str(x) + "," + str(y)

    try:
        tiles[strg] += 1
    except KeyError:
        tiles[strg] = 1

black = []
for key in tiles:
    if tiles[key] % 2 == 1:
        black.append(list(map(int, key.split(","))))
print(len(black))
iter_count = 0
adjacent = [[1, 1], [-1, -1], [1, -1], [-1, 1], [1, 0], [0, 1]]
for _ in range(100):
    to_remove = []
    to_add = []
    to_check = []

    for x in black:
        adj = 0
        for p in adjacent:
            used = [x[0] + p[0], x[1] + p[1]]
            if used in black:
                adj += 1
            else:
                to_check.append(used)
            iter_count += 1
        if adj == 0 or adj > 2:
            to_remove.append(x)

    for x in to_check:
        adj1 = 0
        for p in adjacent:
            u = [x[0] + p[0], x[1] + p[1]]
            if u in black:
                adj1 += 1
            iter_count += 1
        if adj1 == 2:
            to_add.append(x)

    for x in to_remove:
        black.remove(x)
    for x in to_add:
        black.append(x)
    print(len(black))


print(len(black))"""

# day 20
"""tiles = {}
poses = {}
orientations = {}

for x in split:
    tile = []
    for y in x.split("\n"):
        if ":" in y: name = y.split(" ")[1][:-1]

        else:
            tile.append(list(y))

    tiles[name] = tile


def rotated(arr2d):
    return [list(g) for g in zip(*arr2d[::-1])]


def line_by_line(arr):
    for line in arr:
        print("".join(list(line)))


# iterate through each tile, essentially get a list of all of the adjacent tiles and then put them together after
# 1951 - 2311 - 3079
for key_1 in tiles:
    tile = tiles[key_1]
    poses[key_1] = []
    orientations[key_1] = {}
    for __ in range(4):
        top = tile[0]
        bot = tile[-1]
        left = [l[0] for l in tile]
        right = [r[-1] for r in tile]
        lists = [top, bot, left, right]
        for key_2 in tiles:
            r = tiles[key_2]
            if key_2 == key_1: continue

            top_r = r[0]
            bot_r = r[-1]
            left_r = [l_r[0] for l_r in r]
            right_r = [r_r[-1] for r_r in r]

            if top_r in lists or bot_r in lists or left_r in lists or right_r in lists:
                poses[key_1].append(key_2)
        tile = rotated(tile)

    # poses[key_1] = list(set(poses[key_1]))

print(poses)

total = 1

for x in poses:
    if len(poses[x]) == 2:
        total *= int(x)

print(total)"""

# day 19
"""top, bot = text.split("\n\n")

rules = {}

for rule in top.split("\n"):
    splt = rule.split(": ")
    rules[splt[0]] = splt[1]

same = 0
different = 0


def check_condition(r_n):
    for x in rules """

# day 17
"""x = 0
y = 0
z = 0

actives = []

a = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
perms = list(set(itertools.permutations(a, 3)))
perms.remove((0, 0, 0))

for y, row in enumerate(split):
    for x, item in enumerate(row):
        if item == "#":
            actives.append([x, y, 0])
for k in range(3):
    to_check = []
    to_add = []
    to_rem = []
    for active in actives[:]:
        x = active[0]
        y = active[1]
        z = active[2]
        a_n = 0

        for t_a in perms:
            t_x = x + t_a[0]
            t_y = y + t_a[1]
            t_z = z + t_a[2]

            if [t_x, t_y, t_z] in actives:
                if [t_x, t_y, t_z] == [x, y, z]:
                    continue
                a_n += 1
            elif [t_x, t_y, t_z] not in to_check:
                to_check.append([t_x, t_y, t_z])

        if not (a_n == 2 or a_n == 3):
            to_rem.append(active)

    for check in to_check[:]:
        x = check[0]
        y = check[1]
        z = check[2]
        a_n = 0

        for t_a in perms:
            t_x = x + t_a[0]
            t_y = y + t_a[1]
            t_z = z + t_a[2]

            if [t_x, t_y, t_z] in actives:
                a_n += 1

        if a_n == 3:
            to_add.append(check)

    for x in to_rem:
        actives.remove(x)

    for x in to_add:
        actives.append(x)

print(len(actives))"""
