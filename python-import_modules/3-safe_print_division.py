def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None
    finally:
        print("Inside result: {}".format(result))

    return result

# Test cases
print(safe_print_division(10, 2))
print(safe_print_division(5, 0))
print(safe_print_division(8, 3))
