#menu
print('''

--- press '1' for admin mode
--- press '2' for user mode
--- press '3' exit
''' )
username = "admin"
Password = "admin1"
Selection = int(input("enter which mode you want to use: "))
if Selection == 1:


    while True:

        username1 = input("Enter your Username: ")

        if username1 == username:
            break
        else:
            print("the username you entered is incorrect")
    while True:
        password1 = input("Enter your Password: ")

        if password1 == Password:
            break
        else:
            print("the password you entered is incorrect")
            print("\nYou have successfully logged into your account!")

    while True:
        # Admin modules#
        print("-----------------------------------------")
        print(
            "|To manage patients Enter 1 \nTo manage doctors Enter 2  \nFor appointments Enter 3|")
        print("-----------------------------------------")
        AdminOptions = int(input("Enter your choice : "))

        if AdminOptions == 1:
            print("|To add new patient Enter 1	  	|")
            print("|To display patient Enter 2	  	|")
            print("-----------------------------------------")
            Admin_choice = int(input("Enter your choice : "))

            if Admin_choice == 1:
                patientID = int(input("Enter patient ID: "))
                Department = input("Enter patient department: ")
                DoctorName = input("Enter name of doctor following the case:  ")
                name = input("Enter patient name:  ")
                Age = input("Enter patient age:  ")
                Gender = input("Enter patient gender:  ")
                Address = input("Enter patient address:  ")
                RoomNumber = input("Enter patient room number:  ")
                f = open('patientinformationall.txt', 'a')
                f.write(f'''
    ==============================================================================
        PatientID:      {patientID }
        Department:     {Department} 
        Name:           {name}
        Doctor:         {DoctorName}
        Age:            {Age}
        Gender:         {Gender}
        Address:        {Address}
        RoomNumber:     {RoomNumber}
    ==============================================================================
''')
                f.close()
                g = open('patientinformation.txt', 'w')
                g.write(f'''
    ==============================================================================
        PatientID:      {patientID }
        Department:     {Department} 
        Name:           {name}
        Doctor:         {DoctorName}
        Age:            {Age}
        Gender:         {Gender}
        Address:        {Address}
        RoomNumber:     {RoomNumber}
    ==============================================================================
''')
                g.close()
                print("----------------------Patient added successfully----------------------")

            if Admin_choice == 2:
                f = open('patientinformation.txt', 'r')
                a = f.read()
                print(a)
                f.close()

        if AdminOptions == 2:
            print("-----------------------------------------")
            print("|To add new doctor Enter 3              |")
            print("|To display doctor Enter 4              |")
            print("-----------------------------------------")

            Admin_choice = int(input("Enter your choice: "))

            if Admin_choice == 3:
                Doctor_ID = int(input("Enter doctor ID : "))
                Departmentofdoctor = input("Enter Doctor department: ")
                Nameofdocotor = input("Enter Doctor name: ")
                Address1 = input("Enter Doctor address:  ")
                Age1 = input("Enter patient age: ")
                Gender1 = input("Enter patient gender: ")
                mobileno1 = input("Enter mobile number: ")

                print("----------------------Doctor added successfully----------------------")
                h = open('doctorinformationall.txt', 'a')
                c = h.write(f'''
                    ==============================================================================
                        Doctor_ID:             {Doctor_ID}
                        Departmentofdoctor:    {Departmentofdoctor} 
                        Nameofdocotor:         {Nameofdocotor}
                        Age:                   {Age1}
                        Gender:                {Gender1}
                        Address:               {Address1}
                        Number of appointment: {mobileno1}
                    ==============================================================================
                ''')

                h.close()

                h = open('doctorinformation.txt', 'w')
                h.write(f"\n{Doctor_ID},{Departmentofdoctor},{Nameofdocotor},{Age1},{Gender1},{mobileno1}.")
                h.write(f'''
                                   ==============================================================================
                                       Doctor_ID:             {Doctor_ID}
                                       Departmentofdoctor:    {Departmentofdoctor} 
                                       Nameofdocotor:         {Nameofdocotor}
                                       Age:                   {Age1}
                                       Gender:                {Gender1}
                                       Address:               {Address1}
                                       Number fo appointment: {mobileno1}
                                   ==============================================================================
                               ''')
                h.close()

            elif Admin_choice == 4:
                h = open('patientinformation.txt', 'r')
                b = h.read()
                print(b)
                h.close()

        if AdminOptions == 3:
        
             dates = ['1-5-2021', '2-5-2021', '4-5-2021', '5-5-2021', '7-5-2021', '10-5-2021']
             docs = ['Dr. junaid(neuro)', 'Dr. Akhtar(Cardio)', 'Dr. sara(Gynae)']
             print("|      View dates for appointments. Enter 5       |")
             print("|    Book a date. Enter 6       |")
        
             print("-----------------------------------------")
        
             Admin_choice3 = int(input("Enter your choice please: "))
        
             if Admin_choice3 == 5:
                 print("alpha")
                 for item in dates:
                     print(item)
        
             elif Admin_choice3 == 6:
                 d = str(input('Enter the date you want to book appointment for, please check the available dates.\n'))
                 try:
                     print("Date has been booked.")
                     dates.remove(d)
                 except ValueError as e:
                     print("Date isn't available")
                 for item in docs:
                     print(item)
                 doc_c = str(input("Select one of the available doctors, \n")).lower()
                 if doc_c in docs:
                     print("Date is booked!")
                     docs.remove(doc_c)
                 else:
                     print("This doctor isn't available.")
# user modules
elif Selection == 2:
    while True:

        username1 = input("Enter your Username: ")
        if username1 == username:
            break
        else:
            print("the username you entered is incorrect")
    while True:
        password1 = input("Enter your Password: ")
        Password = "user1"
        if password1 == Password:
            break
        else:
            print("the password you entered is incorrect")
    print("\nYou have successfully logged into your account!")
    while True:
        print(
                "****************************************\n|         Welcome to user mode         |\n****************************************")

        print("\n-----------------------------------------")

        print("|To view hospital's doctors Enter 1    |")
        print("|To view patient's details Enter 2     |")
        print("-----------------------------------------")
        UserOptions = input("Enter your choice : ")

        if UserOptions == 1:
            try:
                print(c)
            except:
                print('Information not found!')
        if UserOptions == 2:
            try:
                print(b)
            except:
                print('Information not found!')


elif Selection == '3':
    quit


elif Selection != '1' or Selection != '2' or Selection != '3':
    print('Option Invalid')
    quit