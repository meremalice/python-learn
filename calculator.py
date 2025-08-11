import math

def add(x, y):
    # your code
    return x + y

def subtract(x, y):
    # your code
    return x - y

def multiply(x, y):
    # your code
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def money(x): 
    return f"${x:,.2f}"

def apply_rounding(value, mode):
    if mode == "1":   # nearest
        return round(value, 2)
    if mode == "2":   # floor
        return math.floor(value * 100) / 100
    if mode == "3":   # ceil
        return math.ceil(value * 100) / 100
    return value

def get_int(prompt):
    while True:
        s = input(prompt)
        try: 
            return int(s)
        except ValueError: 
            print("Enter a whole number.")

def get_positive_float(prompt):
    while True:
        s = input(prompt)
        try:
            v = float(s)
            if v <= 0: 
                print("Enter a positive number.")
                continue
            return v
        except ValueError:
            print("Enter a valid number.")

def get_number(prompt, last_result):
    while True:
        s = input(prompt).strip()
        if s.lower() == "ans":
            if last_result is None:
                print("No previous result yet. Enter a number instead.")
                continue
            return last_result
        try:
            return float(s)
        except ValueError:
            print("Error: Enter a valid number or 'ans'.")

def main():
    menu = {
        "1": ("Add", "+", add),
        "2": ("Subtract", "-", subtract),
        "3": ("Multiply", "*", multiply),
        "4": ("Divide", "/", divide),
        "5": ("Quit", "", None),
    }

    history = []
    last_result = None

    print("=== Welcome to My Calculator ===")
    print("Tip: Type 'ans' at any number prompt to reuse the last result.")
    
    print("Rounding: 1) nearest(.2f)  2) floor  3) ceil")
    round_mode = input("Choose rounding mode (1-3, default 1): ").strip() or "1"
    
    while True:
        print("\nChoose an operation:")
        for k, (name, _, _) in menu.items():
            label = f"{k}. {name}" if k != "5" else f"{k}. Quit"
            print(label)
        print("h. History   c. Clear history")

        choice = input("Enter choice (1-5, h, c): ").strip().lower()

        if choice == "5":
            print("Thanks for using my calculator!")
            break
        if choice == "h":
            if not history:
                print("History is empty.")
            else:
                print("\n— History —")
                for i, line in enumerate(history, 1):
                    print(f"{i}. {line}")
            continue
        if choice == "c":
            history.clear()
            last_result = None
            print("History cleared.")
            continue
        if choice not in menu:
            print("Invalid choice. Pick 1–5, h, or c.")
            continue

        _, symbol, func = menu[choice]
        x = get_number("Enter first number (or 'ans'): ", last_result)
        y = get_number("Enter second number (or 'ans'): ", last_result)

        try:
            result = func(x, y)
            result = apply_rounding(result, round_mode)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            continue

        line = f"{money(x)} {symbol} {money(y)} = {money(result)}"
        print("\n" + line)
        history.append(line)
        last_result = result

if __name__ == "__main__":
    main()
