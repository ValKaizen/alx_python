def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    else:
        print("Inside result: {}".format(result))
        return result
    finally:
        print("Finally: Division operation completed.")

# Test cases
print(safe_print_division(10, 2))
print(safe_print_division(5, 0))
