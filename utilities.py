def binary_little_endian_to_int(array):
    byte_sum = 0
    multiplier = 1
    for byte in array:
        byte_sum += byte * multiplier
        multiplier *= 2**8
    return byte_sum


def binary_big_endian_to_int(array):
    byte_sum = 0
    multiplier = 1
    for byte in reversed(array):
        byte_sum += byte * multiplier
        multiplier *= 2**8
    return byte_sum


def binary_to_string(array):
    return array.decode()
