#!/usr/bin/python3
def add(a, b):
    # Perform addition using bitwise operations
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1

    return a