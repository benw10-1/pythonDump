door = 6930903
card = 19716708

subject_number = 7


def operate(number, subject_num):
    holder = 1
    loop_size = 0

    while holder != number:
        holder *= subject_num
        holder %= 20201227
        loop_size += 1

    return loop_size


door_loop = operate(door, subject_number)
card_loop = operate(card, subject_number)
hold = 1

while door_loop > 0:
    hold *= card
    hold %= 20201227
    door_loop -= 1

d_enc = hold
hold = 1

while card_loop > 0:
    hold *= door
    hold %= 20201227
    card_loop -= 1
c_enc = hold

print(d_enc, c_enc)

