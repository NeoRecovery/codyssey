def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero.")
    return a / b

def calculate(a: float, op: str, b: float) -> float:
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        raise ValueError("Invalid operator")

def main():
    expr = input("Enter expression: ").strip()
    parts = expr.split()

    if len(parts) == 2:
        a_str, b_str = parts
        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError:
            print("Invalid number. Please enter valid floats.")
            return
        
        op = input("Select operator (+, -, *, /): ").strip()

        try:
            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            elif op == "/":
                result = divide(a, b)
            else:
                print("Invalid operator.")
                return
        except ZeroDivisionError:
            print("Error: Division by zero.")
            return        

    elif len(parts) == 3:
        a_str, op, b_str = parts

        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError:
            print("Invalid number. Please enter valid floats.")
            return

        try:
            result = calculate(a, op, b)
        except ZeroDivisionError:
            print("Error: Division by zero.")
            return
        except ValueError:
            print("Invalid operator. Use one of +, -, *, /.")
            return
    else:
        print("Invalid input format.")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()