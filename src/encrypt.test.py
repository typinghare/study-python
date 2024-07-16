from encrypt import encrypt_caesar_cipher, decrypt_caesar_cipher, encrypt_block_cipher, \
    decrypt_block_cipher, stringify

text: str = "IAmEatingSupperAndLearningDiscreteStructure"
encrypted_message: str = encrypt_caesar_cipher(text, 17, 36)
print("Encrypted text: ", encrypted_message)
decrypted_message: str = decrypt_caesar_cipher(encrypted_message, 17, 36)
print("Original text: ", decrypted_message)

print('-' * 80)

# Note: we have to ensure that k has an inverse mod 525252, and 74695 has been verified valid
k: int = 74695
b: int = 11923
block_width: int = 3
text: str = "IAmEatingSupperAndLearningDiscreteStructure"
encrypted_large_int: int = encrypt_block_cipher(text, k, b, block_width)
print("Encrypted large int: ", encrypted_large_int)
print("Encrypted text: ", stringify(encrypted_large_int))
decrypted_message: str = decrypt_block_cipher(encrypted_large_int, k, b, block_width, len(text))
print("Original text: ", decrypted_message)
