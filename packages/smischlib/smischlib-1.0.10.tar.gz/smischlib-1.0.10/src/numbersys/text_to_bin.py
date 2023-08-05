def text_to_bin(text):
    binary = bin(int.from_bytes(text.encode(), 'big'))
    return binary[2:]
