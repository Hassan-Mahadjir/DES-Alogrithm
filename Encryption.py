from convert import converToBinary, converToString
from permutation import permutation, initialPermutationMatrix, eachRoundPermutationMatrix, finalPermutationMatrix
from divide_to_bytes import nSplit
from keys import generateKeys
from Sbox import Sbox_substitution


def addExtension(text):
    """Function to add padding according to PKCS5 standard."""

    # Determining padding length
    paddingLength = 8 - (len(text) % 8)
    # Adding paddingLength number of chr(paddingLength) to text
    text += chr(paddingLength) * paddingLength

    # Returning text
    return text


def DES(text, key, isEncrypt):
    isDecrypt = not isEncrypt

    #  need to generateKeys
    keys = generateKeys(key)

    plain_text_to_8byte_blocks = nSplit(text, 8)

    result = []

    for block in plain_text_to_8byte_blocks:

        block = converToBinary(block)
        block = permutation(block, initialPermutationMatrix)
        left_block, right_block = nSplit(block, 32)

        temp = None

        for i in range(16):
            expanded_right_block = expand(right_block, expandMatrix)

            if isEncrypt == True:
                temp = XOR(keys[i], expanded_right_block)

            elif isDecrypt == True:

                temp = XOR(keys[15 - i], expanded_right_block)

            temp = Sbox_substitution(temp)

            temp = permutation(temp, eachRoundPermutationMatrix)

            temp = XOR(left_block, temp)

            left_block = right_block
            right_block = temp

        result += permutation(right_block + left_block, finalPermutationMatrix)

    finalResult = converToString(result)

    return finalResult


expandMatrix = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]


def expand(array, table):
    """Function to expand the array using table."""
    # Returning expanded result
    return [array[element - 1] for element in table]


def XOR(list1, list2):
    """Function to return the XOR of two lists."""
    # Returning the xor of the two lists
    return [element1 ^ element2 for element1, element2 in zip(list1, list2)]


def DESEncryption(text, key, extension):
    if extension == True:
        text = addExtension(text)

    ciphertext = DES(text, key, True)

    return ciphertext
