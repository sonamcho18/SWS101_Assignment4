def vigenere_encrypt(text, key):
    result = []
    key = key.upper()
    key_length = len(key)
    
    for i, char in enumerate(text.upper()):
        if char.isalpha():
            # Calculate shift amount
            shift = ord(key[i % key_length]) - 65
            # Shift the character
            new_char = chr((ord(char) - 65 + shift) % 26 + 65)
            result.append(new_char)
    return ''.join(result)

def vigenere_decrypt(text, key):
    result = []
    key = key.upper()
    key_length = len(key)
    
    for i, char in enumerate(text.upper()):
        if char.isalpha():
            # Calculate shift amount (negative for decryption)
            shift = ord(key[i % key_length]) - 65
            # Shift the character back
            new_char = chr((ord(char) - 65 - shift) % 26 + 65)
            result.append(new_char)
    return ''.join(result)

# Example usage
plaintext = "HELLO"
key = "KEY"

# Encrypt
ciphertext = vigenere_encrypt(plaintext, key)
print("Encrypted:", ciphertext)  # Output: "RIJVS"

# Decrypt
decrypted = vigenere_decrypt(ciphertext, key)
print("Decrypted:", decrypted)  # Output: "HELLO"