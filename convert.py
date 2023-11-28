from divide_to_bytes import nSplit


# def converToBinary(text):
#     """This funciton will take text and return the binary equivlalent"""
#     binary_text = ''.join(format(ord(i), '08b') for i in text)
#     return [int(bit) for bit in binary_text]


def converToString(array):
    # Chunking array of bits to 8 sized bytes
    byteChunks = nSplit(array, 8)
    # Initializing variables required
    stringBytesList = []
    stringResult = ''
    # For each byte
    for byte in byteChunks:
        bitsList = []
        for bit in byte:
            bitsList += str(bit)
        # Appending byte in string form to stringBytesList
        stringBytesList.append(''.join(bitsList))
        print(stringBytesList)

    # Converting each stringByte to char (base 2 int conversion first)
    # and then concatenating
    result = ''.join([chr(int(stringByte, 2))
                     for stringByte in stringBytesList])

    # Returning result
    return result


def converToBinary(text):
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


def binValue(val, bitSize):
    """Function to return the binary value as a string of given size."""

    binVal = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]

    # Appending with required number of zeros in front
    while len(binVal) < bitSize:
        binVal = "0" + binVal

    # Returning binary value
    return binVal
