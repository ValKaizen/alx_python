import sys

def print_arguments():
    num_args = len(sys.argv) - 1

    import sys

def print_arguments():
    num_args = len(sys.argv) - 1
    # Print the number of arguments and the appropriate plural/singular form
    print("Number of argument{}: {}".format("s" if num_args != 1 else "", num_args))

    if num_args == 0:
        # If no arguments were passed, print a dot and a new line
        print(".")
    else:
        # For each argument, print its position, value, and a new line
        for i, arg in enumerate(sys.argv[1:], 1):
            print("{}: {}".format(i, arg))

    # Restore the original sys.argv
    sys.argv = original_args

if __name__ == "__main__":
    print_arguments()
