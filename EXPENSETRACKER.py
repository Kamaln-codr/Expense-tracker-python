
#IMPORTING REQUIRED LIBRARIES
import json
import datetime

#PRINTING MENU INFORMATIONS
print("WELCOME TO EXPENSE TRACKER.PLS TYPE THE NUMBERS TO PERFORM RELATED FUNCTION BELOW:")
print("*"*45)
print("ADD EXPENSE ---> 1\nVIEW ALL EXPENSES ---> 2\nSHOW TOTAL SPENDING ---> 3\nFILTER EXPENSES ---> 4\nSAVE AND EXIT ---> 5")

#CHECKEING IF EXPENSE FILE EXISTS AND LOADING THE DATA
try:
    with open("expenses.json", "r") as project:
        expense = json.load(project)
except FileNotFoundError:
    expense = []

#CREATING USABLE FUNCTIONS
def addex():
    print("YOU CHOSE TO ADD EXPENSE!\nPlease give the following data:")
    d = datetime.datetime.today().strftime("%Y-%m-%d")
    a = float(input("ENTER AMOUNT SPENT:"))
    c = input("ENTER CATEGORY:")
    n = input("ENTER A NOTE (OPTIONAL):")
    expense.append({"Date": d, "Amount": a, "Category": c, "Note": n})

def viewex():
    print("YOU CHOSE TO VIEW ALL EXPENSES!")
    for exp in expense:
        print(f"Date: {exp['Date']}, Amount: {exp['Amount']}, Category: {exp['Category']}, Note: {exp['Note']}")

def filterex():
    print("YOU CHOSE TO FILTER EXPENSES!")
    category = input("ENTER CATEGORY TO FILTER BY:")
    for exp in expense:
        if exp["Category"].lower() == category.lower():
            print(f"Date: {exp['Date']}, Amount: {exp['Amount']}, Category: {exp['Category']}, Note: {exp['Note']}")

def totally():
    total = sum(exp["Amount"] for exp in expense)
    print(f"TOTAL SPENDING IS: {total}")

def savexit():
    print("CLOSING THE APP in 3 SECONDS...")
    with open("expenses.json", "w") as project:         #SAVING THE DATA
        json.dump(expense, project, indent=4)

#TAKING USER INPUTS
while True:
    try:                                                    #prints a custom text instead of passing an error
        inp = int(input("ENTER YOUR MENU NUMBER:"))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if inp == 1:
        addex()
    elif inp == 2:
        viewex()
    elif inp == 3:
        totally()
    elif inp == 4:
        filterex()
    elif inp == 5:
        savexit()
        break
    else:
        print("Invalid Input! Please try again.")