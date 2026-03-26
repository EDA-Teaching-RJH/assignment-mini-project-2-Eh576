import re # import to check email format
import csv # import to save ratings in cvs file
from pathlib import Path # import path to check if file has already existed 

EMAIL_PATTERN = r"^[\w\.-]+@[\w\.-]+\.\w+$" # regex patern for a basic valid email 

def clean_name(name):
    return " ".join(part.capitalize() for part in name.strip().split()) # clean name

def valid_email_cheker(email):
    return re.match(EMAIL_PATTERN, email.strip()) is not None #check if email matches patern

def main():
    print(clean_name("  alice smith "))  # test name cleaning
    print(valid_email_cheker("alice@example.com"))  # test email validation


if __name__ == "__main__":
    main()