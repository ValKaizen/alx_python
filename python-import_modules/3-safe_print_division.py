def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Both inputs must be integers.")
        return None
    else:
        print("Inside result: {}".format(result))
        return result
    finally:
        print("Function execution completed.")

# Test cases
print(safe_print_division(10, 2))
print(safe_print_division(10, -2))
print(safe_print_division(0, 2))
print(safe_print_division(10, 0))
print(safe_print_division(0, 0))

