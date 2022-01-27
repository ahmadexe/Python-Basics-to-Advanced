import random
compno = random.randint(1,10)
userno = 0
while userno != compno:
    userno = int(input("Enter your guess\n"))
    if userno == compno:
        print("Your guess is right!")
    elif userno > compno:
        print("Guess somethimg a little lower.")
    elif userno < compno:
        print("Guess something a little higher.")