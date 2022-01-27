import random
lotteryno1 = random.randint(1,9)
lotteryno2 = random.randint(1,9)
no1 = int(input("Enter the first number.\n"))
no2 = int(input("Enter the second number.\n"))
if no1 == lotteryno1 and no2 == lotteryno2:
    print("GG! You just won $10,000")
elif no1 == lotteryno2 and no2 == lotteryno1:
    print("So close! Just with the wrong order you won $3,000")
elif no1 == lotteryno1 or no1 == lotteryno2 or no2 == lotteryno1 or no2 == lotteryno2:
    print("One of your number matches the lottery number! You won $1,000.")
else:
    print("Better luck next time.")