def print_grid(cells):
    print("---------")
    for i in range(0, 9, 3):
        print(f"| {cells[i]} {cells[i+1]} {cells[i+2]} |")
    print("---------")

def analyze_game_state(cells):
    rows = [cells[i:i+3] for i in range(0, 9, 3)]
    columns = [cells[i::3] for i in range(3)]
    diagonals = [cells[0::4], cells[2:8:2]]
    winning_combinations = rows + columns + diagonals

    x_wins = any(all(cell == 'X' for cell in combination) for combination in winning_combinations)
    o_wins = any(all(cell == 'O' for cell in combination) for combination in winning_combinations)

    count_x = cells.count('X')
    count_o = cells.count('O')
    diff = abs(count_x - count_o)

    if x_wins and o_wins or diff > 1:
        return "Impossible"
    elif x_wins:
        return "X wins"
    elif o_wins:
        return "O wins"
    elif '_' in cells:
        return "Game not finished"
    else:
        return "Draw"

def make_move(cells, row, col, symbol):
    index = (row - 1) * 3 + (col - 1)
    if cells[index] == '_':
        cells[index] = symbol
        return True
    else:
        return False

def is_valid_input(user_input):
    try:
        row, col = map(int, user_input.split())
        return 1 <= row <= 3 and 1 <= col <= 3
    except ValueError:
        return False

# Ініціалізація порожнього поля
game_cells = ['_' for _ in range(9)]

# Початок гри
print_grid(game_cells)

# Гравчини ігровий цикл
current_player = 'X'
while True:
    user_move = input(f"Enter the coordinates for {current_player}: ")
    if is_valid_input(user_move):
        row, col = map(int, user_move.split())
        if make_move(game_cells, row, col, current_player):
            print_grid(game_cells)
            result = analyze_game_state(game_cells)
            if result != "Game not finished":
                print(result)
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("This cell is occupied! Choose another one!")
    else:
        print("Invalid input! Please enter valid coordinates.")
