from typing import Optional, Tuple


def modular_inverse(num: int, modulus: int) -> Optional[int]:
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


def gcd_extended(num: int, modulus: int) -> Tuple[int, int, int]:
    """
    Extended Euclidean Algorithm to find the greatest common divisor of two numbers.
    Additionally, it finds integers x and y such that: gcd(num, modulus) = num * x + modulus * y

    Parameters:
    num (int): The first integer.
    modulus (int): The second integer.

    Returns:
    Tuple[int, int, int]: A tuple containing the gcd and the coefficients x and y.
    """

    def inner(_num: int, _modulus: int) -> int:
        nonlocal x, y
        if _num == 0:
            x, y = 0, 1
            return _modulus

        _gcd = inner(_modulus % _num, _num)
        x_tmp, y_tmp = x, y
        x = y_tmp - (_modulus // _num) * x_tmp
        y = x_tmp

        return _gcd

    x, y = 1, 0
    __gcd = inner(num, modulus)
    return __gcd, x, y


def modular_inverse_gcd(num: int, modulus: int) -> Optional[int]:
    """
    Find the modular inverse of a given number using the Extended Euclidean Algorithm.

    The modular inverse of a number `num` modulo `modulus` is a number `x` such that:
    (num * x) % modulus == 1. This function uses the Extended Euclidean Algorithm to find such
    an `x`, if it exists.

    Parameters:
    num (int): The number to find the modular inverse of.
    modulus (int): The modulus.

    Returns:
    Optional[int]: The modular inverse if it exists, otherwise None.
    """
    if modulus <= 0:
        return None

    _gcd, a, b = gcd_extended(num, modulus)
    if _gcd != 1:
        return None

    return (a % modulus + modulus) % modulus
