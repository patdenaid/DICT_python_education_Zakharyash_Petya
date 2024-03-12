class CoffeeMachine:
    def __init__(self):
        self.resources = {
            'water': 400,
            'milk': 540,
            'coffee_beans': 120,
            'disposable_cups': 9,
            'money': 550
        }
        self.prices = {
            '1': 4,
            '2': 7,
            '3': 6
        }
        self.recipes = {
            '1': {'water': 250, 'milk': 0, 'coffee_beans': 16},
            '2': {'water': 350, 'milk': 75, 'coffee_beans': 20},
            '3': {'water': 200, 'milk': 100, 'coffee_beans': 12}
        }

    def buy_coffee(self, choice):
        if choice in self.recipes:
            recipe = self.recipes[choice]
            if all(self.resources[resource] >= amount for resource, amount in recipe.items()):
                print("I have enough resources, making you a coffee!")
                self.resources['water'] -= recipe['water']
                self.resources['milk'] -= recipe['milk']
                self.resources['coffee_beans'] -= recipe['coffee_beans']
                self.resources['disposable_cups'] -= 1
                self.resources['money'] += self.prices[choice]
            else:
                print("Sorry, not enough resources!")
        elif choice == 'back':
            pass
        else:
            print("Invalid choice!")

    def refill_machine(self, water, milk, coffee_beans, cups):
        self.resources['water'] += water
        self.resources['milk'] += milk
        self.resources['coffee_beans'] += coffee_beans
        self.resources['disposable_cups'] += cups

    def take_money(self):
        print(f"I gave you ${self.resources['money']}")
        self.resources['money'] = 0

    def display_state(self):
        print("The coffee machine has:")
        for resource, amount in self.resources.items():
            print(f"{amount} of {resource}")
        print()

    def process_action(self, action):
        if action == 'buy':
            choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
            self.buy_coffee(choice)
        elif action == 'fill':
            water = int(input("Write how many ml of water you want to add:\n"))
            milk = int(input("Write how many ml of milk you want to add:\n"))
            coffee_beans = int(input("Write how many grams of coffee beans you want to add:\n"))
            cups = int(input("Write how many disposable coffee cups you want to add:\n"))
            self.refill_machine(water, milk, coffee_beans, cups)
        elif action == 'take':
            self.take_money()
        elif action == 'remaining':
            self.display_state()



coffee_machine = CoffeeMachine()

while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == 'exit':
        break
    elif action in ['buy', 'fill', 'take', 'remaining']:
        coffee_machine.process_action(action)
