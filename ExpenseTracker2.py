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
        
        expense_name = input("Expense Name : ")
        try:
            amount = int(input("Amount : "))
            if amount < 0 :
                raise ValueError
        except ValueError:
            print("Invalid amount , reEnter details")
            continue
        
        expense_type = input("Expense type : ")
        break
    dictionary_to_save = {"Expense Name" : expense_name , "Amount" : amount , "Expense type" : expense_type}
    with open("expenseDiary.txt","a") as file:
        file.write(json.dump(dictionary_to_save) + "\n")



        
        