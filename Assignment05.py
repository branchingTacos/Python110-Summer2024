# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Michael Kemery, 2024.07.27, outline main requirements
#   Michael Kemery, 2024.07.28, finish coding and test program
#   Michael Kemery, 2024.07.30, expiramented with JSON/Dictionary changes and added code
#                                  to look for data duplication
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.

student_data: list = []  # one row of student data
students: list = []  # a table of student data

csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

found: bool

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print(f"Error: '{FILE_NAME}' does not exist. \nFile must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')

#    print(students) - testing data is loaded into students[]

'''  commented out as using json rather than csv
for row in file.readlines():
    # Transform the data from the file
    student_data = row.split(',')
    student_data = [student_data[0], student_data[1], student_data[2].strip()]
    # Load it into our collection (list of lists)
    students.append(student_data)
file.close()
'''

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ").title()
            if not student_first_name.isalpha():
                raise ValueError("ERROR: The first name should not contain numbers.")

            student_last_name = input("Enter the student's last name: ").title()
            if not student_last_name.isalpha():
                raise ValueError("ERROR: The first name should not contain numbers.")

            course_name = input("Please enter the name of the course: ").title()

            ## let's add a "duplication detection" step to this branch.
            #  basically loop through students and look for exact match for all three
            #    variabels.  if exact match for all 3 then found = true
            found = False
            for student in students:
                if (student["FirstName"] == student_first_name and
                    student["LastName"] == student_last_name and
                    student["CourseName"] == course_name):
                    found = True
                    break
            ## give user information that studyent is already enrolled.
            if found:
                print(f"{student_first_name} {student_last_name} is already enrolled in {course_name}.")
            else:
                student_data = {"FirstName": student_first_name,
                                "LastName": student_last_name,
                                "CourseName": course_name}
                #  student_data = [student_first_name,student_last_name,course_name]
                students.append(student_data)
                print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

        except ValueError as e:
            print(e)
        #    # Optionally, you can add more instructions for the user here, if needed.
            print("Please enter the data again.")

        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            #print(student["First Name"], student["LastName"], student["GPA"])
            print(f"{student["FirstName"]}, {student["LastName"]},{student["CourseName"]}")
            print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file,indent=4) #using indent parameter to make file more readable
            file.close()

            print("-"*50)
            print("The following data was saved to file:")
            for student in students:
                print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
            print("-" * 50)
            print()
            print("Data Saved!")

        except TypeError as e:
            print("ERROR: Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
