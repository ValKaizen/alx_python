def raise_exception_msg(message=""):
    if len(message) < 9:
        raise NameError(message[:9])
    elif len(message) < 15:
        raise NameError(message[:15])
    else:
        raise NameError(message[0])
    # Test cases
try:
    raise_exception_msg("ShortMsg")
except NameError as e:
    print(str(e))

try:
    raise_exception_msg("MediumMessage")
except NameError as e:
    print(str(e))

try:
    raise_exception_msg("TooLongMessage")
except NameError as e:
    print(str(e))
