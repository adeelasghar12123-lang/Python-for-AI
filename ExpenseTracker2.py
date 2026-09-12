import sys
import re

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
        