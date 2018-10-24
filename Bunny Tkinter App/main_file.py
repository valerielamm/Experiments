
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


        self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
        self.label.config(background="#d8dad9", height=20, width=60)
        self.no_button.grid(row=2, column=0, sticky=W+E)
        self.no_button.config(highlightbackground="#d8dad9", highlightcolor="#d8dad9")
        self.yes_button.grid(row=2, column=1, sticky=W+E)
        self.yes_button.config(highlightbackground="#d8dad9", highlightcolor="#d8dad9")

    def use_save(self, *args):
        self.filename = 'drawing.png'
        self.image1.save(self.filename)
        self.image2 = ImageTk.PhotoImage(Image.open("drawing.png").resize((200, 200)))
        self.image3 = Label(root, image=self.image2)
        self.image3.config(background="#d8dad9")
        self.image3.grid_remove()

    def drawing_setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = 15
        self.color = 'black'
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def paint(self, event):
        self.line_width = 15
        paint_color = self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle='round')
            #  --- PIL
            draw = ImageDraw.Draw(self.image1)
            draw.line((self.old_x, self.old_y, event.x, event.y), width=5, fill='black')

        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    # Note: Imported module functions need to be set as an attribute INSIDE the class that uses it
    introductions = introductions
    question_one = question_one
    question_one_yes = question_one_yes
    question_one_end = question_one_end
    question_one_no = question_one_no
    stage_one = stage_one
    create_window = create_window
    stage_two = stage_two
    stage_three = stage_three


my_gui = GuessingGame(root)
root.config(background="#f0f5f5", padx=20, pady=20)
root.mainloop()
