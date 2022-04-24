import random

while True:
    limit = 0
    num = 3
    while limit < 3:
        input1 = input("Enter your guess"+str(limit+1)+": ")
        if input1 == "":
            continue
        guess = int(input1)
        if guess == num+1 or guess == num-1:
            print("So close!")
            limit = limit+1
            continue
        if guess == num:
            print("You have won the game!\n")
            input()
            break
        if guess > num:
            print("You're above the number")
            limit = limit + 1
        if guess < num:
            print("You're below the number")
            limit = limit + 1


    print("You lose!")
