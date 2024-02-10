from tkinter import *

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"

class QuizInteface():
    def __init__(self):
        self.window = Tk()

        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg=WHITE)
        self.canvas.create_text(150,125,text="dfasdfsad", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        #Score 
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        #Buttons
        right_button_img = PhotoImage(file="./images/false.png")
        wrong_button_img = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=right_button_img, highlightbackground=THEME_COLOR)
        self.wrong_button = Button(image=wrong_button_img, highlightbackground=THEME_COLOR)
        self.right_button.grid(column=0, row=2)
        self.wrong_button.grid(column=1, row=2)
        self.window.mainloop()