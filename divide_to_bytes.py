def nSplit(text_list, size):
    return [text_list[i: i + size] for i in range(0, len(text_list), size)]
