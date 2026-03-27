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

def add_rating(name, rating, filename="ratings.csv"): # function to store ratings
    with open(filename, "a", newline="", encoding="utf-8") as file: # opens CSV file in append mode 
        writer = csv.writer(file) # creates CSV writter
        writer.writerow([clean_name(name), rating]) # writes customers rating

def get_average_rating(filename="ratings.csv"):
    with open(filename, "r", newline="", encoding="utf-8") as file:  # opens CSV file in read mode and reads CSV
        reader = csv.reader(file)
        ratings = [int(row[1]) for row in reader]

    if len(ratings) == 0:
        return 0

    return round(sum(ratings) / len(ratings), 2) # calculates average

class Person: # base class for a person
    def __init__(self, name):
        if not name.strip(): 
            raise ValueError("Name required") # check if name is empty if empty it raises error 
        self.name = clean_name(name)

    def __str__(self):  
        return self.name  # returns name wehn object is printed


def main(): #m ain function where all the functions we made above gets called
    save_customer("alice smith", "alice@example.com")
    add_rating("alice smith", 8) # add first rating 
    add_rating("joseph body", 9) # add second rating 

    print("Average rating:", get_average_rating()) # print average rating 

if __name__ == "__main__":
    main() # runs main function