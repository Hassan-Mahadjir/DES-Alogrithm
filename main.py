from Encryption import DESEncryption
from decryption import DESDecryption

plain_text = "abcdefgh"
key = "12345678"

isExtensionRequired = (len(plain_text) % 8 != 0)

result_of_encryption = DESEncryption(
    text=plain_text, key=key, extension=isExtensionRequired)

print(result_of_encryption)

result_of_decryption = DESDecryption(
    key=key, text=result_of_encryption, extension=isExtensionRequired)

print(result_of_decryption)
