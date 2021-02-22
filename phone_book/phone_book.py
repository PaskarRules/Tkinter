import datetime
from tkinter import *

from about_us import AboutUs
from add_people import AddPerson
from my_people import MyPeople

date = datetime.datetime.now().date()


class Application(object):

    def my_people(self):
        people = MyPeople()

    def add_people(self):
        add_people = AddPerson()

    def about_us(self):
        about_us = AboutUs()

    def __init__(self, master):
        self.master = master

        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500, bg='#34baeb')
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file='phone- 64.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=130, y=25)

        self.heading = Label(self.top, text='My Phone book App', font='arial 15 bold', bg='white', fg='#ebb434')
        self.heading.place(x=230, y=50)

        self.date_lbl = Label(self.top, text="Today's date: " + str(date), font='arial 12 bold', fg='#ebb434',
                              bg='white')
        self.date_lbl.place(x=450, y=110)

        self.viewButton = Button(self.bottom, text='My People', font='aria 12 bold', width=12, fg='#34baeb',
                                 command=self.my_people)
        self.viewButton.place(x=250, y=70)

        self.addButton = Button(self.bottom, text='Add Person', font='aria 12 bold', width=12, fg='#34baeb',
                                command=self.add_people)
        self.addButton.place(x=250, y=130)

        self.aboutButton = Button(self.bottom, text='About us', font='aria 12 bold', width=12, fg='#34baeb',
                                  command=self.about_us)
        self.aboutButton.place(x=250, y=190)


def main():
    root = Tk()
    app = Application(root)
    root.title("Phone Book App")
    root.geometry("650x550+350+200")
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()
