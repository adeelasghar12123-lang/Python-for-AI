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

def load_from_file(expenses = expenses):
    try:
        with open("expenseDiary.txt","r") as file:
            expenses.append(json.load(file))
            return expenses
    except FileNotFoundError:
        return []
        






def add_expense(expenses):
    print()
    while True :
        try:
            expense_id = int(input("Expense Id : "))
            if expense_id < 1:
                raise ValueError
        except ValueError:
            print("Enter Valid expense Id ! ")
            continue
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
        
    dictionary_to_save = {"Expense Id" : expense_id , "Expense Name" : expense_name , "Amount" : amount , "Expense type" : expense_type}
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
        return
        








def search_expense():
    print()
    search_id = int(input("Search expense by Id : "))
    expenses = load_from_file()
    for exp in expenses:
        if exp["Expense Id"] == search_id:
            searched = exp
    if searched:
        print(f'{searched["Expense Id"]} : {searched["Expense Name"]} : {searched["Amount"]} : {searched["Expense type"]} ')
    else:
        print("Couldn't find any expense with this id !")










def delete_expense():
    print()
    expenses = load_from_file()
    no_of_expenses = len(expenses)
    if no_of_expenses == 0:
        print("No expenses in Diary to be deleted !")
    else:
        while True:
            try:
                to_be_deleted = int(input(f'Delete by Id (1-{no_of_expenses})'))
                if to_be_deleted > no_of_expenses:
                    raise ValueError
            except ValueError:
                print("Enter valid Id")
                continue
    expenses = [expense for expense in expenses if expense.get("Expense Id") != to_be_deleted]
    print("Deleted successfully !")



def show_stats():
    print()
    print("======== STATISTICS =========")
    print(f'Total Expenses : {total_expense()}')
    print(f'Average Expenses : {average_expenses()}')
    print()
    print(f'Highest Expense : {highest_expense()}')
    print(f'Lowest Expense : {lowest_expense()}')
    print()
    print(total_by_category())

def total_expense():
    expenses = load_from_file()
    total = 0
    for exp in expenses:
        total = exp["Amount"]
    return total



def average_expenses():
    expenses = load_from_file()
    no_of_expenses = len(expenses)
    average = total_expense()/no_of_expenses

def highest_expense():
    expenses = load_from_file()
    highest_ex =  max(expenses , key = lambda x:x["Amount"])
    print(f'{highest_ex["Expense Id"]} -- {highest_ex["Expense Name"]} -- {highest_ex["Amount"]} -- {highest_ex["Expense type"]}')


def lowest_expense():
    expenses = load_from_file()
    lowest_ex =  min(expenses , key = lambda x:x["Amount"])
    print(f'{lowest_ex["Expense Id"]} -- {lowest_ex["Expense Name"]} -- {lowest_ex["Amount"]} -- {lowest_ex["Expense type"]}')



def total_by_category():
    category_totals = {}
    expenses = load_from_file()

    for exp in expenses:
        category = exp["Expense type"]
        amount = exp["Amount"]
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    for category,total in category_totals:
        print(f'{category} -- {total}')



main_menu()









