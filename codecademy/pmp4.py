def digit_sum(n):
    stringified = str(n)
    listified = []
    count = 0
    for i in stringified:
        listified.append(i)
    for i in listified:
        count += int(i)
    return count
