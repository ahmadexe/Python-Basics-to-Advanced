print("*Rent a car managment system*")
cars=["civic","land cruiser","Mercedes S Class"]

print('Please Login to Access Dashboard')
username=input("Enter the username: ")
password=eval(input('Enter the password: '))
name="faizan"
if username==str(name) and password==123:
    while True:
        print(
        '''
        1. Search_car
        
        2. Reservation
       
        3. Your Booking Detail
        4. Select Payment method
        5. Exit()
        '''
        )

        input_1 = int(input("Enter your choice:"))
        if input_1 == 1:
            for item in cars:
                print(item)
            
        if input_1 == 2:
            q = str(input("Enter the name of car you want: "))
            if q in cars:
                cars.remove(q)
                print("Car booked!")
            else:
                print("Car not booked.")

        if input_1==3:
            Reservation=input(print("Reservation"))
            Name=input('Enter your Name:')
            Phone=input('Enter Phone Number: ')
            Cnic=int(input('Enter your Cnic Number: '))
            days=int(input("For How many day's you want to book the car: "))
            class_1=input('''Which class you want:
                    1. Economy class
                    2. Business Class
                    3. Luxary Class
                    Enter your choice:  ''')
            print("Your details has been successfully Entered. ")
        

        
              
        if input_1 == 4:
            w = str(input("Would you like to pay cash or use card: "))
            print(f"The user has decided to pay via {w}.")

        if input_1 == 5:
            break

print("Thanks for using.")