from sys import argv, exit
from csv import DictReader
from cs50 import SQL


# Check valid input
if len(argv) != 2:
    print("Usage: python import.py data.csv")
    exit(1)


# Connect to database
db = SQL("sqlite:///students.db")

with open(argv[1], "r") as file:
    
    reader = DictReader(file)

    # Add students to database
    for row in reader:
        name = row["name"].split()
        
        if len(name) == 3:
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       name[0], name[1], name[2], row["house"], row["birth"])
        
        elif len(name) == 2:
            db.execute("INSERT INTO students (first, last, house, birth) VALUES(?, ?, ?, ?)",
                       name[0], name[1], row["house"], row["birth"])
