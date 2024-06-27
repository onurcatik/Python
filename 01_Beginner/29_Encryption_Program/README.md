# Encryption Program in Python

## Imports and Character Set

We start by importing necessary modules and defining the character set for encryption. The `random` module will be used to shuffle the key, and the `string` module provides constants for various character sets.

```python
import random
import string

# Define the character set for the encryption
chars = string.ascii_letters + string.digits + string.punctuation + " "
chars_list = list(chars)

print(f"Character Set: {chars_list}")
```

## Creating and Shuffling the Key

Next, we create a copy of the character list to serve as our key. This key will be shuffled to ensure randomness in our encryption.

```python
# Create a key by copying the character list and shuffling it
key = chars_list.copy()
random.shuffle(key)

print(f"Original Characters: {chars_list}")
print(f"Shuffled Key: {key}")
```

## Encryption Function

We define a function to encrypt the plaintext using the shuffled key. This function will iterate over each character in the plaintext, find its index in the original character list, and replace it with the corresponding character from the shuffled key.

```python
def encrypt(plain_text, chars_list, key):
    cipher_text = ""
    for char in plain_text:
        index = chars_list.index(char)
        cipher_text += key[index]
    return cipher_text

# Example usage
plain_text = input("Enter a message to encrypt: ")
cipher_text = encrypt(plain_text, chars_list, key)

print(f"Original Message: {plain_text}")
print(f"Encrypted Message: {cipher_text}")
```

## Decryption Function

To decrypt the message, we create a similar function that reverses the process. It finds the index of each character in the shuffled key and replaces it with the corresponding character from the original character list.

```python
def decrypt(cipher_text, chars_list, key):
    decrypted_text = ""
    for char in cipher_text:
        index = key.index(char)
        decrypted_text += chars_list[index]
    return decrypted_text

# Example usage
decrypted_text = decrypt(cipher_text, chars_list, key)

print(f"Encrypted Message: {cipher_text}")
print(f"Decrypted Message: {decrypted_text}")
```

## Complete Program

Combining all the parts, the complete program allows users to encrypt and decrypt messages using the substitution cipher.

```python
import random
import string

# Define the character set for the encryption
chars = string.ascii_letters + string.digits + string.punctuation + " "
chars_list = list(chars)

# Create a key by copying the character list and shuffling it
key = chars_list.copy()
random.shuffle(key)

def encrypt(plain_text, chars_list, key):
    cipher_text = ""
    for char in plain_text:
        index = chars_list.index(char)
        cipher_text += key[index]
    return cipher_text

def decrypt(cipher_text, chars_list, key):
    decrypted_text = ""
    for char in cipher_text:
        index = key.index(char)
        decrypted_text += chars_list[index]
    return decrypted_text

# Example usage
plain_text = input("Enter a message to encrypt: ")
cipher_text = encrypt(plain_text, chars_list, key)
decrypted_text = decrypt(cipher_text, chars_list, key)

print(f"Original Message: {plain_text}")
print(f"Encrypted Message: {cipher_text}")
print(f"Decrypted Message: {decrypted_text}")
```

