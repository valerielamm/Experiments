
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

import PIL
from PIL import Image, ImageDraw, ImageTk


# Imported module functions
from start import *



class GuessingGame:
    def __init__(self, master):
        self.master = master
        # Title of page
        master.title("The Golden Carrot")

        # Main Text
        self.message = "The Golden Carrot"
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)
        self.label.grid(row=0, column=0, columnspan=2, sticky=W + E)
        self.label.config(background="#d8dad9", height=20, width=60)

        # Bunny Name
        self.b_name = "Bunny"
        self.label_bun = StringVar()
        self.label_bun.set(self.b_name)
        self.bun = Label(master, textvariable=self.label_bun)


        # Main 2 Buttons
        self.yes_button = Button(master, text="Continue", command=self.introductions)
        self.no_button = Button(master, text="Back", state=DISABLED)
        self.name = Entry(master)
        self.name.config(highlightbackground="#d8dad9", highlightcolor="#d8dad9")
        self.no_button.grid(row=2, column=0, sticky=W + E)
        self.no_button.config(highlightbackground="#d8dad9", highlightcolor="#d8dad9")
        self.yes_button.grid(row=2, column=1, sticky=W + E)
        self.yes_button.config(highlightbackground="#d8dad9", highlightcolor="#d8dad9")

        # Options
        self.option_one = True
        self.option_two = True

        # Drawing
        self.top = Toplevel()
        self.c = Canvas(self.top, bg='white', width=600, height=600)
        self.top.wm_title("Draw " + self.label_bun.get())
        self.c.grid(row=1, columnspan=5)
        self.image1 = PIL.Image.new('RGB', (600, 600), '#d8dad9')
        self.save_button = Button(self.top, text='save', command=self.use_save)
        self.save_button.grid(row=0, column=1)
        self.drawing_setup()
        self.top.withdraw()

    # Save Drawing
    def use_save(self, *args):
        self.filename = 'drawing.png'
        self.image1.save(self.filename)
        self.image2 = ImageTk.PhotoImage(Image.open("drawing.png").resize((200, 200)))
        self.image3 = Label(root, image=self.image2)
        self.image3.config(background="#d8dad9")
        self.image3.grid_remove()
        self.top.withdraw()

    # Imported module functions
    introductions = introductions
    question_one = question_one
    question_one_yes = question_one_yes
    question_one_end = question_one_end
    question_one_no = question_one_no
    stage_one = stage_one
    create_window = create_window
    stage_two = stage_two
    stage_three = stage_three
    drawing_setup = drawing_setup
    paint = paint
    reset = reset
    stage_three_fail = stage_three_fail
    stage_four = stage_four

my_gui = GuessingGame(root)
root.config(background="#f0f5f5", padx=20, pady=20)
root.mainloop()
