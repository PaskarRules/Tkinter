from tkinter import *
from tkinter import messagebox

from add_people import AddPerson
from update_people import UpdatePerson
from display import Display


import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()


class MyPeople(Toplevel):

    def add_person(self):
        add_page = AddPerson()
        self.destroy()

    def update_fnc(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(" ")[0]

        update_page = UpdatePerson(person_id)

    def display_person(self):
        selected_item = self.listbox.curselection()
        if selected_item:
            person = self.listbox.get(selected_item)
            person_id = person.split(" ")[0]

            display_page = Display(person_id)
        else:
            messagebox.showwarning("Error", "Empty sell. Choose someone.")

    def delete_person(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(" ")[0]

        query = "delete from 'addressbook' where person_id = '{}'".format(person_id)
        person_info = person.split(" ")

        string_for_mbox = "Are you sure you wanna delete " + person_info[1] + " " + person_info[2] + " ?"
        answer = messagebox.askquestion("Warning", string_for_mbox)
        if answer == 'yes':
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo("Success", "Deleted")
            except EXCEPTION as e:
                messagebox.showinfo("Info", str(e))

    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x550")
        self.title("My People")
        self.resizable(False, False)

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#ebb134')
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file='people.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=130, y=25)

        self.heading = Label(self.top, text='My People', font='arial 15 bold', bg='white', fg='#ebb434')
        self.heading.place(x=270, y=50)

        self.scrollbar = Scrollbar(self.bottom, orient=VERTICAL)

        self.listbox = Listbox(self.bottom, width=40, height=27)
        self.listbox.grid(row=0, column=0, padx=(40, 0))
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        persons = cur.execute("select * from 'addressbook'").fetchall()
        count = 0
        position = 1
        for person in persons:
            self.listbox.insert(count, str(position) + " " + str(person[1]) + " " + str(person[2]))
            count += 1
            position += 1

        self.scrollbar.grid(row=0, column=1, sticky=N+S)

        btn_add = Button(self.bottom, text='Add', width=12, font='Sans 12 bold', command=self.add_person)
        btn_add.grid(row=0, column=2, padx=20, pady=10, sticky=N)

        btn_update = Button(self.bottom, text='Update', width=12, font='Sans 12 bold', command=self.update_fnc)
        btn_update.grid(row=0, column=2, padx=20, pady=50, sticky=N)

        btn_display = Button(self.bottom, text='Display', width=12, font='Sans 12 bold', command=self.display_person)
        btn_display.grid(row=0, column=2, padx=20, pady=90, sticky=N)

        btn_delete = Button(self.bottom, text='Delete', width=12, font='Sans 12 bold', command=self.delete_person)
        btn_delete.grid(row=0, column=2, padx=20, pady=130, sticky=N)



