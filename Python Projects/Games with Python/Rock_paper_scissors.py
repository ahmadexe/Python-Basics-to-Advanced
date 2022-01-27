import random
compno = random.randint (1,3)
userno = int(input("Pick rock(1), paper(2) or scissors(3): "))
if compno == 1:
    if userno == 1:
        print("You both picked rocks! It's a draw!")
    elif userno == 2:
        print("Computer picked rock, you picked Paper, YOU WIN!")
    elif userno == 3:
        print("Computer picked rock, you choose scissors, YOU LOSE!")
if compno == 2:
    if userno == 1:
        print("Computer picked paper, you picked rock, YOU LOSE")
    if userno == 2:
        print("You both picked paper. It's a draw!")
    if userno == 3:
        print("You picked scissors, computer picked papers. YOU WIN!")
if compno == 3:
    if userno == 1:
        print("Computer picked scissors, you picked rock, YOU WIN!")
    if userno == 2:
        print("You picked paper, computer picked scissors, YOU LOSE!")
    if userno == 3:
        print("You both picked scissors, It's a draw.")