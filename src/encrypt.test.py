from encrypt import encrypt_caesar_cipher, decrypt_caesar_cipher, encrypt_block_cipher, \
    decrypt_block_cipher, stringify

text: str = "IAmEatingSupperAndLearningDiscreteStructure"
encrypted_message: str = encrypt_caesar_cipher(text, 17, 36)
print("Encrypted text: ", encrypted_message)
decrypted_message: str = decrypt_caesar_cipher(encrypted_message, 17, 36)
print("Original text: ", decrypted_message)

print('-' * 80)

text: str = "IAmEatingSupperAndLearningDiscreteStructure"
encrypted_large_int: int = encrypt_block_cipher(text, 17, 36, 3)
print("Encrypted large int: ", encrypted_large_int)
print("Encrypted text: ", stringify(encrypted_large_int))
decrypted_message: str = decrypt_block_cipher(encrypted_large_int, 17, 36, 3, len(text))
print("Original text: ", decrypted_message)
