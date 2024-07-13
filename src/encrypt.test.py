from encrypt import encrypt_caesar_cipher, decrypt_caesar_cipher

text: str = "IAmEatingSupperAndLearningDiscreteStructure"
encrypted_message: str = encrypt_caesar_cipher(text, 17, 36)
print("Encrypted text: " + encrypted_message)
decrypted_message: str = decrypt_caesar_cipher(encrypted_message, 17, 36)
print("Original text: " + decrypted_message)
