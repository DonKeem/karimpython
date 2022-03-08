class Student:
    def __init__(self,name):
        self.name = name
        self.student_level = "not set"
        self.courses_taken = {}
        self.courses_in_process = "not set"


    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def get_student_level(self):
        return self.student_level

    def set_student_level(self,Student_level):
        self.student_level = Student_level
    
    def get_courses_taken(self):
        return self.courses_taken

    def set_courses_taken(self,Course_taken):
        self.courses_taken = Course_taken


    def get_courses_in_progress(self):
        return self.courses_in_process

    def set_courses_in_progress(self, Courses_in_progress):
        self.courses_in_process = Courses_in_progress