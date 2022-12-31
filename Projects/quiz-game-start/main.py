from question_model import Question
from data import question_data
from quiz_brain import  QuizBrain

question_bank = []


for i in question_data:
    question_text = i["question"]
    question_answer = i["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

final_score = f"{quiz.score}/{quiz.question_number}"

print("you've complete the quiz")
print(f"your final score was: {final_score}")
