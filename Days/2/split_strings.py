def to_uppercase(text):
    """Converts a string to all uppercase."""
    return text.upper()

def to_lowercase(text):
    """Converts a string to all lowercase."""
    return text.lower()

def split_into_chunks(text, chunk_size):
    """Splits a string into chunks of a given size."""
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# Main function to handle user input
def main():
    print("Choose an option:")
    print("1 - Convert to UPPERCASE")
    print("2 - Convert to lowercase")
    print("3 - Split into chunks")

    choice = input("Enter 1, 2, or 3: ")  # Get the user's choice

    if choice not in ["1", "2", "3"]:
        print("Invalid choice! Please enter 1, 2, or 3.")
        return  # Exit if the choice is invalid

    user_text = input("Enter your text: ")  # Ask for the text after selecting an option

    if choice == "1":
        print("\nResult:", to_uppercase(user_text))
    elif choice == "2":
        print("\nResult:", to_lowercase(user_text))
    elif choice == "3":
        chunk_size = int(input("Enter chunk size: "))
        print("\nResult:", split_into_chunks(user_text, chunk_size))

main()