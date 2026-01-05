from models import Prompt
from rules import category_filter
from executor import PromptExecutor

if __name__ == "__main__":
    prompt = Prompt("Explain decorators in python", "education")
    rule = category_filter("education")

    if rule(prompt):
        executor = PromptExecutor()
        print(executor.execute(prompt))
    else:
        print("Prompt not allowed")
