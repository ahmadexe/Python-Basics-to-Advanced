                                ####### USER LOGIN ########
# print("\t\t\t\tA Projecy By Rabiya Ilyas Of Hotel Reservation System")                                     
# print("\t\t\t\t\t\tWelcome To Our Hotel\n\t\t\t\t\tHope You Will Enjoy Our Service." )


# name = input('"Enter your name: ')
# if len(name)>=3 and len(name)<=18:
#             print(f'Hi {name}')
# while len(name) < 3:
#         new_name: str = input('your name must be in between 3-18 characters long, please enter your name again: ')
#         if len(str(new_name)) >= 3 and len(str(new_name)) <= 18:
#             print(f'Hi {new_name}')
#             break
# while len(name) > 18:
#         new_name: str = input('your name must be in between 3-18 characters long, please enter your name again: ')
#         if len(str(new_name)) >= 3 and len(str(new_name)) <= 18:
#             print(f'Hi {new_name}')
#             break

# Father_name = input("What is your father's name?\n ")
# Mother_name = input("What is your mother's name?\n ")
# Phone_no=int(input("Enter your phone number:\n"))
# E_mail=str(input("Enter your email:"))
# cnic_no=input("Enter yor cnic no:")
# if len(cnic_no)==13:
#         print(f'{cnic_no}')
# while len(cnic_no)!=13:
#         new_cnic_no: str=input("your cnic_no is not equal to 13 characters, please enter your cnic_no again:")
#         if len(str(new_cnic_no)) == 13:
#             print(f'{new_cnic_no}')
#             break
#         print("Alright! Here is what I have so far")
# if len(name)>=3 and len(name)<=18:
#      print(f'Name: {name}')
# else:
#     print("Name: " + new_name)
#     print("Father's name: " + Father_name)
#     print("Mother's name: " + Mother_name)
#     print("Cnic no:"+cnic_no)
#     print("Please press 'enter' to confirm")
                   ######## Start Of System ########


rooms = [1,2,3,4,5,6,7,8,10,15,26,50,70]
normal_class_rooms=[1,2,3,4,5]
luxury_class_rooms=[6,7,8,9,10]
high_luxury_class_rooms=[15,26,50,70]
urgent_house_keeping_services=['Full room cleaning','Half room cleaning','Washroom cleaning','Clothes ironing','laundry']
menu_for_breakfast=['1.Seasonal cut fruit platter','2.Seasonal fresh fruit juices','3.Lassi','4.Yoghurt','5.Corn flakes' ,'6.wheat flakes','7.choco flakes','8.rice krispies' , '9.muesli','10.egg boiled','11.Fried egg','12.Omelette','13.pratha','14.tea','15.coffee']
menu_for_lunch = ['1.Pizza', '2.Burgers', '3.Pasta','4.Waffle Fries','5. Chicken Popeys','6.Tikka boti','7.biryani','8.white chicken','9.roti','10.naan','11.water','12.coke','13.7up','14.tea','15.coffee','16.Chilli hot fish','17.Sour cream guacamole and jalapeño salsa','18.Thai fried rice']
menu_for_dinner=['1.Pizza', '2.Burgers', '3.Pasta','4.Tikka boti','5.biryani','6. Karahi','7.Haleem','8. Mutton Korma','9.Tikka Kebab','10.Chapli Kebab','11.Chicken Tikka Leg Piece','12.Seekh Kabab','13.Reshmi kabab','14.chicken cheese kabab','15.Spiced Grilled Vegetables.']
all_time_available_dishes=['1.Chilli garlic grilled prawns','2.Shrimp and sweet peppers','3.Chicken and sprout','4.Cottage cheese','5.Dal chawal','6.Thick rice pancake','7.sambar and assortment of chutneys.','8.tea','9.coffee','10.cold drinks']
items_cost_breakfast={
'''Seasonal cut fruit platter'''  : '''RS 250''',
'''Seasonal fresh fruit juices''' : '''RS 150''',
'''Lassi ''' :'''RS 150''',
'''Yoghurt''' :'''RS 100''',
'''Corn flake'''  :'''RS 150''',
'''wheat flakes'''  :'''RS 150''',
'''choco flakes'''  :'''RS 150''',
'''rice krispies'''  :'''RS 200''',
'''muesli ''' :'''RS  150''',
'''egg boiled'''  :'''RS 50''',
'''Fried egg ''' :'''RS 50''',
'''Omelette'''  :'''RS 60''',
'''pratha'''  :'''RS 70''',
'''tea'''  :'''RS 70''',
'''coffee'''  :'''RS 80'''
}
items_cost_lunch={
'''Pizza''' :'''RS  800''',
'''Burgers'''  :'''RS  300''',
'''Pasta ''' :'''RS  200''',
'''Waffle Fries'''  :'''RS 200''',
'''Chicken Popeys ''' :'''RS  200''',
'''Tikka boti ''' :'''RS  400''',
'''biryani'''  :'''RS  350''',
'''white chicken'''  :'''RS 350''',
'''roti ''' :'''RS  40''',
'''naan'''  :'''RS  50''',
'''water'''  :'''RS  60''',
'''coke'''  :'''RS  80''',
'''7up'''  :'''RS  80''',
'''tea'''  :'''RS  70''',
'''coffee'''  :'''RS 80''',
'''Chilli hot fish ''' :'''RS  400''',
'''Sour cream guacamole and jalapeño salsa'''  :'''RS  400''',
'''Thai fried rice ''' :'''RS 450'''
}
items_cost_dinner={
'''Pizza'''  :'''RS  800''',
'''Burgers'''  :'''RS  300''',
'''Pasta'''  :'''RS  200''',
'''Tikka boti'''  :'''RS 250''',
'''biryani'''  :'''RS 350''',
''' Karahi'''  :'''RS 400''',
'''Haleem ''' :'''RS 300''',
''' Mutton Korma'''  :'''RS 400''',
'''Tikka Kebab'''  :'''RS 500''',
'''Chapli Kebab'''  :'''RS 100''',
'''Chicken Tikka Leg Piece ''' :'''RS 200''',
'''Seekh Kabab ''' :'''RS  200''',
'''Reshmi kabab ''' :'''RS  200''',
'''chicken cheese kabab ''' :'''RS  200''',
'''Spiced Grilled Vegetables ''' :'''RS 230'''
}
cost_all_time_available_dishes={ 
'''Chilli garlic grilled prawns'''  :'''RS 420''',
'''Shrimp and sweet peppers ''' :'''RS 150''',
'''Chicken and sprout'''  :'''RS 230''',
'''Cottage cheese '''  :'''RS 200''',
'''Dal chawal ''' :'''RS 190''',
'''Thick rice pancake'''  :'''RS 210''',
'''sambar and assortment of chutneys'''  :'''RS 80''',
'''tea  ''' :'''RS 70''',
'''coffee ''' :'''RS 80''',
'''cold drinks ''' :'''RS 80''',
}

parking=['place1','place2','place3','place4','place5','place6','place7','place8','place9','place10','place11','place12','place13','place14',]



while True:
    print(
    '''
    1. Check room.
    2. Rent of rooms
    3. Rooms available in normal class
    4. Book a room from normal class
    5. Rooms available in luxury class
    6. Book a room from normal class
    7. Rooms available in high luxury class
    8. book a room from high luxury class
    9. House keeping services available
    10. Dues of extra house keeping service 
    11. Call a servent for extra service
    12. Menu  
    13. Exit.
    '''
    )
    r = int(input("Enter your choice: "))

    if r == 1:
        for item in rooms:
            print(item)
    if r == 2:
        print('''The rent of rooms per a day according to class of room:
                "Rent of normal class room per a day: RS 8000"
                "Rent of Luxury class room per a day: RS 12000"
                "Rent of high luxury class room per a day: RS 16000"
                ''')
          

    if r == 3:
        for item in normal_class_rooms:
            print(item)

    if r == 4:
       a = int(input("Enter the room of your choice: "))
       days=input("How many days do you want to stay")
       print(int(days)*int(8000))
       normal_class_rooms.remove(a)
       print("Room",a,"has been booked.")
      

    if r == 5:
         for item in luxury_class_rooms:
            print(item)

    if r == 6:
       b = int(input("Enter the room of your choice: "))
       days=input("How many days do you want to stay")
       print(int(days)*int(12000))
       luxury_class_rooms.remove(a)
       print("Room",b,"has been booked.")        

    if r == 7:
         for item in high_luxury_class_rooms:
            print(item) 

    if r == 8:
        c = int(input("Enter the room of your choice: "))
        days=input("How many days do you want to stay")
        print(int(days)*int(16000))
            
        high_luxury_class_rooms.remove(a)
        print("Room",c,"has been booked.")

    if r == 9:
         for item in urgent_house_keeping_services:
            print(item) 

    if r == 10:
        print(''' Dues For Extra House Keeping Service Are As Follow:
        1.Full room = RS 1000
        2.half room = RS 700
        3.washroom cleaning =  RS 300
        4.Clothes ironing= RS 100 per cloth
        5.laundry= RS 100 per cloth
        
        ''')

    if r == 11:
        d=input('''Enter the service you need urgently:
        ''')
        if d == 1:
            print('''The payment for this service is: RS 1000
        which add in your total bill at time when you leave our hotel.''')

        elif d == 2:
            print('''The payment for this service is: RS 700
        which add in your total bill at time when you leave our hotel.''')

        elif d == 3:
            print('''The payment for this service is: RS 300
        which add in your total bill at time when you leave our hotel.''')

        elif d == 4:
            print('''The payment for this service is: RS 100
        which add in your total bill at time when you leave our hotel.''')

        elif d == 5:
            print('''The payment for this service is: RS 100
        which add in your total bill at time when you leave our hotel.''')

    if r == 12:
       print(''' There are three meals available:
       1.breakfast
       2.lunch
       3.dinner
       4.All time available dishes''')

       e=int(input("Enter the meal which you want:"))
       if e == 1:
           for items in menu_for_breakfast:
               print(items)

       if e == 2:
           for items in menu_for_lunch:
               print(items)

       if e == 3:
           for items in menu_for_dinner:
               print(items)

       if e == 4:
           for items in all_time_available_dishes:
               print(items)
    

    if r == 13:
        break