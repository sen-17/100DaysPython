class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.question_list = questions_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        user_answer = input(f"Q{self.question_number}: {current_question.text}(True/False): ").capitalize()
        
        if user_answer == current_question.answer:
            self.score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was: {current_question.answer}")
        print(f"Your current score is : {self.score}/{self.question_number}")
            

