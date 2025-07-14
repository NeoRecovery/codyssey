def calculate_power(base: float, exp: int) -> float:
    """
    base 를 exp 만큼 거듭제곱
    exp 가 음수일 경우에도 처리.
    """

    if exp == 0:
        return 1.0

    negative = exp < 0
    exp = -exp if negative else exp

    result = 1.0
    for _ in range(exp):
        result *= base

    if negative:
        return 1.0 / result
    else:
        return result


def main():
    while True:
        base_input = input("Enter number: ")
        try:
            base = float(base_input)
            break
        except ValueError:
            print("Invalid number input.")

    while True:    
        exp_input = input("Enter exponent: ")
        try:
            exp = int(exp_input)
            break
        except ValueError:
            print("Invalid exponent input.")
        
    result = calculate_power(base, exp)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()