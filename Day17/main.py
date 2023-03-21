from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for key in question_data:
    new_question = Question(key["text"], key["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("you've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_no}")