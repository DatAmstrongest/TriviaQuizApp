from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
GREEN = "#008000"
RED = "#FF0000"

class QuizInteface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()

        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg=WHITE)
        self.question_text = self.canvas.create_text(150,125, width=200,text="dfasdfsad", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        #Score 
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        #Buttons
        right_button_img = PhotoImage(file="./images/false.png")
        wrong_button_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=right_button_img, highlightbackground=THEME_COLOR, command=self.true_button_action)
        self.false_button = Button(image=wrong_button_img, highlightbackground=THEME_COLOR, command= self.false_button_action)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg=WHITE)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
  
    def true_button_action(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_button_action(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)
        self.window.after(1000, self.get_next_question)
    
