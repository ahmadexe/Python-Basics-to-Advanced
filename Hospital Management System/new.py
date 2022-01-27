from tkinter import *
from tkinter.messagebox import showinfo
import time
import random
from PIL import Image, ImageTk

doctors = ['Dr. Ahmad', 'Dr. Haris', 'Dr. Sufyan', 'Dr. Usman', 'Dr. Mussab']
dates = ['2/10/2020', '3/10/2020', '5/10/2020']


root = Tk()
# img_a = Image.open(sss.jpg)

# img_b = ImageTk.PhotoImage(img_a)

# Label(root, image = img_b).place(x = 0, y = 0)


def main_user():
    

    def info():
        f = open('apps.txt', 'r')
        l = f.readlines()
        f.close()
        for line in l:
            if e_info_val.get() in line:
                showinfo("Information", line)
            else:
                pass
       

    def app():
        f = open('apps.txt', 'a')
        f.write(f"\n{e_name_val.get()}, {e_phone_val.get()}, {e_gender_val.get()}, {e_age_val.get()}, {e_doc_val.get()}, {e_date_val.get()}.")        
        showinfo("Appointment Completed!", "Your Appointment has been completed")

    def show_doc():
        global doctors
        a = ""
        for item in doctors:
            a = a + ", " + item
    
        showinfo("Doctors", f"Available Doctors are {a}")


    def show_date():
        global dates
        b = ""
        for item in dates:
            b = b + ", " + item
    
        showinfo("Dates", f"Available dates are {b}")



     
    top = Toplevel()
#   global p,o,i

#   p = Image.open(jdsahl.jpg)

#   o = ImageTk.PhotoImage(p) 
#   i = Label(top, image = o)
#   i.place(x = 0, y = o)


    top.title("Hospital Management System")
    top.geometry('800x450')
    Label(top, text = "Hospital Managemnet System", font = "Lucida 20 bold").place(x = 490, y = 10)

    btn_doc = Button(top, text = "View Doctors", command = show_doc)
    btn_doc.place(x = 20, y = 20)
    
    bnt_date = Button(top, text= "View Dates", command = show_date) 
    bnt_date.place(x = 20, y = 60)

    
    e_name_val = StringVar()
    e_phone_val = StringVar()
    e_gender_val = StringVar()
    e_age_val = StringVar()
    e_doc_val = StringVar()
    e_date_val = StringVar()


    e_name_ent = Entry(top, textvariable = e_name_val)
    e_name_ent.place(x = 200, y = 100)
    e_phone_ent =  Entry(top, textvariable = e_phone_val)
    e_phone_ent.place(x = 200, y = 140)
    e_gender_ent = Entry(top, textvariable = e_gender_val)
    e_gender_ent.place(x = 200, y = 180)
    e_age_ent =  Entry(top, textvariable = e_age_val)
    e_age_ent.place(x = 200, y = 220)
    e_doc_ent =  Entry(top, textvariable = e_doc_val)
    e_doc_ent.place(x = 200, y = 260) 
    e_date_ent =  Entry(top, textvariable = e_date_val)
    e_date_ent.place(x = 200, y = 300)





    Label(top, text = "Name", font = 'lucida 12').place(x = 20, y = 100)
    Label(top, text = "Phone", font = 'lucida 12').place(x = 20, y = 140)
    Label(top, text = "Gender", font = 'lucida 12').place(x = 20, y = 180)
    Label(top, text = "Age", font = 'lucida 12').place(x = 20, y = 220)
    Label(top, text = "Name of your Doctor", font = 'lucida 12').place(x = 20, y = 260)
    Label(top, text = "Date Alloted", font = 'lucida 12').place(x = 20, y = 300)
    


    global doctors, dates
    doc_pick = random.randint(0, 4)
    x = doctors[doc_pick]
    e_doc_val.set(x)
    date_pick = random.randint(0, 2)
    y = dates[date_pick]
    e_date_val.set(y)
    Button(top, text = 'Get Appointment', command = app).place(x = 110, y = 350)

    e_info_val = StringVar()
    e_info_ent = Entry(top, textvariable = e_info_val)
    e_info_ent.place(x = 1100, y = 100)
    Button(top, text = 'View Information', command = info).place(x = 1100, y = 150)

    


root.geometry('800x450')
root.title("Login")
Button(root, text = "Welcome, Get Started!", command = main_user).place(x = 20, y = 20)

root.mainloop()
