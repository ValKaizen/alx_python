import sys

def print_arguments():
    num_args = len(sys.argv) - 1

    # Print the number of arguments and the appropriate plural/singular form
    print("{} argument: {}".format("s" if num_args != 1 else "", num_args))

    if num_args == 0:
        print(".")
    else:
        # For each argument, print its position, value, and a new line
        for i, arg in enumerate(sys.argv[1:], 1):
            print("{}: {}".format(i,arg))

if __name__ == "__main__":
    print_arguments()

