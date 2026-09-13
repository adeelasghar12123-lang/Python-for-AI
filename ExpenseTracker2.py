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
            add_expense()
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

def save_to_file(expenses):
    with open("expenseDiary.txt","w") as file:
        json.dump(expenses, file, indent=4)

def load_from_file():
    try:
        with open("expenseDiary.txt", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def add_expense():
    print()
    expenses = load_from_file()
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

    new_id = max([exp.get("Expense Id", 0) for exp in expenses], default=0) + 1
        
    dictionary_to_save = {"Expense Id" : new_id , "Expense Name" : expense_name , "Amount" : amount , "Expense type" : expense_type}
    expenses.append(dictionary_to_save)
    save_to_file(expenses)    
    print("Expense added successfully!")

def view_expense():
    print("\n==== Expenses ====")
    expenses = load_from_file()
    if expenses:
        for exp in expenses:
            print()
            print(f'{exp["Expense Id"]} : {exp["Expense Name"]} : {exp["Amount"]} : {exp["Expense type"]} ')
    else:
        print("No expenses to show !")

def search_expense():
    print()
    while True:
        try:
            search_id = int(input("Search expense by Id : "))
            break
        except ValueError:
            print("Enter valid numerical Id !")
            
    expenses = load_from_file()
    searched = None
    for exp in expenses:
        if exp["Expense Id"] == search_id:
            searched = exp
            break # Can stop searching once found
            
    if searched:
        print(f'{searched["Expense Id"]} : {searched["Expense Name"]} : {searched["Amount"]} : {searched["Expense type"]} ')
    else:
        print("Couldn't find any expense with this id !")

def delete_expense():
    print()
    expenses = load_from_file()
    original_count = len(expenses)
    
    if original_count == 0:
        print("No expenses in Diary to be deleted !")
        return
    
    while True:
        try:
            # FIXED: Removed len() around the variable
            to_be_deleted = int(input('Delete by Id: '))
            break
        except ValueError:
            print("Enter valid numerical Id")
            continue
            
    expenses = [expense for expense in expenses if expense.get("Expense Id") != to_be_deleted]
    
    if len(expenses) == original_count:
        print("Expense not found !")
    else:
        save_to_file(expenses)
        print("Deleted successfully !")

def show_stats():
    expenses = load_from_file()
    if not expenses:
        print("No expenses to show stats")
        return
        
    print()
    print("======== STATISTICS =========")
    print(f'Total Expenses : {total_expense(expenses)}')
    print(f'Average Expenses : {average_expenses(expenses):.2f}')
    print()
    highest_expense(expenses)
    print()
    lowest_expense(expenses)
    print()
    total_by_category(expenses)

def total_expense(expenses):
    total = 0
    for exp in expenses:
        total += exp["Amount"]
    return total

def average_expenses(expenses):
    average = total_expense(expenses)/len(expenses)
    return average

def highest_expense(expenses):
    highest_ex = max(expenses , key = lambda x:x["Amount"])
    print("===== Highest Expense =====")
    print(f'{highest_ex["Expense Id"]} -- {highest_ex["Expense Name"]} -- {highest_ex["Amount"]} -- {highest_ex["Expense type"]}')

def lowest_expense(expenses):
    lowest_ex = min(expenses , key = lambda x:x["Amount"])
    print("===== Lowest Expense =====")
    print(f'{lowest_ex["Expense Id"]} -- {lowest_ex["Expense Name"]} -- {lowest_ex["Amount"]} -- {lowest_ex["Expense type"]}')

def total_by_category(expenses):
    category_totals = {}

    for exp in expenses:
        category = exp["Expense type"]
        amount = exp["Amount"]
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
            
    for category,total in category_totals.items():
        print(f'{category} -- {total}')

if __name__ == "__main__":
    main_menu()