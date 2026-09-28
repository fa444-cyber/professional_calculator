# Professional Calculator

A command-line calculator application built in Python using advanced Object-Oriented Programming principles - including an abstract base class, the Factory design pattern, and both LBYL and EAFP error-handling strategies - with 100% test coverage enforced via GitHub Actions.

## Features

- Interactive REPL (Read-Eval-Print Loop) interface
- Supports addition, subtraction, multiplication, and division
- Calculation history tracked during the session
- Special commands: help, history, exit
- Robust input validation and error handling (LBYL and EAFP demonstrated)
- 100% test coverage enforced automatically via GitHub Actions

## Project Structure

professional_calculator/
- app/
  - calculator/__init__.py (REPL loop, history, special commands)
  - calculation/__init__.py (Calculation abstract base class, subclasses, CalculationFactory)
  - operation/__init__.py (Operation class with arithmetic logic)
- tests/
  - test_calculator.py
  - test_calculations.py
  - test_operations.py
- main.py
- pytest.ini
- requirements.txt
- .github/workflows/python-app.yml

## Design Overview

- Operation: static methods for basic arithmetic (add, subtract, multiply, divide).
- Calculation: an abstract base class defining the interface every calculation must implement (execute()). Concrete subclasses (AddCalculation, SubtractCalculation, MultiplyCalculation, DivideCalculation) each implement their own version.
- CalculationFactory: implements the Factory design pattern, creating the correct Calculation subclass instance based on the requested operator.
- Error handling: the REPL demonstrates both LBYL (checking input format before using it) and EAFP (attempting conversion/execution inside try/except blocks).

## Setup Instructions

1. Clone the repository:
   git clone git@github.com:fa444-cyber/professional_calculator.git
   cd professional_calculator

2. Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\Activate.ps1

3. Install dependencies:
   pip install -r requirements.txt

## Usage

Run the calculator:
   python main.py

## Running Tests

Run all tests with coverage:
   pytest

This project requires 100% test coverage. If coverage drops below 100%, the test run and CI pipeline will fail.

## Continuous Integration

This project uses GitHub Actions to automatically run all tests and enforce 100% coverage on every push and pull request to main. See .github/workflows/python-app.yml for details.
