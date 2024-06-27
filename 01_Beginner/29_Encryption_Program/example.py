import random
import string 


chars = string.ascii_letters + string.digits + string.punctuation + " "
chars_list = list(chars)


key = chars_list.copy()
random.shuffle(key)

print("Original Characters:", chars_list)
print("=" * 100)
print("Shuffled Key:", key)


def encrypt(plain_text, char_list, key):
    cipher_text = ""
    for char in plain_text:
        if char in char_list:
            index = char_list.index(char)
            cipher_text += key[index]
        else:
            
            cipher_text += char
    return cipher_text


plain_text = input("Enter a message: ")


cipher_text = encrypt(plain_text, chars_list, key)


print(f"Original Message: {plain_text}")
print(f"Encrypted Message: {cipher_text}")
