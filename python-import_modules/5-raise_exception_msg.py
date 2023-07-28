def raise_exception_msg(message=""):
    if not isinstance(message, str):
        raise TypeError("Message must be a string.")
    raise NameError(message)

# Example usage:
try:
    raise_exception_msg("This is a name exception with a custom message.")
except NameError as e:
    print("Caught exception:", e)
