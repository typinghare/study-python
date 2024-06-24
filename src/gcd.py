from typing import Optional


def inverse_brute_force(num: int, modulus: int) -> Optional[int]:
    """
    Find the modular inverse of a given number using brute force. This function iterates through
    all possible values from 0 to mod-1 to find the modular inverse.

    Parameters:
    num (int): The number to find the inverse of.
    modulus (int): The modulus.

    Returns:
    Optional[int]: The modular inverse if it exists, otherwise None.
    """
    if modulus <= 0:
        return None

    for i in range(modulus):
        if ((num % modulus) * (i % modulus)) % modulus == 1:
            return i

    return None


def gcd(num1: int, num2: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers using the Euclidean Algorithm. The
    Euclidean Algorithm is an efficient method for computing the GCD of two numbers. The GCD of two
    integers is the largest integer that divides both of them without leaving a remainder. If either
    of the number is zero, the GCD is the non-zero number. If both are zero, the GCD is zero. The
    GCD must be non-negative.

    Parameters:
    num1 (int): The first integer.
    num2 (int): The second integer.

    Returns:
    int: The greatest common divisor of the two given integers.
    """
    num1 = abs(num1)
    num2 = abs(num2)

    if num1 == 0:
        return num2
    if num2 == 0:
        return num1

    return gcd(num2, num1 % num2)


def inverse_gcd(num: int, modulus: int) -> int:
    return gcd(num, modulus)


# Test inverse_brute_force
print(inverse_brute_force(3, 11))  # Expected output: 4 (since 3 * 4 % 11 == 1)
print(inverse_brute_force(10, 17))  # Expected output: 12 (since 10 * 12 % 17 == 1)
print(inverse_brute_force(3, 6))  # Expected output: None (since 3 has no inverse mod 6)
print(inverse_brute_force(0, 5))  # Expected output: None (0 has no modular inverse)
print(inverse_brute_force(3, -11))  # Expected output: None (modulus should be positive)

# test gcd
print(gcd(48, 18))  # Expected output: 6
print(gcd(0, 5))  # Expected output: 5
print(gcd(7, 7))  # Expected output: 7
print(gcd(10, 5))  # Expected output: 5
print(gcd(-48, -18))  # Expected output: 6

# Test inverse_gcd
print(inverse_gcd(3, 11))  # Expected output: 4 (since 3 * 4 % 11 == 1)
print(inverse_gcd(10, 17))  # Expected output: 12 (since 10 * 12 % 17 == 1)
print(inverse_gcd(3, 6))  # Expected output: None (since 3 has no inverse mod 6)
print(inverse_gcd(0, 5))  # Expected output: None (0 has no modular inverse)
print(inverse_gcd(3, -11))  # Expected output: None (mod should be positive)
