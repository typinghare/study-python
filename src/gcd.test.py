from gcd import modular_inverse, gcd, gcd_extended, modular_inverse_gcd

# Test inverse_brute_force
print(modular_inverse(3, 11))  # Expected output: 4 (since 3 * 4 % 11 == 1)
print(modular_inverse(10, 17))  # Expected output: 12 (since 10 * 12 % 17 == 1)
print(modular_inverse(3, 6))  # Expected output: None (since 3 has no inverse mod 6)
print(modular_inverse(0, 5))  # Expected output: None (0 has no modular inverse)
print(modular_inverse(3, -11))  # Expected output: None (modulus should be positive)

# test gcd
print(gcd(48, 18))  # Expected output: 6
print(gcd(0, 5))  # Expected output: 5
print(gcd(7, 7))  # Expected output: 7
print(gcd(10, 5))  # Expected output: 5
print(gcd(-48, -18))  # Expected output: 6

# Test gcd_extended
print(gcd_extended(30, 20))  # Expected output: (10, 1, -1)
print(gcd_extended(35, 64))  # Expected output: (1, 11, -6)

# Test inverse_gcd
print(modular_inverse_gcd(3, 11))  # Expected output: 4 (since 3 * 4 % 11 == 1)
print(modular_inverse_gcd(10, 17))  # Expected output: 12 (since 10 * 12 % 17 == 1)
print(modular_inverse_gcd(3, 6))  # Expected output: None (since 3 has no inverse mod 6)
print(modular_inverse_gcd(0, 5))  # Expected output: None (0 has no modular inverse)
print(modular_inverse_gcd(3, -11))  # Expected output: None (mod should be positive)
