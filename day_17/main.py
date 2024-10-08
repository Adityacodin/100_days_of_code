from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question = data['text']
    answer = data['answer']
    question_bank.append(Question(question,answer))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    print()
print("You have completed the quiz !!")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")