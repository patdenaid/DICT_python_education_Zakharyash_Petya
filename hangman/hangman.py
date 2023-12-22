import random

# Список слів
word_list = ['python', 'java', 'javascript', 'php']


def generate_hint(secret_word, guessed_letters):
    # Генерує підказку зі слова та вже вгаданих літерами
    hint = ""
    for letter in secret_word:
        if letter in guessed_letters:
            hint += letter
        else:
            hint += "-"
    return hint


def main():
    print("HANGMAN")

    while True:
        choice = input('Type "play" to play the game, "exit" to quit: > ').strip().lower()
        if choice == "exit":
            print("See you later!")
            break
        elif choice == "play":
            # Випадково обране слово зі списку
            secret_word = random.choice(word_list)

            # Відомі літери
            guessed_letters = []

            # Кількість спроб (життів)
            attempts = 8

            while attempts > 0:
                print("\n" + generate_hint(secret_word, guessed_letters))
                print("Attempts left:", attempts)
                guess = input("Input a letter: > ").lower()

                if len(guess) != 1 or not guess.isalpha() or not guess.islower():
                    print("Please enter a lowercase English letter.")
                    continue

                if guess in guessed_letters:
                    print("You've already guessed this letter")
                    continue

                guessed_letters.append(guess)

                if guess in secret_word:
                    if "-" not in generate_hint(secret_word, guessed_letters):
                        print(secret_word)
                        print("You guessed the word!")
                        print("You survived!")
                        break
                    else:
                        print("No improvements")
                else:
                    print("That letter doesn't appear in the word")
                    attempts -= 1

            if "-" in generate_hint(secret_word, guessed_letters):
                print("You lost!")
        else:
            print("Invalid choice. Type 'play' to play or 'exit' to quit.")


if __name__ == "__main__":
    main()
