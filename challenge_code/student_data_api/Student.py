class Student():
    def __init__(self, first_name, last_name, major, credit_hours, gpa, id_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__id_number = id_number

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name
        return

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name
        return
    
    def get_major(self):
        return self.__major

    def set_major(self, new_major):
        self.__major = new_major
        return
    
    def get_credit_hours(self):
        return self.__credit_hours

    def set_credit_hours(self, new_credit_hours):
        self.__credit_hours = new_credit_hours
        return
    
    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, new_gpa):
        self.__gpa = new_gpa
        return

    def get_id_number(self):
        return self.__id_number

    def get_class_level(self):
        if self.__credit_hours >= 0 and self.__credit_hours <= 30:
            return "Freshman"
        if self.__credit_hours >= 31 and self.__credit_hours <= 60:
            return "Sophomore"
        if self.__credit_hours >= 61 and self.__credit_hours <= 90:
            return "Junior"
        if self.__credit_hours >= 91:
            return "Senior"


    def update_credit_hours(self, updated_hours):
        self.__credit_hours += updated_hours
        return
        
    def print_student_data(self):
        print(f"{self.__first_name} {self.__last_name}")
        print(f"Class Level: {self.get_class_level()}, Major: {self.__major}")
        print(f"GPA: {self.__gpa}, ID: {self.__id_number}")

    