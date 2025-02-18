import random

# Function to display a 2D grid
def display_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

# Tic-Tac-Toe
def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = "X"

    def check_win():
        for row in board:
            if row.count(player) == 3:
                return True
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return True
        return False

    for _ in range(9):
        display_grid(board)
        row, col = map(int, input(f"Player {player}, enter row and col (0-2): ").split())
        if board[row][col] == ' ':
            board[row][col] = player
            if check_win():
                display_grid(board)
                print(f"Player {player} wins!")
                return
            player = "O" if player == "X" else "X"
    print("It's a tie!")

# Minesweeper
def minesweeper():
    size = 5
    board = [[' ' for _ in range(size)] for _ in range(size)]
    mines = random.sample([(r, c) for r in range(size) for c in range(size)], 3)

    for r, c in mines:
        board[r][c] = "M"

    display_grid(board)
    print("Minesweeper started! Enter row and column to reveal (0-4)")

    while True:
        row, col = map(int, input("Enter row and col: ").split())
        if board[row][col] == "M":
            print("You hit a mine! Game Over.")
            break
        else:
            print("Safe! Keep playing.")

# Connect Four
def connect_four():
    board = [[' ' for _ in range(7)] for _ in range(6)]
    player = "X"

    def check_win():
        for r in range(6):
            for c in range(7 - 3):
                if all(board[r][c + i] == player for i in range(4)):
                    return True
        for r in range(6 - 3):
            for c in range(7):
                if all(board[r + i][c] == player for i in range(4)):
                    return True
        for r in range(6 - 3):
            for c in range(7 - 3):
                if all(board[r + i][c + i] == player for i in range(4)) or all(board[r + 3 - i][c + i] == player for i in range(4)):
                    return True
        return False

    while True:
        display_grid(board)
        col = int(input(f"Player {player}, enter column (0-6): "))
        for row in range(5, -1, -1):
            if board[row][col] == ' ':
                board[row][col] = player
                if check_win():
                    display_grid(board)
                    print(f"Player {player} wins!")
                    return
                player = "O" if player == "X" else "X"
                break

# Snake Game
def snake():
    size = 10
    board = [[' ' for _ in range(size)] for _ in range(size)]
    snake = [(5, 5)]  # Snake starts at position (5, 5)
    direction = "RIGHT"
    
    # Place food at a random location
    food = (random.randint(0, size-1), random.randint(0, size-1))
    
    def move_snake():
        head = snake[0]
        if direction == "UP":
            new_head = (head[0] - 1, head[1])
        elif direction == "DOWN":
            new_head = (head[0] + 1, head[1])
        elif direction == "LEFT":
            new_head = (head[0], head[1] - 1)
        else:  # RIGHT
            new_head = (head[0], head[1] + 1)

        # Check for collision with the walls or itself
        if new_head in snake or not (0 <= new_head[0] < size and 0 <= new_head[1] < size):
            print("Game Over! Snake crashed.")
            return False

        # Check if snake eats food
        if new_head == food:
            snake.insert(0, new_head)  # Snake grows
            return True  # Food eaten, snake grows

        # Move the snake
        snake.insert(0, new_head)
        snake.pop()
        return True

    while True:
        # Reset the board
        board = [[' ' for _ in range(size)] for _ in range(size)]
        
        # Place snake on the board
        for segment in snake:
            board[segment[0]][segment[1]] = 'O'
        
        # Place food on the board
        board[food[0]][food[1]] = 'X'
        
        display_grid(board)
        command = input("Move (W/A/S/D): ").upper()
        
        if command == "W":
            direction = "UP"
        elif command == "S":
            direction = "DOWN"
        elif command == "A":
            direction = "LEFT"
        elif command == "D":
            direction = "RIGHT"
        
        if not move_snake():
            break

# Battleship
def battleship():
    size = 5
    board = [[' ' for _ in range(size)] for _ in range(size)]
    ship_positions = random.sample([(r, c) for r in range(size) for c in range(size)], 3)
    guesses = 0

    print("Battleship Game! Guess ship locations.")

    while guesses < 5:
        row, col = map(int, input("Enter row and col: ").split())
        if (row, col) in ship_positions:
            print("Hit!")
            ship_positions.remove((row, col))
        else:
            print("Miss!")
        
        if not ship_positions:
            print("You sunk all ships! You win!")
            return
        guesses += 1

    print("Game Over! Some ships remain.")

# Main Menu
while True:
    print("\nGame Selector")
    print("1. Tic-Tac-Toe")
    print("2. Minesweeper")
    print("3. Connect Four")
    print("4. Snake")
    print("5. Battleship")
    print("6. Exit")

    choice = input("Enter the number of the game to play: ")

    if choice == "1":
        tic_tac_toe()
    elif choice == "2":
        minesweeper()
    elif choice == "3":
        connect_four()
    elif choice == "4":
        snake()
    elif choice == "5":
        battleship()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
