from decorators import validate_prompt, log_prompt, timer

class PromptExecutor:

    @timer
    @log_prompt
    @validate_prompt
    def execute(self, prompt):
        return f"AI Response: {prompt.text.upper()}"
