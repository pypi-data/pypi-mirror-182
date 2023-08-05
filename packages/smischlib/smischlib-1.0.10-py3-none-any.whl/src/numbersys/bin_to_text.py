def bin_to_text(bin):
    text = int(bin, 2).to_bytes((int(bin, 2).bit_length() + 7) // 8, 'big').decode()
    return text