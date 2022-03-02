
from queue import Empty
from unicodedata import name


class Course:

    def __init__(self,name):
        self.name = name
        self.price = "not set"
        self.type = "not set"
        self.entry_level = "beginner"
        self.students_capacity = 10
        self.students_id_enrolled = [1, 3, 5]
        self.appointments = []
        self.description = 'not set' 
        self.content = {}
    def get_name(self):
        return self.__name 

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self,price):
        self.price = price

    def get_type(self):
        return self.type

    def set_type(self,type):
        self.type = type

    def set_entry_level(self, entry_level):
        self.entry_level = entry_level

    def get_entry_level(self):
        return self.entry_level

    def get_students_capacity(self):
        return self.students_capacity - len(self.students_id_enrolled)

    def set_students_capacity(self,students_capacity):
        self.students_capacity = students_capacity

    def get_appointments(self):
        return self.appointments

    def set_appointments(self,appointment):
        if appointment not in self.appointments:
            self.appointments.append(appointment)

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content



class Professor:

    def __init__(self,name):
        self.name = name
        self.phd = "not set"
        self.course_given = "not set"
        self.Professor_review = "not set"
        self.Teaching_techniques = "not set"


    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def get_professor_phd(self):
        return self.phd

    def set_professor_phd(self,professor_phd):
        self.phd = professor_phd

    def get_Course_given(self):
        return self.course_given

    def set_Course_given(self,course_given):
        self.course_given = course_given
    

    def get_professor_review(self):
        return self.Professor_review

    def set_professor_review(self, Professor_review):
        self.Professor_review = Professor_review

    def get_teaching_techniques(self):
        return self.Teaching_techniques  

    def set_teaching_techniques(self, Teaching_techniques):
        self.Teaching_techniques = Teaching_techniques


#mostafa = Professor("mostafa")
#mostafa.set_professor_phd("doctor in engineering")
#print(mostafa.get_professor_phd())


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

    
