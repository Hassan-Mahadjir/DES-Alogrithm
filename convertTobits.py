def converToBinary(plain_text):
    """This funciton will take text and return the binary equivlalent"""
    binary_text = ''.join(format(ord(i), '08b') for i in plain_text)
    return [int(bit) for bit in binary_text]
