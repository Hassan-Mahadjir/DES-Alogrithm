from Encryption import DESEncryption

plain_text = "helloooow"
key = "hassannn"
print(len(key))
isExtensionRequired = (len(plain_text) % 8 != 0)

result_of_encryption = DESEncryption(
    text=plain_text, key=key, extension=isExtensionRequired)

print(result_of_encryption)
