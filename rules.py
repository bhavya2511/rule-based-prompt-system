def category_filter(allowed):
    def check(prompt):
        return prompt.category == allowed
    return check
