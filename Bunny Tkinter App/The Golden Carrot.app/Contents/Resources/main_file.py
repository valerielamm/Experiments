
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

root = Tk()

"""
.Main File that determines paths
"""
from start import *


class GuessingGame:
    def __init__(self, master):
        self.master = master
        # Title of page
        master.title("The Golden Carrot")

        self.message = "The Golden Carrot"
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)

        self.b_name = "Bunny"
        self.label_bun = StringVar()
        self.label_bun.set(self.b_name)
        self.bun = Label(master, textvariable=self.label_bun)

        self.yes_button = Button(master, text="Continue", command=self.introductions)
        self.no_button = Button(master, text="Back", state=DISABLED)
        self.name = Entry(master)
        self.name.config(highlightbackground="#d8dad9", highlightcolor="#d8dad9")


        self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
        self.label.config(background="#d8dad9", height=20, width=60)
        self.no_button.grid(row=2, column=0, sticky=W+E)
        self.no_button.config(highlightbackground="#d8dad9", highlightcolor="#d8dad9")
        self.yes_button.grid(row=2, column=1, sticky=W+E)
        self.yes_button.config(highlightbackground="#d8dad9", highlightcolor="#d8dad9")

    # Note: Imported module functions need to be set as an attribute INSIDE the class that uses it
    introductions = introductions
    question_one = question_one
    question_one_yes = question_one_yes
    question_one_end = question_one_end
    question_one_no = question_one_no
    stage_one = stage_one


my_gui = GuessingGame(root)
root.config(background="#f0f5f5", padx=20, pady=20)
root.mainloop()
