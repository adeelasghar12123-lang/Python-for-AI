import sys
import json

def main_menu():
    while True:
        print("\n======== Main Menu =========")
        print("1 : Add expense")
        print("2 : View expenses")
        print("3 : Search expenses")
        print("4 : Delete expense")
        print("5 : Show statistics")
        print("6 : Exit")

        try:
            command = int(input("Enter a command 1-6: "))
            if command < 1 or command > 6 :
                raise ValueError
        except ValueError:
            print("Enter a correct command from 1-6.")
            continue

        if command == 1:
            add_expense(expenses)
        elif command == 2:
            view_expense()
        elif command == 3:
            search_expense()
        elif command == 4:
            delete_expense()
        elif command == 5:
            show_stats()
        else:
            print("Goodbye!")
            sys.exit()
            
        input('\nPress "Enter" to return to the main menu.')








expenses = []

def save_to_file(expenses):
    try:
        with open("expenseDiary.txt","w") as file:
            json.dump(expenses,file,indent=4)
    except json.JSONDecodeError:
        print("Expense file is corrupted.")
        return []

def load_from_file():
    with open("expenseDiary.txt","r") as file:
        expenses.append(json.loads(file))
        return expenses
        






def add_expense(expenses):
    print()
    while True :
        expense_name = input("Expense Name : ").strip().title()
        try:
            amount = float(input("Amount : "))
            if amount < 1 :
                raise ValueError
        except ValueError:
            print("Invalid amount, please re-enter details.")
            continue
        
        expense_type = input("Expense type : ").strip().title()
        break
        
    dictionary_to_save = {"Expense Name" : expense_name , "Amount" : amount , "Expense type" : expense_type}
    expenses.append(dictionary_to_save)
    save_to_file(expenses)    
    print("Expense added successfully!")





def view_expense():
    print("\n==== Expenses ====")
    expenses = load_from_file()
    if expenses:
        for exp in expenses:
            print()
            print(f'Expense Name : {exp["Expense Name"]}')
            print(f'Amount : {exp["Amount"]}')
            print(f'Expense Type : {exp["Expense type"]}')
    else:
        print("No expenses to show !")
        return
        








def search_expense():
    print()
    expense_to_search = input

def delete_expense():
    print()
    exp_to_delete = input("Delete Expense Name : ").strip().title()
    expenses = []
    
    try:
        with open("expenseDiary.txt", "r") as file:
            for line in file:
                data = json.loads(line.strip())
                expenses.append(data)
    except FileNotFoundError:
        print("No expenses recorded yet.")
        return

    # Filter out the expense the user wants to delete
    original_count = len(expenses)
    expenses = [ex for ex in expenses if ex["Expense Name"] != exp_to_delete]
    
    if len(expenses) == original_count:
        print("Expense not found.")
        return

    # Open file in "w" mode ONCE to overwrite it, then loop through and write each dict
    with open("expenseDiary.txt", "w") as file:
        for exp in expenses:
            file.write(json.dumps(exp) + "\n")
            
    print(f"'{exp_to_delete}' has been deleted.")

def show_stats():
    print("\n==== Statistics ====")
    expenses = []
    
    # Must open in "r" mode to read stats, not "w" mode
    try:
        with open("expenseDiary.txt", "r") as file:
            for line in file:
                data = json.loads(line.strip())
                expenses.append(data)
    except FileNotFoundError:
        print("No expenses recorded yet.")
        return
        
    if not expenses:
        print("No data available to calculate statistics.")
        return
        
    total_amount = sum(exp["Amount"] for exp in expenses)
    total_entries = len(expenses)
    
    print(f"Total number of expenses: {total_entries}")
    print(f"Total money spent: ${total_amount}")

if __name__ == "__main__":
    main_menu()