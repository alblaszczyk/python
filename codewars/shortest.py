def find_short(s):
    lst = s.split()
    smallest_length = []
    for i in lst:
        smallest_length.append(len(i))
    l = min(smallest_length)


    return l # l: shortest word length
