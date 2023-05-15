import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Manchester FC - Survey')

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
        return
test = add_row()
print(test)