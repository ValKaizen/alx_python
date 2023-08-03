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
        #if isinstance(a, int) and isinstance(b, int):
         #   print("{} / {} = {}".format(a, b, result))
        #else:
            #print("Invalid inputs: {} / {} cannot be calculated.".format(a, b))