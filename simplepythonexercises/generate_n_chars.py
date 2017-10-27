def generate_n_chars(n,c):
    counter = 0
    for i in range(n):
        counter += 1
    return c * counter

print generate_n_chars(5,'*')
