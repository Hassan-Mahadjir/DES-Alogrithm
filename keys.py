from convert import converToBinary
from permutation import permutation, keyPermutationMatrix1, keyPermutationMatrix2
from divide_to_bytes import nSplit

SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def generateKeys(key):
    keys = []
    key = converToBinary(key)

    key = permutation(key, keyPermutationMatrix1)

    left_block, right_block = nSplit(key, 28)

    for i in range(16):
        left_block, right_block = leftShift(left_block, right_block, SHIFT[i])
        temp = left_block + right_block
        # Permutation on shifted key to get next key
        keys.append(permutation(temp, keyPermutationMatrix2))

    return keys


def leftShift(list1, list2, n):
    """Function to left shift the arrays by n."""
    # Left shifting the two arrays
    return list1[n:] + list1[:n], list2[n:] + list2[:n]
