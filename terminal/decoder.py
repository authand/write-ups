import textwrap

def main():
    block_size = 7
    key = "214277"
    binary = "00101011111011111111000010001000110110111101111010111001000001001100011101001110011100110100111010000001011100111100101"

    padding_needed = (block_size - len(binary) % block_size) % block_size
    padded_binary = binary + '0' * padding_needed

    chunks = textwrap.wrap(padded_binary, block_size)

    decrypted_message = ""
    key_index = 0

    for chunk in chunks:
        rotation_amount = int(key[key_index])
        rotated_chunk = chunk[rotation_amount:] + chunk[:rotation_amount]

        decimal_value = int(rotated_chunk, 2)
        character = chr(decimal_value)
        decrypted_message += character

        key_index = (key_index + 1) % len(key)

    print(decrypted_message)

main()
