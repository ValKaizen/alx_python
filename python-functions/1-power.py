def pow(a, b):
    result = 1

    # If the exponent is negative, invert base and exponent
    if b < 0:
        a = 1 / a
        b = -b

    while b > 0:
        # If the exponent is odd, multiply result with base
        if b % 2 == 1:
            result *= a

        a *= a
        b //= 2

    return result