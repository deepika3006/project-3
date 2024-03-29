import os
import datetime

# Function to load expense data from file
def load_expenses(filename):
    expenses = {}
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                category, amount, description = line.strip().split(',')
                if category not in expenses:
                    expenses[category] = []
                expenses[category].append((float(amount), description))
    return expenses

# Function to save expense data to file
def save_expenses(expenses, filename):
    with open(filename, 'w') as file:
        for category, items in expenses.items():
            for amount, description in items:
                file.write(f"{category},{amount},{description}\n")

# Function to record new expense
def record_expense(expenses):
    category = input("Enter category of expense: ")
    amount = float(input("Enter amount spent: "))
    description = input("Enter a brief description: ")
    if category not in expenses:
        expenses[category] = []
    expenses[category].append((amount, description))
    print("Expense recorded successfully!")

# Function to display monthly expense summary
def monthly_summary(expenses):
    month = datetime.datetime.now().strftime("%B")
    total_expenses = sum(sum(amount for amount, _ in items) for items in expenses.values())
    print(f"Summary for {month}:")
    print(f"Total expenses: ${total_expenses:.2f}")
    for category, items in expenses.items():
        category_total = sum(amount for amount, _ in items)
        print(f"{category.capitalize()}: ${category_total:.2f}")

# Main function
def main():
    filename = "expenses.txt"
    expenses = load_expenses(filename)
    while True:
        print("\nExpense Tracker")
        print("1. Record Expense")
        print("2. Monthly Summary")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            record_expense(expenses)
        elif choice == '2':
            monthly_summary(expenses)
        elif choice == '3':
            save_expenses(expenses, filename)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
