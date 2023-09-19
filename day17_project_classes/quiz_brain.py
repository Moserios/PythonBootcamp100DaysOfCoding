class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("That's right.")
            self.score += 1
        else:
            print(f"That's wrong. Correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.")

    def final_score(self):
        print(f"Your've completed the quiz")
        print(f"Your final score is: {self.score}/{self.question_number}.")



