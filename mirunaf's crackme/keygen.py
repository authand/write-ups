def main():
    for i in range(100):
        print(f"{i}:{gen_key(i)}")

def gen_key(original_input):
    copy_input = original_input # mov eax, edx
    copy_input <<= 2 # shl eax, 2
    copy_input += original_input # add eax, edx
    copy_input <<= 2 # shl eax, 2
    copy_input += 4 # add eax, 4

    return copy_input

main()