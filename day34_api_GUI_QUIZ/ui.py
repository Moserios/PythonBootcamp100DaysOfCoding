from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(150, 125, text="Question text from 'https://opentdb.com'",
                                                     fill='black', font=("Arial", 18, "italic"), width=290)

        self.score_lable = Label(width=10, text="Score: 0", font=("Arial", 10, "bold"), bg=THEME_COLOR,
                                 fg="white")
        self.score_lable.grid(column=1, row=0)

        false_button_img = PhotoImage(file="images/false.png")
        true_button_img = PhotoImage(file="images/true.png")
        self.false_button = Button(image=false_button_img, highlightthickness=0, highlightbackground=THEME_COLOR,
                                   command=self.answer_false)
        self.false_button.grid(column=1, row=2)
        self.true_button = Button(image=true_button_img, highlightthickness=0, highlightbackground=THEME_COLOR,
                                  command=self.answer_true)
        self.true_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="WHITE")
        if self.quiz.still_has_questions():
            self.score_lable.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've tried all questions.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
        # self.get_next_question()

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        # self.get_next_question()

    def give_feedback(self, is_right):
        if is_right is True:
            self.canvas.config(bg="GREEN")
        else:
            self.canvas.config(bg="RED")
        self.window.after(1000, self.get_next_question)
