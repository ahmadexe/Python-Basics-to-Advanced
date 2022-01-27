import random
#1 = Rock
# 2 = paper
# 3 = scissors
compno = random.randint(1,3)
userno = int(input("Press 1 to choose rock, 2 to choose paper and 3 to choose scissors: "))
if compno == 1:
    if userno == 1:
        print("It's a draw!")
    if userno == 2:
        print("You Win")
    if userno == 3:
        print("You Lose")
if compno == 2:
    if userno == 1:
        print("You Lose")
    if userno == 2:
        print("It's a draw")
    if userno == 3:
        print("You Win")
if compno == 3:
    if userno == 1:
        print("You win")
    if userno == 2:
        print("You lose")
    if userno == 3:
        print("It's a draw")