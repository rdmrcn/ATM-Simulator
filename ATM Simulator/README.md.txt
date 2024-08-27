# ATM Simulator

## Description
ATM Simulator is a simple Python application that emulates the basic functions of an ATM. It allows users to check their balance, deposit money, withdraw money, and exit the application. This project is created using Python and is designed to be run in Sublime Text.

## Features
- Check account balance
- Deposit money into the account
- Withdraw money from the account
- Simple PIN-based authentication

## How to Run

1. Ensure you have Python installed on your system.
2. Open the project in Sublime Text.
3. Press `Ctrl + B` or `F7` to run the script.

## Code Explanation

The script starts with a welcome message and prompts the user to insert their card and enter their PIN. It checks the entered PIN against a hardcoded value for simplicity. If the PIN is correct, the user is presented with a menu of options:

1. **Check Balance**: Displays the current balance.
2. **Deposit Money**: Allows the user to deposit an amount into their account.
3. **Withdraw Money**: Allows the user to withdraw an amount from their account.
4. **Exit**: Ends the ATM session.

If an invalid PIN is entered, the user is prompted to try again.

## Example Usage

```python
print("Welcome to the ATM Simulator! Please insert your card.")
# Output: Welcome to the ATM Simulator! Please insert your card.

# Prompt user to enter their PIN
entered_pin = input("Please enter your PIN: ")
