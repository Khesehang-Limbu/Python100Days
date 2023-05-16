class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.q_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q{self.question_no}. {current_question.text}(True or False) : ").lower()
        self.compare_answer(user_answer, current_question.answer.lower())

    def still_has_questions(self):
        return self.question_no < len(self.q_list)

    def compare_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print(f"You got it right!")
            self.score += 1
        elif user_answer != correct_answer:
            print("You're wrong!")
        print(f"Your score is {self.score}/{self.question_no}\n")
