book = ["fourty rules of love", "fourty rules of love", "notebook", "notebook", "notebook", "the best of me", "a walk to remember", "subtle art of not giving a fuck"]
while True:
    menu = '''Welcome to Jinnah Libarary
    1. View Books.
    2. Purchase a book.
    3. Issue a book.
    4. Return a book.
    5. Leave a review
    6. Exit'''
    print(menu)
   
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(book)
    elif choice == 2:
        try:
            p = input("Enter the name of book you want to purchase: ").lower()
            book.remove(p)
            print("Purchase complete, please pay the cash")
        except ValueError as e:
            print("The book isnt available")
    elif choice == 3:
        name = input("Enter your name: ")
        doi = input("Enter the date: ")
        

        try:
            i = input("Enter the name of book you want: ").lower()
            book.remove(i)
            print("Please return in 15 days")
        except ValueError as e:
            print("The book is not available")
        f = open("records.txt", "w")
        f.write(f"{name}, {doi}, {i}")3
        f.close()
    elif choice == 4:
        r = input("Enter the name of book you want to return: ").lower()
        book.append(r)
        print("Thank's for returning the book.")
    elif choice == 5:
        rev = input("How was your experience: ")
        f = open("rev.txt", "w")
        f.write(rev)
        f.close()
        print("Thanks!")
    elif choice == 6:
        break

print("Thanks for using.")   