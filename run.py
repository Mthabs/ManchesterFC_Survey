import gspread
from google.oauth2.service_account import Credentials
import re
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Manchester FC - Survey').sheet1
"""
def add_row():
    while True:
        name = input("Enter name: ").strip()
        if not all(c.isalpha() or c.isspace() for c in name):
            print("Invalid name. Please enter letters only.")
            continue
        brand_score = validate_score("Enter brand score (1-10): ")
        coach_score = validate_score("Enter coach score (1-10): ")
        players_score = validate_score("Enter players score (1-10): ")
        SHEET.append_row([name, brand_score, coach_score, players_score])
        print("Row added successfully.")
        break

def validate_score(prompt):
    while True:
        score = input(prompt).strip()
        if not score.isdigit():
            print("Invalid score. Please enter a number.")
            continue
        score = int(score)
        if score < 1 or score > 10:
            print("Invalid score. Please enter a number between 1 and 10.")
            continue
        return score        

def main():
    while True:
        print("1. Add a row")
        print("2. Quit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_row()
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == '__main__':
    main()

"""
def calculate_average():
    data = SHEET.get_all_values()
    new_data = [data[0][1:],]  # exclude name and age columns
    new_data.extend([row[1:] for row in data[1:]])

    averages = [["Category", "Average"]]
    for category in ["Brand score", "Coach score", "Players score"]:
        category_data = new_data[1:]
        category_scores = [int(row[new_data[0].index(category)]) for row in category_data]
        category_average = sum(category_scores) / len(category_scores)
        averages.append([category, str(int(category_average))])

    # Transpose the averages list to get the output in row format
    row_format = list(map(list, zip(*averages)))
    return row_format

def append_to_sheet2():
    sheet = GSPREAD_CLIENT.open('Manchester FC - Survey').worksheet('Sheet2')
    data = calculate_average()
    last_row = len(sheet.get_all_values()) + 1  # add 1 to account for the header row
    update_range = f"B{last_row}:E{last_row}"  # Update the range to include three columns
    sheet.update(update_range, data[1:])  # Update with the data in row format excluding the header row
    return "Average scores updated successfully to Sheet2!!!"
append_to_sheet2()
