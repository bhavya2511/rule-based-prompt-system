import time

def not_empty(func):
    def wrapper(data):
        if not data:
            raise ValueError("Dataset is empty")
        return func(data)
    return wrapper


def log(func):
    def wrapper(data):
        print("Processing dataset...")
        return func(data)
    return wrapper


def timer(func):
    def wrapper(data):
        start = time.time()
        result = func(data)
        print("Time:", round(time.time() - start, 4), "s")
        return result
    return wrapper


def salary_threshold(limit):
    def check(emp):
        return emp["salary"] >= limit
    return check



employees = [
    {"name": "Anil", "salary": 50000},
    {"name": "Meena", "salary": 80000}
]



@timer
@log
@not_empty
def bonus(data):
    return [
        {"name": e["name"], "bonus": e["salary"] * 0.1}
        for e in data
        if salary_threshold(70000)(e)
    ]




print("Result:", bonus(employees))
