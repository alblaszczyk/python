def sequence_sum(begin_number, end_number, step):
    lst = [x for x in range(begin_number, end_number + 1)]
    counter = 0
    for x in lst[::step]:
        counter += x
    return counter
