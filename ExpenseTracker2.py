import sys
import json

def main_menu():
    while True:
        print("======== Main Menu =========")
        print("1 : Add expense")
        print("2 : View expenses")
        print("3 : Search expenses")
        print("4 : Delete expense")
        print("5 : Show statistics")
        print("6 : Exit")

        try:
            command = int(input("Enter a command 1-6"))
            if command < 0 or command > 6 :
                raise ValueError
        except ValueError:
            print("Enter the correct command 1-6")
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
            sys.exit()
        input('\nPress "Enter" to return to the main menu.')

def add_expense():
    while True :
        
        expense_name = input("Expense Name : ").strip().title()
        try:
            amount = int(input("Amount : "))
            if amount < 0 :
                raise ValueError
        except ValueError:
            print("Invalid amount , reEnter details")
            continue
        
        expense_type = input("Expense type : ").strip().title()
        break
    dictionary_to_save = {"Expense Name" : expense_name , "Amount" : amount , "Expense type" : expense_type}
    with open("expenseDiary.txt","a") as file:
        file.write(json.dump(dictionary_to_save) + "\n")



        
def view_expense():
    print()
    print("==== Expenses ====")
    expenses = []
    with open("expenseDiary.txt","r") as file:
        for line in file:
            data = json.loads(line.strip())
            expenses.append(data)
    for exp in expenses:
        print(f'Expense Name : {exp["Expense Name"]}')
        print(f'Amount : {exp["Amount"]}')
        print(f'Expense type : {exp["Expense type"]}')
        print()
        


def search_expense():
    expenses = []
    exp_to_search = input("Search Category : ").strip().title()
    with open("expenseDiary.txt","r") as file:
        for line in file:
            data = json.loads(line.strip())
            expenses.append(data)
    for exp in expenses:
        if exp["Category"] == exp_to_search:
            print()
            print(f'Expense Name : {exp["Expense Name"]}')
            print(f'Amount : {exp["Amount"]}')
            print(f'Expense type : {exp["Expense type"]}')

            
