# ATM simulation with password protection using while loop

def display_menu():
    print("Welcome to MyBank ATM")
    print("1. Check Balance")
    print("2. Deposit")                                             
    print("3. Withdraw")
    print("4. Change Password")
    print("5. Exit")

balance = 1000  # Initial balance
password = "1234"  # Initial password

while True:
    print()  # Print a blank line for readability
    user_password = input("Enter your password: ")

    if user_password == password:
        while True:
            display_menu()

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                print(f"Your current balance is ${balance}")
            elif choice == '2':
                deposit_amount = float(input("Enter amount to deposit: "))
                balance += deposit_amount
                print(f"${deposit_amount} deposited successfully")
            elif choice == '3':
                withdraw_amount = float(input("Enter amount to withdraw: "))
                if withdraw_amount <= balance:
                    balance -= withdraw_amount
                    print(f"${withdraw_amount} withdrawn successfully")
                else:
                    print("Insufficient funds!")
            elif choice == '4':
                new_password = input("Enter new password: ")
                password = new_password
                print("Password changed successfully")
            elif choice == '5':
                print("Thank you for using MyBank ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    else:
        print("Incorrect password. Please try again.")
