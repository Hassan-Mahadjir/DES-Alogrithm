import socket
from Encryption import DESEncryption
from decryption import DESDecryption

input_text = input('Enter text:')
key = input("Enter a key (ony 8 bytes):")
condition = input("select Encryption(e) or Decryption(d): ")

while len(key) != 8:
    key = input("Enter a key (ony 8 bytes)")

isExtensionRequired = (len(input_text) % 8 != 0)


if condition == 'e':
    result_of_encryption = DESEncryption(
        text=input_text, key=key, extension=isExtensionRequired)

    print("Encrypted Ciphertext is : %r " % result_of_encryption)
    result_of_encryption = "%r " % result_of_encryption
    print(result_of_encryption)

elif condition == 'd':
    result_of_decryption = DESDecryption(
        key=key, text=input_text, extension=isExtensionRequired)

    print(result_of_decryption)

# from Encryption import DESEncryption
# from decryption import DESDecryption


# condition = input("select Encryption(e) or Decryption(d):")
# key = input("Enter a key (ony 8 bytes):")
# while len(key) != 8:
#     key = input("Enter a key (ony 8 bytes)")


# if condition == 'e':
#     text = input('Enter text: ')
#     isExtensionRequired = (len(text) % 8 != 0)
#     f = open("demofile2.txt", "w")
#     result_of_encryption = DESEncryption(
#         text=text, key=key, extension=isExtensionRequired)
#     f.write(result_of_encryption)
#     print(result_of_encryption)
#     f.close()

# elif condition == 'd':
#     read = open("demofile2.txt", "r")
#     read1 = read.read()
#     result_of_decryption = DESDecryption(
#         key=key, text=read1, extension=False)
#     print(result_of_decryption)
#     read.close()
