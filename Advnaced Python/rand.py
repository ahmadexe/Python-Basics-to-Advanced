while True:
    print("Enter Q to exit")
    a = input("Enter a number: ")
    if a == "q":
        break


    try:
        a = int(a)
        if a > 5:
            print("Your number is greater than 5")
        elif a < 5:
            print("Your number is smaller than 5")
    except Exception as e:
        print("Sorry Try again.")

print("Thanks for playing")

    