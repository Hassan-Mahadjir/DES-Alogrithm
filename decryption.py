# from bitarray import bitarray
# # Convert bits to the orginal text
# bit_stream = ""
# bits = bitarray(bit_stream)
# orignal_text = bits.tobytes().decode('ascii')
# print("The normal string is: ", orignal_text)

from Encryption import DES


def removeExtenstion(data):
    paddingLength = ord(data[-1])

    return data[: -paddingLength]


def DESDecryption(key, text, extension):
    plaint_text = DES(text, key, False)

    if extension == True:
        return removeExtenstion(plaint_text)

    return plaint_text
