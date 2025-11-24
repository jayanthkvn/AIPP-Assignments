def is_prime(n):
    """Return True if n is a prime number, False otherwise."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors up to sqrt(n)
    limit = int(n ** 0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False

    return True


test_cases = {
    -10: False,
    0: False,
    1: False,
    2: True,
    3: True,
    4: False,
    17: True,
    18: False,
    97: True,
    100: False,
    121: False
}


def run_regression_suite() -> None:
    """Execute and report the AI-generated regression cases."""
    all_passed = True
    for n, expected in test_cases.items():
        result = is_prime(n)
        passed = result == expected
        all_passed = all_passed and passed
        print(f"is_prime({n}) = {result} -> {'PASS' if passed else 'FAIL'}")

    if all_passed:
        print("All AI-generated tests passed.")
        
def prompt_user_inputs() -> None:
    """Allow the user to check arbitrary integers."""
    try:
        user_values = input(
            "Enter integer values separated by spaces (or press Enter to skip): "
        ).strip()
    except EOFError:
        # Non-interactive environments (e.g., automated runs) can raise EOF.
        return
    if not user_values:
        return

    for token in user_values.split():
        try:
            value = int(token)
        except ValueError:
            print(f"Ignoring '{token}': not an integer.")
            continue
        verdict = "a prime" if is_prime(value) else "not a prime"
        print(f"{value} is {verdict} number.")

def is_prime(n: int) -> bool:
    """Check if the given integer n is a prime number."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Run the regression suite as requested
run_regression_suite()
for i in range(2):
    try:
        value = int(input(f"Enter integer #{i+1} to check if it is prime: "))
        verdict = "a prime" if is_prime(value) else "not a prime"
        print(f"{value} is {verdict} number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    # Prompt the user for a single integer to check for primality
    try:
        value = int(input("Enter an integer to check if it is prime: "))
        verdict = "a prime" if is_prime(value) else "not a prime"
        print(f"{value} is {verdict} number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")