class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PatientFactory:
    @staticmethod
    def create_patient(name, age):
        return Patient(name, age)
