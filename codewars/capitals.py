def capitals(word):
    upper_list = []
    for i, c in enumerate(word):
        if c == c.upper():
            upper_list.append(i)
    return (upper_list)
