

import random
import json
from colorama import init, Fore, Style

init(autoreset=True)
def load_questions():
    with open("questions.json", "r") as json_file:
        data = json.load(json_file)
    print(data)  # Add this line to see the contents of the data dictionary
    return data["questions"]



def select_random_question(questions):
    return random.choice(questions)

def animate_question(question):
    colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]
    font_sizes = [Style.NORMAL, Style.BRIGHT]

    for color in colors:
        for font_size in font_sizes:
            formatted_question = f"{font_size}{color}{question['question']}{Style.RESET_ALL}"
            print(formatted_question)
            input("Press Enter for the next animation...")

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
    animate_question(selected_question)
    user_answer = get_user_answer()
    check_answer(selected_question, user_answer)

