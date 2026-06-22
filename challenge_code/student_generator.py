from Student import Student
# Create student objects from the data loaded from students.csv
# Place in a list
# Print each students data
def main():
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
        id_number = student_data[5]

        student_object = Student(student_first, student_last, major, credit_hours, gpa, id_number)

        students.append(student_object)
    
    for student in students:
        student.print_student_data()


main()
