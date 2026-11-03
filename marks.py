
print("===================================")
print("     STUDENT MARKS MANAGEMENT")
print("===================================")

# Get Student Name
name = input("Enter student name: ").strip()

while not name:
    print("Error: Student name cannot be empty.")
    name = input("Enter student name: ").strip()


# Function to Get Valid Marks
def get_marks(subject):
    while True:
        try:
            marks = int(input(f"Enter {subject} marks (0-100): "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter numbers only.")


# Get Subject Marks
linux = get_marks("Linux")
aws = get_marks("AWS")
git = get_marks("Git")
python = get_marks("python")
SQL = get_marks("SQL")


# Calculate Total and Average
total = linux + aws + git + python + SQL
average = total / 5


# Display Student Details
print("\n===================================")
print("          STUDENT RESULT")
print("===================================")

print("Student Name  :", name)
print("Linux Marks   :", linux)
print("AWS Marks     :", aws)
print("Git Marks     :", git)
print("python  Marks :", python)
print("SQL Marks     :", SQL)

print("-----------------------------------")

print("Total Marks   :", total, "/ 500")
print("Average Marks :", round(average,4))

print("-----------------------------------")


# Check PASS or FAIL
if linux >= 35 and aws >= 35 and git >=35 and python >=35 and SQL >=35:
    print("Final Result  : PASS")
else:
    print("Final Result  : FAIL")

print("===================================")
print("       THANK YOU!")
print("===================================")

print("Thank you for using Student Marks Management") 
