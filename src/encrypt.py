from typing import List, Optional
from gcd import modular_inverse_gcd

# The inverse function finds the inverse of a number by extended Euclidean algorithm
inverse = modular_inverse_gcd

# Define a list containing all uppercase and lowercase letters
letters: List[str] = [chr(letter) for letter in range(ord('A'), ord('Z') + 1)] + \
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
    - m is the modulus, which must be greater than zero.

    :param num: The number to encrypt.
    :param k: The coefficient to use.
    :param b: The bias to use.
    :param m: The modulus to use.
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
    - m is the modulus, which must be greater than zero.

    :param num: The number to decrypt.
    :param k: The coefficient to use.
    :param b: The bias to use.
    :param m: The modulus to use. The modulus must be greater than zero.
    :return: The decrypted number.
    """
    k_inverse: Optional[int] = inverse(k, m)
    if k_inverse is None:
        raise ValueError(f'The inverse of k does not exist: {k}')

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


def concatenate_integers(int_list: List[int]) -> str:
    """
    Concatenates a list of integers into a single string.
    If an integer is a single digit, it is zero-padded to become a two-digit number string.

    :param int_list: A list of integers to concatenate.
    :return The concatenated result as a string.
    """
    two_digit_list = [f"{n:02d}" for n in int_list]

    return ''.join(two_digit_list)


def encrypt_block_cipher(text: str, k: int, b: int, width: int) -> int:
    """
    Encrypts a text using block cipher technique with affine transformation.

    :param text: The text to encrypt.
    :param k: The coefficient for the affine cipher.
    :param b: The bias for the affine cipher.
    :param width: The width of each block in the text.
    :return: The encrypted text as a large integer.
    """
    modulus: int = int(concatenate_integers([len(letters)] * width))
    block_width: int = width * 2
    index_list: List[int] = [letter_to_index(letter) for letter in text]

    block_list: List[int] = []
    right: int = len(index_list)
    while right > 0:
        left: int = max(0, right - width)
        window: List[int] = index_list[left:right]
        block_list.append(int(concatenate_integers(window)))
        right -= width
    block_list.reverse()

    encrypted_block_list: List[int] = [encrypt(block, k, b, modulus) for block in block_list]
    encrypted_block_str_list: List[str] = []
    for block in encrypted_block_list:
        block_str: str = str(block)
        encrypted_block_str_list.append('0' * (block_width - len(block_str)) + block_str)

    return int(''.join(encrypted_block_str_list))


def decrypt_block_cipher(large_int: int, k: int, b: int, width: int, original_text_length: int) \
        -> str:
    """
    Decrypts a large integer encrypted using block cipher technique with affine transformation.

    :param large_int: The encrypted large integer.
    :param k: The coefficient used in the encryption process.
    :param b: The bias used in the encryption process.
    :param width: The width of each block in the original text.
    :param original_text_length: The length of the original text.
    :return: The decrypted text.
    """
    modulus: int = int(concatenate_integers([len(letters)] * width))
    block_width: int = 2 * width
    large_int_str: str = str(large_int)
    padding_len: int = block_width - len(large_int_str) % block_width
    large_int_str = '0' * padding_len + large_int_str

    block_str_list: List[str] = []
    for i in range(0, len(large_int_str), block_width):
        block_str_list.append(large_int_str[i:i + block_width])
    block_list: List[int] = [decrypt(int(block), k, b, modulus) for block in block_str_list]

    index_list: List[int] = []
    for block in block_list:
        block_str: str = str(block)
        block_str = '0' * (block_width - len(block_str)) + block_str
        for i in range(0, len(block_str), 2):
            index_list.append(int(block_str[i:i + 2]))

    char_list: List[str] = [index_to_letter(index) for index in index_list]

    return ''.join(char_list[len(char_list) - original_text_length:])


def stringify(large_int: int) -> str:
    """
    Converts a large integer to a string representation using a base determined by the length of letters.

    :param large_int: The large integer to convert.
    :return: The string representation of the large integer.
    """
    base = len(letters)
    result = ''
    while large_int > 0:
        result += index_to_letter(large_int % base)
        large_int = large_int // base

    return result
