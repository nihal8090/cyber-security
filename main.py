def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr(start + (ord(char) - start + shift_amount) % 26)
            result.append(new_char)
        else:
            result.append(char)  # Non-alphabetic characters are unchanged
    return ''.join(result)

def caesar_encrypt(plaintext, shift):
    return caesar_cipher(plaintext, shift)

def caesar_decrypt(ciphertext, shift):
    return caesar_cipher(ciphertext, -shift)
    
    # Example usage
plaintext = "Hello, World!"
shift = 3

encrypted_text = caesar_encrypt(plaintext, shift)
print(f"Encrypted: {encrypted_text}")

decrypted_text = caesar_decrypt(encrypted_text, shift)
print(f"Decrypted: {decrypted_text}")
