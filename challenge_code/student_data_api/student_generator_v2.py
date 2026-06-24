from Student import Student
# Create student objects from the data loaded from students.csv
# Place in a list
# Print each students data
"""
Function to return a list of student objects
input: None
Output: List of student objects
"""
def load_students()-> list[Student]:
    data_file = open("students.csv", "r")
    students = []
    line_number = 0
    for line_of_data in data_file:
        line_number += 1

        if line_number == 1:
            continue
        student_data = line_of_data.split(",")
        # Handle errors in the data format. line_of_data should have 6 items
        # if error in format then write to a log file
        try:
            if len(student_data) != 6:
                raise Exception(f"Error on line {line_number} of the file. Data has {len(student_data)} items, but should have 6.\n")
        except Exception as error:
            continue

        student_first = student_data[0]
        student_last = student_data[1]
        major = student_data[2]
        credit_hours = int(student_data[3])
        gpa = float(student_data[4])
        id_number = student_data[5].strip()

        student_object = Student(student_first, student_last, major, credit_hours, gpa, id_number)

        students.append(student_object)
    
    return students
"""
Function to convert student objects into student dicitonaries
Input: List of student objects
Output: List of student dictionaries
"""

def student_to_dictionary(list_of_students: list[Student])-> list[dict]:
    # Create an empty list to store the dictionaries
    student_dictionary_list = []

    # Loop through the list and write each student's data to a dictionary
    for student in list_of_students:
        # Create an empty dictionary
        student_dictionary = {}

        # Make entries into the dictionary using the student properties
        # First name, last name, major, gpa, class, id
        student_dictionary['first_name'] = student.get_first_name()
        student_dictionary['last_name'] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_gpa()
        student_dictionary['class'] = student.get_class_level()
        student_dictionary['id'] = student.get_id_number()
        # Append the dicitonary to the list of dictionaries
        student_dictionary_list.append(student_dictionary)
        # Return the list of dictionaries
    return student_dictionary_list

"""
Create a function to get student dictionaries
Input: none
Output: A list of student dictionaries
"""
def get_student_dictionaries():
    # Get a list of students
    student_list = load_students()

    # Get a list of student dictionaries
    student_dictionaries = student_to_dictionary(student_list)

    return student_dictionaries

    
