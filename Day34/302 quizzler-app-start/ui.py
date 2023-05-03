import tkinter.messagebox
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title = "Quizzler!!"
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text=f"Score: {self.quiz.score}")
        self.score_label.config(foreground="white", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question", font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        correct_btn_img = PhotoImage(file="./images/true.png")
        false_btn_img = PhotoImage(file="./images/false.png")

        self.correct_btn = Button(image=correct_btn_img, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.submit_true)
        self.false_btn = Button(image=false_btn_img, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.submit_false)

        self.correct_btn.grid(row=2, column=0)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz!")
            self.correct_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
            box = tkinter.messagebox
            box.showinfo(title="Completed", message=f"You completed the quiz.\nYour final score is {self.quiz.score}/{len(self.quiz.question_list)}")

    def submit_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
        # if self.quiz.check_answer("True"):
        #     self.score_label.config(text=f"Score: {self.quiz.score}")
        #     self.give_feedback(True)
        # else:
        #     self.give_feedback(False)
        # self.get_next_question()

    def submit_false(self):
        self.give_feedback(self.quiz.check_answer("True"))
        # if self.quiz.check_answer("False"):
        #     self.score_label.config(text=f"Score: {self.quiz.score}")
        #     self.give_feedback(True)
        # else:
        #     self.give_feedback(False)
        # self.get_next_question()

    # def bg_noraml(self):
    #     self.canvas.config(bg="white")

    def give_feedback(self, condition: bool):
        if condition:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)