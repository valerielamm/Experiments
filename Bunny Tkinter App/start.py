

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


def stage_two(self):
    self.label.config(height=7)
    self.image3.grid(row=1, column=0, columnspan=2, sticky="w" + "e")
    self.message = self.label_bun.get() + " looks great."
    self.label_text.set(self.message)
    self.yes_button.configure(text="Thanks.", command=self.stage_three)

def stage_three(self):
    self.label.config(height=20)
    self.image3.grid_forget()
    self.message = "Okay, here we go."
    self.label_text.set(self.message)
    self.yes_button.configure(text="Let's go.")