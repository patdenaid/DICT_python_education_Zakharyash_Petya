def main():
    # Етап 1: Зчитуємо кількість друзів
    num_friends = int(input("Enter the number of friends joining (including you):\n"))

    # Перевірка на коректність кількості людей
    if num_friends <= 0:
        print("No one is joining for the party")
        return

    # Етап 2: Зчитуємо імена друзів та зберігаємо їх у словнику
    friends_dict = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_friends):
        friend_name = input("> ")
        friends_dict[friend_name] = 0

    # Етап 3: Виводимо отриманий словник
    print(friends_dict)

    # Етап 4: Розділити рахунок порівну
    total_amount = float(input("Enter the total amount:\n"))
    if num_friends > 0:
        per_person_amount = round(total_amount / num_friends, 2)
        for friend in friends_dict:
            friends_dict[friend] = per_person_amount

    # Етап 5: Виводимо оновлений словник
    print(friends_dict)

if __name__ == "__main__":
    main()
