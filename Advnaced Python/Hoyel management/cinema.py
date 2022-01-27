seats = [1,2,3,34,54,6,56,89,90]
movies = ['Titanic', 'Shawshank Redemption', 'Django Unchained', 'Wolf Of Wall The Wall Street ']
while True:
    print(
    '''
    1. View Seats.
    2. Book Seats
    3. View Movies
    4. Book a Movie
    5. Select Payment method
    6. Exit()
    '''
    )

    c = int(input("Enter your choice: "))
    if c == 1:
        for item in seats:
            print(item)
    if c == 2:
        a = int(input("Enter the seat you want: "))
        seats.remove(a)
        print("Seat is booked!")
    if c == 3:
        for item in movies:
            print(item)
    if c == 4:
        b = str(input("Enter the name of movie: ")).title()
        movies.remove(b)
        print("Thank you!")
    if c == 5:
        p = str(input("Enter the mode of payment: "))
        if p == 'Cash':
            print("Pay at the counter.")
        if p == 'Card':
            q = int(input("Enter card number: "))
            print("Thank you!")
    if c == 6:
        exit()