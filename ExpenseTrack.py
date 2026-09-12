while True:
    try:
        number_of_expenses = int(input("How many expenses you want to enter ? "))
        if number_of_expenses <= 0 :
            raise TypeError
    except TypeError:
        print("Enter a valid Number (1-1000) ")
    else:
        break



expenses = []
def take_expense_input():
    
    for i in range(number_of_expenses):
        expense_name = input("Expense Name : ")
        while True:
            try:
                expense_amount = int(input("Amount : "))
                
            except ValueError:
                print("Enter Numerical Amount !")
            else:
                break
        expenses.append({"Expense Name" : expense_name , "Amount" : expense_amount})


# DISPLAY EVERY EXPENSE
def display_expenses(expenses):
    for ex in expenses:
        print(ex["Expense Name"],ex["Amount"])

# TOTAL SPENDINGS
def total_spendings(expenses):
    total_spendings = 0
    for ex in expenses:
        total_spendings += ex["Amount"]
    return total_spendings

# AVERAGE EXPENSE
def average():
    return total_spendings()/number_of_expenses

# HIGHEST
def Highest_expense(expenses):
    return max(expenses, key=lambda x: x["Amount"])

# LOWEST
def Lowest_expense(expenses):
    return min(expenses, key=lambda x: x["Amount"])


#SPENDING LEVEL
def Spending_level():
    total = total_spendings()
    if total < 5000 :
        print("Spending Level - Low spendings.")
    elif total < 10000:
        print("Spending level - Moderate spendings")
    else:
        print("Spending level - High spendings")



take_expense_input()
display_expenses(expenses)
print(f'Total Spendings : {total_spendings()}')
print(f'Average : {average()}')
h_ex = Highest_expense(expenses)
print(f'Highest Expense : {h_ex["Expense Name"]}-{h_ex["Amount"]}')

l_ex = Lowest_expense(expenses)
print(f'Lowest Expense : {l_ex["Expense Name"]}-{l_ex["Amount"]}')
Spending_level()