import re # import to check email format
import csv # import to save ratings in cvs file
from pathlib import Path # import path to check if file has already existed 

EMAIL_PATTERN = r"^[\w\.-]+@[\w\.-]+\.\w+$" # regex patern for a basic valid email 

def clean_name(name):
    return " ".join(part.capitalize() for part in name.strip().split()) # clean name

def valid_email_cheker(email):
    return re.match(EMAIL_PATTERN, email.strip()) is not None # check if email matches patern

def save_customer(name, email, filename="customers.txt"): # function to save customer details
    name = clean_name(name) 
    email = email.strip().lower() 

    if not valid_email_cheker(email): # check if email is invalid and if it is send error message
        raise ValueError("Invalid email")

    with open(filename, "a", encoding="utf-8") as file: # opens file in apend mode and writes customers details and data to files
        file.write(f"{name},{email}\n")


def main(): #m ain function where all the functions we made above gets called
    save_customer("alice smith", "alice@example.com")
    print("Customer saved") 


if __name__ == "__main__":
    main() # runs main function