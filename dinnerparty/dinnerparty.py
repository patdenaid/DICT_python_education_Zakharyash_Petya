def main():

    num_friends = int(input("Enter the number of friends joining (including you):\n"))


    if num_friends <= 0:
        print("No one is joining for the party")
        return


    friends_dict = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_friends):
        friend_name = input("> ")
        friends_dict[friend_name] = 0


    print(friends_dict)

    total_amount = float(input("Enter the total amount:\n"))
    if num_friends > 0:
        per_person_amount = round(total_amount / num_friends, 2)
        for friend in friends_dict:
            friends_dict[friend] = per_person_amount

    print(friends_dict)

if __name__ == "__main__":
    main()
