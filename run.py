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
