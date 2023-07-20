import random
import json
from colorama import init, Fore, Style

init(autoreset=True)
def load_questions():
    with open("questions.json", "r") as json_file:
        data = json.load(json_file)
    # print(data) : Add this line to see the contents of the data dictionary
    return data["questions"]
def select_random_question(questions):
    return random.choice(questions)

def send_question(question):
    formatted_question = f"{question['question']}"
    print(formatted_question)

def get_user_answer():
    return input("Your answer: ")

def check_answer(question, user_answer):
    if user_answer.lower() == question['answer'].lower():
        print(Fore.GREEN + "Correct answer!")
    else:
        print(Fore.RED + "Incorrect answer. The correct answer is:", question['answer'])

if __name__ == "__main__":
    questions = load_questions()
    selected_question = select_random_question(questions)
    send_question(selected_question)
    user_answer = get_user_answer()
    check_answer(selected_question, user_answer)
