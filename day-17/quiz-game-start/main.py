from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_bank = []
score = 0
for item in question_data:
    question = item["text"]
    answer = item["answer"]
    new_question = Question(question, answer)
    questions_bank.append(new_question)

quiz = QuizBrain(questions_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")




