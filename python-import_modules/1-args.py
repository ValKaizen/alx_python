import sys

def main():
    # Get the number of command-line arguments
    num_args = len(sys.argv) - 1

    # Print the number of arguments and the list of arguments
    print("Number of argument{}: {}".format("s" if num_args != 1 else "", num_args))

    if num_args == 0:
        print(".")
    else:
        for i, arg in enumerate(sys.argv[1:], 1):
            print("{}: {}".format(i, arg))

if __name__ == "__main__":
    main()
