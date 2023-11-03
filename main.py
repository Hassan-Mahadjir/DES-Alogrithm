from convertTobits import converToBinary
from permutation import permutation, initialPermutationMatrix
plain_text = "helloooo"
key = "hassan"

# while len(key) != 8:
#     print("Invalid Key. Key should be of 8 length (8 bytes)., Enter different Key")
#     key = input("Enter Key (key should be of 8 length (8 bytes): ")

plain_text_bits = converToBinary(plain_text)
key_bits = converToBinary(key)
print([bit for bit in plain_text_bits])
print()
block = permutation(plain_text_bits, initialPermutationMatrix)
print(block)
print(len(block))
print(len(plain_text_bits))
