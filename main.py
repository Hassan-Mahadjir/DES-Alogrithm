from Encryption import DESEncryption
from decryption import DESDecryption

plain_text = input('Enter text: ')
key = input("Enter a key (ony 8 bytes)")
while len(key) != 8:
    key = input("Enter a key (ony 8 bytes)")
isExtensionRequired = (len(plain_text) % 8 != 0)

result_of_encryption = DESEncryption(
    text=plain_text, key=key, extension=isExtensionRequired)

print(result_of_encryption)

result_of_decryption = DESDecryption(
    key=key, text=result_of_encryption, extension=isExtensionRequired)

print(result_of_decryption)
