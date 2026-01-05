
students_data = [
    {"name": "Asha", "score": 85},
    {"name": "Ravi", "score": 60},
    {"name": "John", "score": 82}
]

employees_data = [
    {"name": "Anil", "salary": 50000},
    {"name": "Meena", "salary": 80000},
    {"name": "Karan", "salary": 60000}
]

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_passed(self):
        return self.score >= 75


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

students = [Student(s["name"], s["score"]) for s in students_data]
employees = [Employee(e["name"], e["salary"]) for e in employees_data]

passed_students = [s.name for s in students if s.is_passed()]
high_paid_employees = [e.name for e in employees if e.salary > 60000]

average_score = sum(s.score for s in students) / len(students)
total_salary = sum(e.salary for e in employees)


print("Passed Students:", passed_students)
print("High Paid Employees:", high_paid_employees)
print("Average Score:", round(average_score, 1))
print("Total Salary:", total_salary)
