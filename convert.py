from divide_to_bytes import nSplit


def converToString(array):
    # Chunking array of bits to 8-sized bytes
    byteChunks = nSplit(array, 8)

    # Converting each byte to char and then concatenating
    result = ''.join([chr(int(''.join(map(str, byte)), 2))
                     for byte in byteChunks])

    # Returning result
    return result


def converToBinary(text):
    """Function to convert a string into a list of bits."""
    # Initializing variable required
    bitArray = []
    for letter in text:
        # Getting binary (8-bit) value of letter
        binVal = binValue(letter, 8)
        # Making list of the bits
        binValArr = [int(x) for x in binVal]
        # Appending the bits to array
        bitArray.extend(binValArr)

    # Returning answer
    return bitArray


def binValue(val, bitSize):
    """Function to return the binary value as a string of given size."""
    binVal = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]

    # Appending with the required number of zeros in front
    while len(binVal) < bitSize:
        binVal = "0" + binVal

    # Returning binary value
    return binVal
