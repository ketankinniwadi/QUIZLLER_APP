THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
from tkinter import *
from quiz_brain import QuizBrain


class QuizUi:

    def __init__(self, quiz: QuizBrain):
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.quiz = quiz
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125, text="this is the question", font=FONT, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text=f"SCORE:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.correct_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.correct_image, highlightthickness=0,
                                  activebackground=THEME_COLOR, bd=0, command=self.user_choose_correct)
        self.true_button.grid(row=2, column=0)

        self.wrong_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.wrong_image, highlightthickness=0,
                                   activebackground=THEME_COLOR, bd=0, command=self.user_choose_wrong)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="black")
        try:
            quiz_que = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=quiz_que)
            self.update_score()
        except IndexError:
            self.canvas.itemconfig(self.canvas_text, text="Quiz_is_over")

    def user_choose_correct(self):
        user_answer = "True"
        is_right = self.quiz.check_answer(user_answer)
        self.feed_back(is_right)

    def user_choose_wrong(self):
        user_answer = "False"
        is_right = self.quiz.check_answer(user_answer)
        self.feed_back(is_right)

    def feed_back(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def update_score(self):
        self.score_label.config(text=f"Score : {self.quiz.score}")


