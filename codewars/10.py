def binary_array_to_number(arr):
    bin_join = '0b' + ''.join(str(i) for i in arr)
    return int(bin_join, 2)
