import datetime

# Отримуємо поточний рік
current_year = datetime.datetime.now().year

# Задаємо ім'я бота
bot_name = "DICT_Bot"

# Виводимо привітання
print(f"Hello! My name is {bot_name}.")
print(f"I was created in {current_year}.")

# Просимо користувача ввести своє ім'я
user_name = input("Please, remind me your name.\n")

# Виводимо вітання з ім'ям користувача
print(f"What a great name you have, {user_name}!")

# Вгадуємо вік користувача
print("Let me guess your age.")
remainder3 = int(input("Enter the remainder of dividing your age by 3: "))
remainder5 = int(input("Enter the remainder of dividing your age by 5: "))
remainder7 = int(input("Enter the remainder of dividing your age by 7: "))

# Визначаємо вік за формулою
your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

# Виводимо вгаданий вік
print(f"Your age is {your_age}; that's a good time to start programming!")

# Рахуємо від 0 до числа, введеного користувачем
count_to = int(input("Now I will prove to you that I can count to any number you want.\n"))
current_number = 0

while current_number <= count_to:
    print(f"{current_number} !")
    current_number += 1

# Тест для перевірки знань користувача
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

correct_answer = 2  # Правильна відповідь
user_answer = int(input("> "))

while user_answer != correct_answer:
    print("Please, try again.")
    user_answer = int(input("> "))

print("Congratulations, have a nice day!")
