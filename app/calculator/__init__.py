from app.calculation import CalculationFactory


def calculator():
    print("Welcome to the Professional Calculator!")
    print("Supported operations: +, -, *, /")
    print("Special commands: help, history, exit")
    print()

    history = []

    while True:
        user_input = input("Enter calculation (e.g. 2 + 3): ").strip()

        # --- Special commands (EAFP-friendly: just check the string directly) ---
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        if user_input.lower() == "help":
            print("Supported operations: +, -, *, /")
            print("Format: number operator number (e.g. 2 + 3)")
            print("Special commands: help, history, exit")
            print()
            continue

        if user_input.lower() == "history":
            if not history:
                print("No calculations yet.\n")
            else:
                print("Calculation history:")
                for entry in history:
                    print(f"  {entry}")
                print()
            continue

        # --- LBYL: check the format BEFORE trying to use it ---
        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid format. Use: number operator number (e.g. 2 + 3)\n")
            continue

        num1_str, operator, num2_str = parts

        # --- EAFP: try the conversion, handle the exception if it fails ---
        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            print(f"Invalid numbers: '{num1_str}' or '{num2_str}' is not a valid number.\n")
            continue

        # --- EAFP: try creating and running the calculation, handle errors ---
        try:
            calculation = CalculationFactory.create_calculation(operator, num1, num2)
            result = calculation.execute()
        except ValueError as e:
            print(f"Error: {e}\n")
            continue

        print(f"Result: {result}\n")
        history.append(str(calculation))