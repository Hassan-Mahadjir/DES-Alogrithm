from convertTobits import converToBinary
from permutation import permutation, initialPermutationMatrix
plain_text = "helloooohelloooohelloooohelloooo"
key = "hassan"

# while len(key) != 8:
#     print("Invalid Key. Key should be of 8 length (8 bytes)., Enter different Key")
#     key = input("Enter Key (key should be of 8 length (8 bytes): ")

plain_text_bits = converToBinary(plain_text)
key_bits = converToBinary(key)

isPaddingRequired = (len(plain_text_bits) % 8 != 0)

print([int(bit) for bit in plain_text_bits])
# print()

block = permutation(plain_text_bits, initialPermutationMatrix)
# print(block)


def binValue(val, bitSize):
    """Function to return the binary value as a string of given size."""

    binVal = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]

    # Appending with required number of zeros in front
    while len(binVal) < bitSize:
        binVal = "0" + binVal

    # Returning binary value
    return binVal


def stringToBitArray(text):
    """Funtion to convert a string into a list of bits."""

    # Initializing variable required
    bitArray = []
    for letter in text:
        # Getting binary (8-bit) value of letter
        binVal = binValue(letter, 8)
        # Making list of the bits
        binValArr = [int(x) for x in list(binVal)]
        # Apending the bits to array
        bitArray += binValArr

    # Returning answer
    return bitArray


function_array = stringToBitArray(plain_text)
print(function_array)


for i in range(len(function_array)):
    if function_array[i] != int(plain_text_bits[i]):
        print(f"false {i}")
    else:
        print(True)
