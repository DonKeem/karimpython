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