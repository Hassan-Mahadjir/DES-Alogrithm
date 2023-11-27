from convertTobits import converToBinary
from permutation import permutation, initialPermutationMatrix
plain_text = "helloooow"
key = "hassan"
isExtensionRequired = (len(plain_text) % 8 != 0)
print(isExtensionRequired)

# while len(key) != 8:
#     print("Invalid Key. Key should be of 8 length (8 bytes)., Enter different Key")
#     key = input("Enter Key (key should be of 8 length (8 bytes): ")

plain_text_bits = converToBinary(plain_text)
key_bits = converToBinary(key)


# print(plain_text_bits)
# # print()

# block = permutation(plain_text_bits, initialPermutationMatrix)
# print(block)
