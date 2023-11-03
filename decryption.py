from bitarray import bitarray
# Convert bits to the orginal text
bit_stream = ""
bits = bitarray(bit_stream)
orignal_text = bits.tobytes().decode('ascii')
print("The normal string is: ", orignal_text)
