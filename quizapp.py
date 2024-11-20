import random
from users_db import register_user, login_user 
from questions_db import create_question_db, insert_questions  
import sqlite3

class PythonQuizApp:
    def __init__(self):
        self.score = 0
        self.conn_question = sqlite3.connect('questions.db')
        self.c_question = self.conn_question.cursor()

    def start_quiz(self):
        # Fetch 5 random questions
        self.c_question.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT 5")
        questions = self.c_question.fetchall()

        for question in questions:
            question_text = question[1]
            options = question[2].split(',')
            correct_answer = question[3]
            self.ask_question(question_text, options, correct_answer)

        print(f"Your final score: {self.score}/5")

    def ask_question(self, question_text, options, correct_answer):
        print(f"Question: {question_text}")
        for idx, option in enumerate(options):
            print(f"{idx + 1}. {option}")

        answer = input("Your answer: ")
        if answer.strip().lower() == correct_answer.lower():
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_answer}\n")

if __name__ == "__main__":
   
    from users_db import create_user_db 
    from questions_db import create_question_db, insert_questions 

    create_question_db()  
    insert_questions()  
    create_user_db() 

    # Register a user
    username = input("Enter username for registration: ")
    password = input("Enter password for registration: ")
    register_user(username, password)

    # Log in
    username = input("Enter username for login: ")
    password = input("Enter password for login: ")

    if login_user(username, password):
        # If login is successful, start the quiz
        quiz_app = PythonQuizApp()
        quiz_app.start_quiz()
