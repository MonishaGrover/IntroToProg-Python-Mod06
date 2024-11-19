# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates the use of functions, classes and separation of concerns pattern
# Change Log: (Who, When, What)
#   Monisha Grover,11/16/2030,Created Script
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
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = ''  # Holds combined string data in a json format.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

class FileProcessor:
    """Processes data to and from a file."""

    @staticmethod
    def read_data_from_file(file_name:str, students:list):
        """
        The function reads in a json file and returns the result
        :param file_name: The name of the json file
        :return: Alist of dictionaries containing the data from the json file
        """
        try:
            with open(file_name,"r") as f:
                data = json.load(f)
        except FileNotFoundError as e:
            IO.output_error_messages("File not found", e)
        except Exception as e:
            IO.output_error_messages("Something went wrong", e)

    @staticmethod
    def write_data_to_file(file_name:str, students):
        """writes data from a list of dictionaries to a json file"""
        with open(file_name,"w") as f:
            json.dump(students,f)
        print("Wrote to file successfully")

class IO:
    """Handles Input and Output for the program."""

    @staticmethod
    def output_error_messages(message:str, error:Exception = None):
        """Displays error messages to the user"""
        print(message, end="\n\n")
        if error is not None:
            print("--Technical Error Message---")
            print(error, error.__doc__, type(error), sep='\n')

    def output_menu(menu:str):
        """Displays the main menu to the user"""
        print(MENU)

    def output_student_courses(student_data:list):
        """displays all student registrations."""
        if student_data:
            print("\nRegistered Students and courses:")
            for student in student_data:
                print(f"{student["FirstName"]} {student["LastName"]} - Course: {student["CourseName"]}")
        else:
            print("No data available. Please register a student first.")

    @staticmethod
    def input_menu_choice():
        """Prompts the user to select an option from the menu"""
        try:
            menu_choice = input("What would you like to do: ")
            if menu_choice not in ["1","2","3","4"]:
                raise ValueError("Invalid choice. Please try again.")
            return menu_choice
        except ValueError as e:
            IO.output_error_messages(str(e))
            return

    @staticmethod
    def input_student_data(student_data:list):
        """prompts the user to input a student's first name, last name and course name"""
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(str(e))
        except Exception as e:
            IO.output_error_messages("An unexpected error occurred while entering student data.", str(e))

# Main Program
menu_choice = ""

if __name__ == "__main__":
    FileProcessor.read_data_from_file(FILE_NAME, students)

    while menu_choice != "4":
        IO.output_menu(menu_choice)
        menu_choice = IO.input_menu_choice()

        if menu_choice == "1":
            IO.input_student_data(students)
        elif menu_choice == "2":
            IO.output_student_courses(students)
        elif menu_choice == "3":
            FileProcessor.write_data_to_file(FILE_NAME, students)
        elif menu_choice == "4":
            print("Program ended. Thank you!")

