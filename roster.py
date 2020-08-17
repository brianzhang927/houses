from sys import argv, exit
from cs50 import SQL


# Check valid input
if len(argv) != 2:
    print("Usage: python roster.py house")
    exit(1)


# Connect to database
db = SQL("sqlite:///students.db")

# Produce roster
people = db.execute(f"SELECT first, middle, last, birth FROM students WHERE house = '{argv[1]}' ORDER BY last, first")

# Print roster
for row in people:
    print(row["first"], end=" ")

    if (row["middle"]) != None:
        print(row["middle"], end=" ")

    print(row["last"], end=", ")
    print("born", row["birth"])