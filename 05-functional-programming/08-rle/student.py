def rle_encode(data):
    if not data:
        return

    current_char = None
    count = 0

    for char in data:
        if current_char is None:
            current_char = char
            count = 1
        elif char == current_char:
            count += 1
        else:
            yield current_char, count
            current_char = char
            count = 1

    if current_char is not None:
        yield current_char, count



def rle_decode(data):
    for char, count in data:
        for _ in range(count):
            yield char


data = "AAABBCCCC"
encoded_data = rle_encode(data)

decoded_data = ''.join(rle_decode(encoded_data))

print(decoded_data)
