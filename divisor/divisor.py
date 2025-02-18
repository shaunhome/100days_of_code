# Define a function to find divisors of a given number
def find_divisors(num):
    # Initialize an empty list to store divisors
    divisors = []
    # Iterate through numbers from 1 to the given number (inclusive)
    for i in range(1, num + 1):
        # Check if the current number evenly divides the given number
        if num % i == 0:
            # If it does, add it to the list of divisors
            divisors.append(i)
    # Return the list of divisors
    return divisors

# Start an infinite loop : AMAZING
while True:
    # Prompt the user to enter a number (or 'exit' to quit)
    user_input = input("Enter a number (or 'exit' to quit): ")
    
    # Check if the user wants to exit the program
    if user_input.lower() == 'exit':
        # If so, print a message and exit the loop, ending the program
        print("Exiting the program.")
        break
    
    # Try to convert the user input to an integer
    try:
        number = int(user_input)
        # Check if the entered number is positive
        if number < 1:
            # If not, prompt the user to enter a positive integer
            print("Please enter a positive integer.")
        else:
            # If the number is positive, find its divisors using the find_divisors function
            divisors = find_divisors(number)
            # Print the divisors of the entered number
            print("Divisors of", number, "are:", divisors)
    # Handle the case where the user enters an invalid input (not a number)
    except ValueError:
        # If the input is not a valid number, print an error message and prompt the user again
        print("Invalid input. Please enter a valid number or 'exit' to quit.")