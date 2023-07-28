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
        print("Division operation has been completed.")

# Example usage:
result = safe_print_division(10, 2)
