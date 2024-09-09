class Student:
    def __init__(self, name, age, average_grade):
        self.name = name
        self.age = age
        self.average_grade = average_grade

    # Методы для установки значений
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_average_grade(self, average_grade):
        self.average_grade = average_grade

    # Методы для получения значений
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_average_grade(self):
        return self.average_grade

    # Метод для вывода информации о студенте
    def display_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Средний балл: {self.average_grade}")

    # Метод для оценки студента на основе среднего балла
    def evaluate_performance(self):
        if self.average_grade > 8:
            return "Отлично"
        elif 6 <= self.average_grade <= 8:
            return "Хорошо"
        elif 4 <= self.average_grade < 6:
            return "Удовлетворительно"
        else:
            return "Неудовлетворительно"

# Создание объектов класса Student
student1 = Student("Алексей", 20, 9.5)
student2 = Student("Мария", 19, 7.0)
student3 = Student("Иван", 22, 5.5)

# Установка значений свойств
student1.set_age(21)
student2.set_average_grade(8.5)

# Вывод информации о студентах
students = [student1, student2, student3]
for student in students:
    student.display_info()
    print(f"Оценка: {student.evaluate_performance()}\n")
