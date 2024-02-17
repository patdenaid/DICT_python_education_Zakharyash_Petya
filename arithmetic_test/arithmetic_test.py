import random

def generate_question(level):
    """Генерує арифметичне завдання відповідно до рівня складності."""
    if level == 1:
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operator = random.choice(['+', '-', '*'])
        question = f"{num1} {operator} {num2}"
    elif level == 2:
        num = random.randint(11, 29)
        question = f"{num}"
    return question

def save_results(name, mark, level_description):
    """Зберігає результати тесту в файл results.txt."""
    with open("results.txt", "a") as file:
        file.write(f"{name}: {mark}/5 in level {level_description}.\n")

def main():
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")
    level = int(input("> "))

    if level not in [1, 2]:
        print("Incorrect format.")
        return

    correct_answers = 0
    for _ in range(5):
        question = generate_question(level)
        print(question)
        while True:
            user_answer = input("> ")
            try:
                user_answer = int(user_answer) if level == 2 else eval(user_answer)
            except (NameError, SyntaxError, ValueError):
                print("Wrong format! Try again.")
                continue
            else:
                break

        correct_answer = eval(question) if level == 1 else int(question) ** 2
        if user_answer == correct_answer:
            print("Right!")
            correct_answers += 1
        else:
            print("Wrong!")

    print(f"Your mark is {correct_answers}/5. Would you like to save the result? Enter yes or no.")
    save_result = input("> ").lower()
    if save_result in ['yes', 'y']:
        name = input("What is your name?\n> ")
        if level == 1:
            level_description = "simple operations with numbers 2-9"
        else:
            level_description = "integral squares of 11-29"
        save_results(name, correct_answers, level_description)
        print("The results are saved in 'results.txt'.")
    else:
        print("Goodbye.")

if __name__ == "__main__":
    main()
