def print_horizontal_line(length):
    print(" ---" * length)

def print_vertical_line(width):
    print("|   " * width + "|")

def print_board(length, width):
    for _ in range(width):
        print_horizontal_line(length)
        print_vertical_line(width)
        print_horizontal_line(length)

# Example usage:
print_board(6, 3)