from Student import Student
def main():
    # Create a student
    test_student = Student("Truman", "Tiger", "Mizzou Stuff", 50, 4.5, 12345678)

    # Test the set credit hours method
    test_student.set_credit_hours(55)
    test_student.print_student_data()

    # Test update credit hours
    test_student.update_credit_hours(10)

main()