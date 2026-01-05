import time

def validate_prompt(func):
    def wrapper(self, prompt):
        if len(prompt.text) < 5:
            raise ValueError("Invalid prompt")
        return func(self, prompt)
    return wrapper

def log_prompt(func):
    def wrapper(self, prompt):
        print("Processing prompt...")
        return func(self, prompt)
    return wrapper

def timer(func):
    def wrapper(self, prompt):
        start = time.time()
        result = func(self, prompt)
        print("Time:", round(time.time() - start, 4))
        return result
    return wrapper
