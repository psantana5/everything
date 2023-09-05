import json
from datetime import datetime
import pandas as pd
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


expenses = []

# Load saved data
try:
    with open('expenses.json', 'r') as f:
        expenses = json.load(f)
except FileNotFoundError:
    print("No saved data found. Starting fresh.")

def save_expenses():
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f)

def addexpense():
    add_expense = str(input("What is the name of the expense you wish to add? "))
    expense_price = int(input("How much is the expense? "))
    category = str(input("What category is this expense? e.g: Entertainment, Shopping, etc. "))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    confirmation = str(input("Do you wish to add the expense now? y/n "))
    
    if confirmation.lower() == 'y':
        new_expense = {'name': add_expense, 'price': expense_price, 'category': category, 'timestamp': timestamp}
        expenses.append(new_expense)
        save_expenses()
    else:
        print("Expense not added.")
    menu()

def listexpenses():
    seecurrent = str(input("Do you wish to see your current expenses? y/n "))
    
    if seecurrent.lower() == "y":
        for i, expense in enumerate(expenses):
            print(f"{i+1}. Name: {expense['name']}, Price: {expense['price']}, Category: {expense['category']}, Timestamp: {expense['timestamp']}")
    else:
        print("Option not recognized")
    menu()

def deleteexpenses():
    print("Enumerating current expenses")
    for i, expense in enumerate(expenses):
        print(f"{i+1}. Name: {expense['name']}, Price: {expense['price']}, Category: {expense['category']}")
        
    deleteexpense = str(input("What is the name of the expense you want to delete? "))
    for i, expense in enumerate(expenses):
        if expense['name'] == deleteexpense:
            del expenses[i]
            save_expenses()
            print("Expense deleted")
            break
    
    choice_deletion = str(input("Do you wish to see the current expenses? y/n "))
    if choice_deletion.lower() == "y":
        listexpenses()
    else:
        print("Option not found")
        menu()

def total_expenses():
    total = sum(expense['price'] for expense in expenses)
    print(f"Total Expenses: {total}")
    menu()

def expenses_by_category():
    categories = {}
    for expense in expenses:
        if expense['category'] in categories:
            categories[expense['category']] += expense['price']
        else:
            categories[expense['category']] = expense['price']
    for category, total in categories.items():
        print(f"{category}: {total}")
    menu()

def edit_expense():
    print("Enumerating current expenses")
    for i, expense in enumerate(expenses):
        print(f"{i+1}. Name: {expense['name']}, Price: {expense['price']}, Category: {expense['category']}")
        
    edit_expense_index = int(input("Enter the number of the expense you want to edit: ")) - 1
    if 0 <= edit_expense_index < len(expenses):
        edit_field = str(input("Which field do you want to edit? (name/price/category) "))
        if edit_field in ['name', 'price', 'category']:
            new_value = input(f"Enter the new value for {edit_field}: ")
            if edit_field == 'price':
                new_value = int(new_value)
            expenses[edit_expense_index][edit_field] = new_value
            save_expenses()
            print("Expense updated.")
        else:
            print("Invalid field.")
    else:
        print("Invalid expense number.")
    menu()
def search_expenses():
    print("Search by:")
    print("1. Name")
    print("2. Category")
    print("3. Price Range")
    search_option = int(input("Select a search option: "))
    
    if search_option == 1:
        name_query = str(input("Enter the name to search for: "))
        found_expenses = [expense for expense in expenses if name_query.lower() in expense['name'].lower()]
    elif search_option == 2:
        category_query = str(input("Enter the category to search for: "))
        found_expenses = [expense for expense in expenses if category_query.lower() in expense['category'].lower()]
    elif search_option == 3:
        lower_bound = int(input("Enter the lower bound of the price range: "))
        upper_bound = int(input("Enter the upper bound of the price range: "))
        found_expenses = [expense for expense in expenses if lower_bound <= expense['price'] <= upper_bound]
    else:
        print("Invalid option.")
        menu()
    
    if not found_expenses:
        print("No expenses found.")
    else:
        print("Found Expenses:")
        for i, expense in enumerate(found_expenses):
            print(f"{i+1}. Name: {expense['name']}, Price: {expense['price']}, Category: {expense['category']}, Timestamp: {expense['timestamp']}")
    
    menu()
def manual_backup():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_file = f"backup_{timestamp}.json"
    
    with open(backup_file, 'w') as f:
        json.dump(expenses, f)
    
    print(f"Backup successful. Data saved to {backup_file}")
    menu()

def export_to_excel():
    df = pd.DataFrame(expenses)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    excel_file = f"expenses_{timestamp}.xlsx"
    df.to_excel(excel_file, index=False)
    print(f"Data successfully exported to {excel_file}")
    menu()

def import_from_excel():
    excel_file = input("Please enter the name of the Excel file to import (e.g., expenses.xlsx): ")
    
    try:
        df = pd.read_excel(excel_file)
        global expenses  
        expenses = df.to_dict(orient='records')  
        print("Data successfully imported!")
    except FileNotFoundError:
        print(f"File {excel_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
    menu()

def generate_pdf_report():
    # Create a PDF document
    pdf = SimpleDocTemplate(
        "Expense_Report.pdf",
        pagesize=A4
    )
    
    # Create a list to store PDF elements
    elements = []
    
    # Generate a report for each category
    categories = {expense['category'] for expense in expenses}
    for category in categories:
        category_expenses = [expense for expense in expenses if expense['category'] == category]
        total_expense = sum(expense['price'] for expense in category_expenses)
        
        # Create a table for each category
        data = [["Name", "Price"]]
        for expense in category_expenses:
            data.append([expense['name'], expense['price']])
        
        data.append(["Total", total_expense])
        
        # Create a Table element
        t = Table(data)
        
        # Add Table Style
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        # Add category header and table to PDF elements
        elements.append(f"Category: {category}")
        elements.append(t)
    
    # Generate PDF
    pdf.build(elements)
    
    print("PDF Report generated: Expense_Report.pdf")
    menu()

def menu():
    print("Welcome to the expense tracker application")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Delete Expenses")
    print("4. Total Expenses")
    print("5. Expenses by Category")
    print("6. Edit Expense")
    print("7. Search Expenses")
    print("8. Manual Backup")
    print("9. Export to Excel")
    print("10. Import from Excel")
    print("11. Generate PDF Report")
    print("0. Exit")
    
    chosen_option = int(input("What do you wish to do: "))
    
    if chosen_option == 1:
        addexpense()
    elif chosen_option == 2:
        listexpenses()
    elif chosen_option == 3:
        deleteexpenses()
    elif chosen_option == 4:
        total_expenses()
    elif chosen_option == 5:
        expenses_by_category()
    elif chosen_option == 6:
        edit_expense()
    elif chosen_option == 7:
        search_expenses()
    elif chosen_option == 0:
        exit()
    elif chosen_option == 9:
        export_to_excel()
    elif chosen_option == 10:
        import_from_excel()
    elif chosen_option == 11:
        generate_pdf_report()
    else:
        print("Invalid option.")
        menu()

menu()
