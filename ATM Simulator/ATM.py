#Atm Simulator for python Sublime Version made in 10.05.2024 by Reha Demircan 
#to run Crtl + b or f7 
print("Welcome to the ATM Simulator! Please insert your card.")

# Initial account balance
balance = 1000

# Hardcoded user PIN for simplicity
user_pin = "1234"

# Prompt user to enter their PIN
entered_pin = input("Please enter your PIN: ")

# Check if the entered PIN matches the correct PIN
if entered_pin != user_pin:
    print("Invalid PIN. Please try again.")
    atm_on


# Start the ATM session loop
while atm_on:
    # Display the main menu options
    print("\nMain Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    # Get the user's choice
    choice = input("Please select an option: ")

    # Handle user's choice
    if choice == '1':
        print("Your current balance is: $" + str(balance))
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: $"))
        balance += amount  # Add the deposit to the balance
        print("$" + str(amount) + " has been successfully deposited.")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: $"))
        if amount > balance:
            print("Insufficient funds!")
        else:
            balance -= amount  # Subtract the withdrawal from the balance
            print("$" + str(amount) + " has been successfully withdrawn.")
    elif choice == '4':
        print("Thank you for using our service! Have a great day!")
        atm_on = False  # End the session
    else:
        print("Invalid selection. Please try again.")  # Handle invalid menu options
