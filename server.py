from decryption import DESDecryption
from Encryption import DESEncryption
import socket

import re


def remove_unwanted_characters(input_string):
    # Define a regular expression pattern to match unwanted characters
    pattern = re.compile(r'[\x00-\x1F\x7F-\x9F]')

    # Use the sub method to replace matched characters with an empty string
    cleaned_string = pattern.sub('', input_string)

    return cleaned_string


def receiver():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 12345))
    server.listen()

    client, addr = server.accept()

    print(f"Connection from {addr} established")
    print("#massage received#")

    msg = client.recv(1024)
    encrypt = msg.decode("utf-8")
    print("Encrypted Ciphertext is : %r " % encrypt)

    key = input("Enter the key (ony 8 bytes):")
    while len(key) != 8:
        key = input("Enter the key (ony 8 bytes)")

    isExtensionRequired = (len(encrypt) % 8 != 0)

    result_of_decryption = DESDecryption(
        key=key, text=encrypt, extension=isExtensionRequired)

    print("Decrypted text is : ",
          remove_unwanted_characters(result_of_decryption))
    # print("Plain_text: ", result_of_decryption)

    client.close()
    server.close()


def sender():
    ip = input("enter ip address of the receiver: ")

    # get the key and plain_text from user and encrypt it
    input_text = input('Enter text:')
    key = input("Enter a key (ony 8 bytes):")
    while len(key) != 8:
        key = input("Enter a key (ony 8 bytes)")
    isExtensionRequired = (len(input_text) % 8 != 0)
    result_of_encryption = DESEncryption(
        text=input_text, key=key, extension=isExtensionRequired)

    print("Encrypted Ciphertext is : %r " % result_of_encryption)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, 12345))

    client.send(bytes(result_of_encryption, "utf-8"))
    client.close()
