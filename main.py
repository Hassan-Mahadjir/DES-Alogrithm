from Encryption import DESEncryption
from decryption import DESDecryption

text = input('Enter text: ')
key = input("Enter a key (ony 8 bytes): ")
condition = input("select Encryption(e) or Decryption(d): ")
while len(key) != 8:
    key = input("Enter a key (ony 8 bytes)")
isExtensionRequired = (len(text) % 8 != 0)

if condition == 'e':
    result_of_encryption = DESEncryption(
        text=text, key=key, extension=isExtensionRequired)
    print(result_of_encryption)

elif condition == 'd':
    result_of_decryption = DESDecryption(
        key=key, text=text, extension=isExtensionRequired)
    print(result_of_decryption)
