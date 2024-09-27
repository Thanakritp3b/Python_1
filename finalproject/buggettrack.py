import os
from datetime import datetime


# Function to clear the terminal screen
def clear_screen() -> None:
    if os.name == 'nt':
        os.system('cls')  # for Windows
    else:
        os.system('clear')  # for macOS/Linux


# Function to add an income source
def add_income(user_data: dict) -> None:
    """
    Function for adding income record

    Args:
        user_data: dict, An object that contains user data in a dictionary format

    Returns:
        None
    """
    source = input("Enter income source (e.g., salary, freelancing): ")
    while True:
        try:
            amount = float(input("Enter amount: "))
            break  # Valid input, exit loop
        except ValueError:
            print("Invalid amount! Please enter a valid number.")
    
    user_data['income'].append({'source': source, 'amount': amount})
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user_data['log'].append(f"Added income: {source} - {amount} at {timestamp}")

    print(f"Added income: {source} - {amount}")
    input("Press Enter to continue...")
    clear_screen()


# Function to add an expense with categories
def add_expense(user_data: dict) -> None:
    """
    Function for adding expense record

    Args:
        user_data: dict, An object that contains user data in a dictionary format

    Returns:
        None
    """

    item = input("Enter expense item (e.g., groceries, rent): ")
    
    while True:
        try:
            amount = float(input("Enter amount: "))
            break  # Valid input, exit loop
        except ValueError:
            print("Invalid amount! Please enter a valid number.")
    
    # Selecting a category for the expense
    categories = {
        '1': 'food',
        '2': 'shopping',
        '3': 'transition',
        '4': 'saving',
        '5': 'gift/invest',
        '6': 'other'
    }

    while True:
        print("Select a category for the expense:")
        for key, value in categories.items():
            print(f"{key}. {value.capitalize()}")
        
        category_choice = input("Choose a category (1-6): ")
        if category_choice in categories:
            category = categories[category_choice]
            break  # Valid input, exit loop
        else:
            print("Invalid choice! Please select a valid category (1-6).")
    
    user_data['expenses'].append({
        'item': item,
        'amount': amount,
        'category': category
    })
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user_data['log'].append(
        f"Added expense: {item} - {amount} in {category} at {timestamp}")

    print(f"Added expense: {item} - {amount} in {category}")
    input("Press Enter to continue...")
    clear_screen()


# Function to view income, expenses, and balance summary
def view_summary(user_data: dict) -> None:
    """
    Function for viewing summary data

    Args:
        user_data: dict, An object that contains user data in a dictionary format

    Returns:
        None
    """

    total_income = sum(item['amount'] for item in user_data['income'])
    total_expense = sum(item['amount'] for item in user_data['expenses'])
    balance = total_income - total_expense

    print("\n--- Budget Summary ---")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expense}")
    print(f"Balance: {balance}")

    # Calculate and display the percentage of each category
    if total_expense > 0:
        categories = ['food', 'shopping', 'transition', 'saving',
                      'gift/invest', 'other']
        category_totals = {category: 0 for category in categories}

        for expense in user_data['expenses']:
            category_totals[expense['category']] += expense['amount']

        print("\n--- Expense Breakdown by Category ---")
        for category in categories:
            amount = category_totals[category]
            percentage = (amount / total_expense) * 100 \
                if total_expense > 0 else 0
            print(f"{category.capitalize()}: {amount} ({percentage:.2f}%)")
    else:
        print("\nNo expenses recorded.")

    print("----------------------\n")


# Function to save data for all users to a file
def save_data(users_data: dict) -> None:
    """
    Function for saving data

    Args:
        users_data: dict, An object that contains user data for all users

    Returns:
        None
    """

    with open("user_budget_data.txt", "w") as f:
        for username, data in users_data.items():
            f.write(f"User: {username}\n")
            f.write("Income:\n")
            for income in data['income']:
                f.write(f"{income['source']}: {income['amount']}\n")
            f.write("Expenses:\n")
            for expense in data['expenses']:
                f.write(f"{expense['item']}: {expense['amount']} - "
                        f"{expense['category']}\n")
            f.write("Log:\n")
            for log_entry in data['log']:
                f.write(f"{log_entry}\n")

    print("Data saved to user_budget_data.txt")
    input("Press Enter to continue...")
    clear_screen()


# Function to handle user login or create a new account
def login(users_data: dict) -> str or None:
    """
    Function for user login or account creation

    Args:
        users_data: dict, A dictionary that contains user data

    Returns:
        String or None: The username of the logged-in user or None
    """

    print("1. Login")
    print("2. Create a new account")

    while True:
        choice = input("Choose an option (1-2): ")
        if choice == '1':
            username = input("Enter your username: ")
            if username in users_data:
                print(f"Welcome back, {username}!")
                return username
            else:
                print("Username not found.")
                return None
        elif choice == '2':
            username = input("Enter a new username: ")
            if username in users_data:
                print("Username already exists. Try again.")
            else:
                users_data[username] = {'income': [], 'expenses': [], 'log': []}
                print(f"Account created for {username}.")
                return username
        else:
            print("Invalid choice! Please select 1 or 2.")


# Function to view the log of transactions
def view_log(user_data: dict) -> None:
    """
    Function to view transaction logs

    Args:
        user_data: dict, A dictionary containing the user's data

    Returns:
        None
    """

    print("\n--- Transaction Log ---")

    if not user_data['log']:
        print("No transactions recorded.")
    else:
        for entry in user_data['log']:
            print(entry)

    print("----------------------\n")
    input("Press Enter to continue...")
    clear_screen()


# Main program
def main() -> None:
    """
    Main function

    Args:
        None

    Returns:
        None
    """

    users_data = load_data()
    current_user = None

    while not current_user:
        current_user = login(users_data)

    while True:
        clear_screen()  # Clear screen before showing the summary
        print(f"\nLogged in as: {current_user}")
        view_summary(users_data[current_user])  # Always show the summary

        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Log")
        print("4. Save Data")
        print("5. Logout")
        print("6. Quit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_income(users_data[current_user])
        elif choice == '2':
            add_expense(users_data[current_user])
        elif choice == '3':
            view_log(users_data[current_user])
        elif choice == '4':
            save_data(users_data)
        elif choice == '5':
            current_user = None
            while not current_user:
                save_data(users_data)
                current_user = login(users_data)
        elif choice == '6':
            save_data(users_data)
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 6.")
            input("Press Enter to continue...")


# Function to load data for all users from a file
def load_data() -> dict:
    """
    Function for loading user data from a file

    Args:
        None

    Returns:
        users_data: dict, A dictionary of user data
    """

    users_data = {}
    try:
        with open("user_budget_data.txt", "r") as f:
            current_user = None
            current_section = None
            for line in f:
                if line.startswith("User:"):
                    current_user = line.split(":")[1].strip()
                    users_data[current_user] = {'income': [],
                                                'expenses': [],
                                                'log': []}
                elif line.startswith("Income"):
                    current_section = 'income'
                elif line.startswith("Expenses"):
                    current_section = 'expenses'
                elif line.startswith("Log"):
                    current_section = 'log'
                else:
                    if current_section == 'income':
                        source, amount = line.split(": ")
                        users_data[current_user]['income'].append({
                            'source': source.strip(),
                            'amount': float(amount.strip())
                        })
                    elif current_section == 'expenses':
                        item, rest = line.split(": ")
                        amount, category = rest.split(" - ")
                        users_data[current_user]['expenses'].append({
                            'item': item.strip(),
                            'amount': float(amount.strip()),
                            'category': category.strip()
                        })
                    elif current_section == 'log':
                        users_data[current_user]['log'].append(line.strip())
        print("Data loaded from user_budget_data.txt")

    except FileNotFoundError:
        print("No saved data found, starting fresh.")

    input("Press Enter to continue...")
    clear_screen()
    return users_data


# Run the program
if __name__ == "__main__":
    main()
