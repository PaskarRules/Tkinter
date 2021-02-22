from tkinter import *
from tkinter import messagebox

# from my_people import MyPeople

import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()


class AddPerson(Toplevel):

    def add_person(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone_number = self.entry_phone_number.get()
        address = self.entry_address.get(1.0, 'end-1c')

        # people = MyPeople()
        self.destroy()

        if name and surname and email and phone_number and address !=0:
            try:
                query = "insert into 'addressbook' (person_name, person_surname, person_email, person_phone, person_address) values (?,?,?,?,?)"
                cur.execute(query, (name, surname, email, phone_number, address))
                con.commit()
                messagebox.showinfo("Success", "Contact add")
            except EXCEPTION as e:
                messagebox.showerror('Error', str(e))
        else:
            messagebox.showerror('Error', 'Fill all the fields!', icon='warning')

    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x550")
        self.title("Add new person")
        self.resizable(False, False)

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#34baeb')
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file='people.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=130, y=25)

        self.heading = Label(self.top, text='Add new person', font='arial 15 bold', bg='white', fg='#ebb134')
        self.heading.place(x=270, y=50)

        # Name
        self.label_name = Label(self.bottom, text='Name', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_name.place(x=49, y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0, 'Enter name')
        self.entry_name.place(x=150, y=40)

        # Surname
        self.label_surname = Label(self.bottom, text='Surname', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_surname.place(x=49, y=80)

        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.insert(0, 'Enter surname')
        self.entry_surname.place(x=150, y=80)

        # Email
        self.label_email = Label(self.bottom, text='Email', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_email.place(x=49, y=120)

        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, 'Enter email')
        self.entry_email.place(x=150, y=120)

        # Phone number
        self.label_phone_number = Label(self.bottom, text='Phone', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_phone_number.place(x=49, y=160)

        self.entry_phone_number = Entry(self.bottom, width=30, bd=4)
        self.entry_phone_number.insert(0, 'Enter phone number')
        self.entry_phone_number.place(x=150, y=160)

        # Address
        self.label_address = Label(self.bottom, text='Address', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_address.place(x=49, y=200)

        self.entry_address = Text(self.bottom, width=23, height=8, bd=4)
        self.entry_address.place(x=150, y=200)

        # Button

        button = Button(self.bottom, text='Add person', width=27, height=1, command=self.add_person)
        button.place(x=147, y=350)
