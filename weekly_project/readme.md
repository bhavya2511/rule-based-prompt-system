# Prompt Engine (Python)

A lightweight, modular Python project that demonstrates how prompts can be validated, filtered, logged, and executed using clean software design principles such as decorators, rule-based checks, and separation of concerns.

This repository focuses on **code structure and execution flow**, rather than external frameworks or heavy dependencies.

---

## 📌 Features

- Rule-based prompt filtering
- Decorator-driven validation, logging, and timing
- Clear separation of models, rules, and execution logic
- Pure Python (no third-party dependencies)
- Easy to extend and experiment with

---

## 🗂️ Project Structure

├── main.py # Entry point
├── executor.py # Prompt execution logic
├── decorators.py # Validation, logging, timing decorators
├── rules.py # Rule-based prompt filters
├── models.py # Data models
├── requirements.txt # Dependencies
└── README.md

## ▶️ How It Works

1. A `Prompt` object is created with text and category.
2. A rule checks whether the prompt is allowed.
3. Decorators validate the prompt, log execution, and measure runtime.
4. The executor processes the prompt and returns a response.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher

### Run the project
```bash
python main.py