import PIL
from PIL import Image, ImageDraw, ImageTk

# Intro
def introductions(self):
    self.message = "\n\nBunny Tales: The Golden Carrot\
        \nThere once was a bunny that was trapped in a cage.\
        \nHis owner used to feed him all kinds of treats. \
        \nHe used to get carrots, kale, broccoli, and sweet\
        \ngrasses. One day his owner stopped bringing him\
        \nall the tasty foods. All he got was lettuce.\
        \nHe spent every day mindlessly eating the tasteless\
        \nlettuce. Every night, he dreamt of the tale of the\
        \ngolden carrot..."
    self.label_text.set(self.message)
    self.yes_button.configure(text="Continue", command=self.question_one)

# Ask user if they want to play
def question_one(self):
    self.message = "Do you want to guide the bunny to the golden carrot?"
    self.label_text.set(self.message)
    self.yes_button.configure(text="Yes", command=self.question_one_yes)
    self.no_button.configure(text="No", command=self.question_one_no, state="normal")

def question_one_yes(self):
    self.message = "Name your bunny."
    self.label_text.set(self.message)
    self.yes_button.configure(text="Continue", command=self.question_one_end)
    self.name.grid(row=2, column=0, columnspan=2, sticky= "w" + "e")
    self.yes_button.grid(row=3, column=1, sticky= "w" + "e")
    self.no_button.grid(row=3, column=0, sticky= "w" + "e")
    self.no_button.configure(state="disabled")

def question_one_end(self):
    self.b_name = self.name.get()
    self.b_name = self.b_name.capitalize()  # Capitalize that name!
    self.label_bun.set(self.b_name)
    self.name.destroy()
    self.message = "All right, " + self.label_bun.get() + " it is."
    self.label_text.set(self.message)
    self.yes_button.grid(row=2, column=1, sticky="w" + "e")
    self.no_button.grid(row=2, column=0, sticky="w" + "e")
    self.yes_button.configure(text="Continue", command=self.stage_one)
    self.no_button.configure(text=" ", command=self.question_one_yes, state="disabled")

def question_one_no(self):
    self.message = "The bunny never gathered the courage to go \
               \nafter the golden carrot. He spent the rest\
               \nof his days sad over what could\'ve been"
    self.label_text.set(self.message)
    self.yes_button.configure(state="disabled")
    self.no_button.configure(state="disabled")

def stage_one(self):
    self.message = self.label_bun.get() + " is ready to start their journey."
    self.label_text.set(self.message)
    self.yes_button.configure(text="Continue", command=self.create_window)

def create_window(self):
    self.yes_button.configure(text="Continue", command=self.stage_two)
    self.top.deiconify()
    self.top.wm_title("Draw " + self.label_bun.get())

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

def stage_two(self):
    self.label.config(height=7)
    self.image3.grid(row=1, column=0, columnspan=2, sticky="w" + "e")
    self.message = self.label_bun.get() + " looks great."
    self.label_text.set(self.message)
    self.yes_button.configure(text="Thanks.", command=self.stage_three)
    self.no_button.configure(text="I guess.", command=self.stage_three, state="normal")

def stage_three(self):
    self.label.config(height=20)
    self.image3.grid_forget()
    self.message = "Do you think " + self.label_bun.get() + " looks great?"
    self.label_text.set(self.message)
    self.yes_button.configure(text="Yes.", command=self.stage_four)
    self.no_button.configure(text="Not really.", command=self.stage_three_fail)

def stage_three_fail(self):
    self.message = self.label_bun.get() + " overheard you. \n They lost their confidence " \
                                          "and have decided to just stay in their cage."
    self.label_text.set(self.message)
    self.yes_button.configure(state="disabled")
    self.no_button.configure(state="disabled", text=" ")

def stage_four(self):
    self.message = self.label_bun.get() + " overheard you. \nThey gained more confidence " \
                                          "and have decided to go with you."
    self.label_text.set(self.message)
    self.yes_button.configure(text="Let's go.")
    self.no_button.configure(text=" ")
