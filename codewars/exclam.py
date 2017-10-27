def product(s):
    counter_a = 0
    counter_b = 0
    for c in s:
        if c == '!':
            counter_a += 1
        elif c == '?':
            counter_b += 1
    if counter_a and counter_b != 0:
        return counter_a * counter_b
    else:
        return 0
