# class User:
#     def __init__(self, id, username):
#         self.id = id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         self.following += 1
#         user.followers += 1
#
# user1 = User("001", "Serge")
# user2 = User("002", "Tania")
#
# user1.follow(user2)
#
# print(user1.followers)
# print(user1.following)
# print(user2.followers)
# print(user2.following)



####################### QUIZ GAME #######################
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    # question_bank.append(Question("text","answer"))
    q_text = question['question']
    q_answer = question['correct_answer']
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

more_questions = True
while quiz.still_has_questions() == True:
    quiz.next_question()
    print("")

if quiz.still_has_questions() == False:
    quiz.final_score()

print(quiz.score)
print(quiz.question_number)
    # more_questions = quiz.still_has_questions()
# if user_answer == current_question.answer:
#     question_number += 1
# else:
#     Print("You a wrong!")


