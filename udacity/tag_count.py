def tag_count(tokens):
    count = 0
    for token in tokens:
        if token[0] == '<' and token[-1] == '>':
            count += 1
    return count
