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