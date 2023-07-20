#!/usr/bin/python3
ef add(a, b):
    # Perform addition using bitwise operations
    while b != 0:
        carry = a & b
        a = (a ^ b) & 0xFFFFFFFF  # To handle negative numbers in 32-bit integers
        b = carry << 1