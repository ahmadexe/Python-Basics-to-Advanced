
while(True):
    print("Press Q to quit!")
    n = input("Enter a number: ")
    if n == 'q' or 'Q' :
        break
    try:
        n = int(n)
        if n > 5:
            print("Your Number is greater than 5")
        else:
            print("Your number is smaller than 5")
    except Exception as e:
        print("An error occured. Try again. Make sure you are entering a number.")
    
    

print("Thanks for playing!")
