from Encryption import DESEncryption

plain_text = "hello123hello123"
key = "abcdefgh"

isExtensionRequired = (len(plain_text) % 8 != 0)

result_of_encryption = DESEncryption(
    text=plain_text, key=key, extension=isExtensionRequired)

print(result_of_encryption)
