def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")

def mortgage_calculator():
    print("Welcome to the Deadly Accurate Mortgage Calculator!")
    house_cost = get_float_input("Enter the house cost in pounds: ")
    deposit = get_float_input("Enter the deposit amount in pounds: ")

    while deposit >= house_cost:
        print("Deposit cannot be equal to or greater than the house cost.")
        deposit = get_float_input("Enter the deposit amount in pounds: ")

    principal = house_cost - deposit

    annual_interest_rate = get_float_input("Enter the annual interest rate (as a percentage): ") / 100

    credit_score = int(input("Enter your credit score: "))

    # Adjust interest rate based on credit score
    if credit_score < 600:
        annual_interest_rate += 0.02  # Add 2 percentage points for lower credit scores
    elif 600 <= credit_score < 700:
        annual_interest_rate += 0.01  # Add 1 percentage point for moderate credit scores

    years = int(get_float_input("Enter the loan term in years: "))
    payments_per_year = 12  # Assuming monthly payments for UK mortgages

    # Calculate monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12

    # Calculate total number of payments
    total_payments = years * payments_per_year

    # Calculate mortgage payment
    mortgage_payment = principal * (monthly_interest_rate * ((1 + monthly_interest_rate) ** total_payments)) / (((1 + monthly_interest_rate) ** total_payments) - 1)

    # Option to overpay
    overpay_option = input("Do you want to overpay each month? (yes/no): ").lower()
    if overpay_option == "yes":
        overpayment_amount = get_float_input("Enter the overpayment amount per month in pounds: ")
    else:
        overpayment_amount = 0

    # Initialize payment schedule list
    payment_schedule = []

    # Calculate payments for each quarter of each year
    for year in range(years):
        for quarter in range(1, 5):  # 4 quarters in a year
            for month in range(3):  # 3 months in a quarter
                interest_payment = principal * monthly_interest_rate
                principal_payment = mortgage_payment + overpayment_amount - interest_payment
                principal -= principal_payment
                payment_schedule.append((year + 1, quarter, month + 1, mortgage_payment + overpayment_amount, interest_payment, principal_payment))

    # Display payment schedule
    print("\nPayment Schedule:")
    print("Year | Quarter | Month | Total Payment | Interest Payment | Principal Payment")
    for payment in payment_schedule:
        print("%4d | %7d | %5d | £%.2f | £%.2f | £%.2f" % payment)

mortgage_calculator()