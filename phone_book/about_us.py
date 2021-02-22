from tkinter import *


class AboutUs(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("550x550+550+200")
        self.title("About us")
        self.resizable(False, False)

        self.top = Frame(self, height=550, width=550, bg='#ffa550')
        self.top.pack(fill=BOTH)

        self.text = Label(self.top, text="This page is about us."
                                         "\nThis app made by Alex Prydolob for example of my power!\n"
                                         "Our contacts:\n"
                                         "Phone: +380957452819\n"
                                         "Email: prydolob_o@itstep.org",
                          font='arial 14 bold', bg="#34baeb", fg='white'

                          )

        self.text.place(x=3, y=50)