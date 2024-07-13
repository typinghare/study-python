from typing import List
from gcd import modular_inverse_gcd

# The inverse function finds the inverse of a number by extended Euclidean algorithm
inverse = modular_inverse_gcd

# Define a list containing all uppercase and lowercase letters
letters: List[str] = \
    [chr(letter) for letter in range(ord('A'), ord('Z') + 1)] + \
    [chr(letter) for letter in range(ord('a'), ord('z') + 1)]


def letter_to_index(letter: str) -> int:
    """
    Convert a letter (either uppercase or lowercase) to a zero-based index.

    :param letter: The letter to convert.
    :return: Zero-based index corresponding to the letter.
    :raise: ValueError if the letter is not uppercase or lowercase.
    """
    if 'A' <= letter <= 'Z':
        return ord(letter) - ord('A')
    elif 'a' <= letter <= 'z':
        return ord(letter) - ord('a') + 26
    else:
        raise ValueError(f'Invalid letter: {letter}')


def index_to_letter(index: int) -> str:
    """
    Convert a zero-based index to the corresponding letter.

    :param index: The zero-based index to convert.
    :return: The corresponding letter.
    """
    return letters[index]


def encrypt(num: int, k: int, b: int, m: int) -> int:
    """
    Encrypts a number using the affine cipher technique. he affine cipher encryption function is
    defined as:

        f(x) = (kx + b) mod m

    Where:
    - x is the number to encrypt,
    - k is the coefficient,
    - b is the bias,
    - m is the modulus.

    The modulus m must be greater than zero.

    :param num: The number to encrypt.
    :param k: The coefficient to use.
    :param b: The bias to use.
    :param m: The modulus to use. The modulus must be greater than zero.
    :return: The encrypted number.
    """
    return (k * num + b) % m


def decrypt(num: int, k: int, b: int, m: int) -> int:
    """
    Decrypts a number encrypted using the affine cipher technique. The affine cipher decryption
    function is the reverse process of encryption:

    f^{-1}(x) = [k^{-1}(x - b)] mod m

    Where:
    - x is the number to decrypt,
    - k is the coefficient,
    - b is the bias,
    - m is the modulus.

    :param num: The number to decrypt.
    :param k: The coefficient to use.
    :param b: The bias to use.
    :param m: The modulus to use. The modulus must be greater than zero.
    :return: The decrypted number.
    """
    k_inverse: int = inverse(k, m)

    return (k_inverse * (num - b)) % m


def encrypt_caesar_cipher(string: str, k: int, b: int) -> str:
    """
    Encrypts a string using the Caesar cipher technique with an affine transformation.
    Each letter in the string is first converted to its corresponding index,
    then encrypted using the affine cipher formula:

        f(x) = (kx + b) mod m

    where x is the letter's index, k is the coefficient, b is the bias, and m is the modulus
    (the total number of letters in the alphabet). The encrypted letters are converted back
    to their corresponding characters to form the encrypted string.

    :param string: The string to encrypt.
    :param k: The coefficient for the affine cipher.
    :param b: The bias for the affine cipher.
    :return: The encrypted string.
    """
    modulus: int = len(letters)
    index_list: List[int] = [letter_to_index(letter) for letter in string]
    encrypted_index_list: List[int] = [encrypt(index, k, b, modulus) for index in index_list]

    return ''.join([index_to_letter(index) for index in encrypted_index_list])


def decrypt_caesar_cipher(string: str, k: int, b: int) -> str:
    """
    Decrypts a string encrypted using the Caesar cipher technique with an affine transformation.
    Each letter in the string is first converted to its corresponding index,
    then decrypted using the inverse affine cipher formula:

        f^{-1}(x) = [k^{-1}(x - b)] mod m

    where x is the encrypted letter's index, k is the coefficient, b is the bias,
    and m is the modulus (the total number of letters in the alphabet).
    The decrypted indices are converted back to their corresponding characters
    to form the decrypted string.

    :param string: The string to decrypt.
    :param k: The coefficient used in the encryption process.
    :param b: The bias used in the encryption process.
    :return: The decrypted string.
    """
    modulus: int = len(letters)
    index_list: List[int] = [letter_to_index(letter) for letter in string]
    decrypted_index_list: List[int] = [decrypt(index, k, b, modulus) for index in index_list]

    return ''.join([index_to_letter(index) for index in decrypted_index_list])

# def concatenate_integers(int_list: List[int]) -> int:
#     """
#     Combines a list of integers into a single concatenated string representation.
#
#     :param int_list: The list of integers to combine.
#     :return: The concatenated string representation of the integers.
#     """
#     return int(''.join(map(str, int_list)))
#
#
# def divide_into_two_letter_strings(string: str) -> List[str]:
#     res: List[str] = []
#     i: int = len(string)
#     while i > 1:
#         res.append(string[i - 2:i])
#         i -= 2
#
#     if i == 1:
#         res.append(string[0])
#
#     res.reverse()
#     return res


# def encrypt_block_cipher(string: str, k: int, b: int, width: int) -> str:
#     modulus: int = concatenate_integers([len(letters)] * width)
#     index_list: List[int] = [letter_to_index(letter) for letter in string]
#
#     block_list: List[int] = []
#     for i in range(0, len(index_list), width):
#         window: List[int] = index_list[i:i + width]
#         block_list.append(concatenate_integers(window))
#
#     encrypted_block_list: List[int] = [encrypt(block, k, b, modulus) for block in block_list]
#     encrypted_index_list: List[int] = []
#     for block in encrypted_block_list:
#         block_str: str = str(block)
#         strings: List[str] = divide_into_two_letter_strings(block_str)
#         for string in strings:
#             encrypted_index_list.append(int(string))
#
#     return ''.join([index_to_letter(index) for index in encrypted_index_list])
#
#
# def decrypt_block_cipher(string: str, k: int, b: int) -> str:
#     return ""
