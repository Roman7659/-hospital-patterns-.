# Ваш основний файл, наприклад main.py

from factory_patient import PatientFactory

# Створення пацієнта за допомогою фабрики
new_patient = PatientFactory.create_patient("Іванов Іван", 30)
print(f"Створений пацієнт: {new_patient.name}, вік {new_patient.age} років")

