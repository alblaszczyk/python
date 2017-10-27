x = [3, 4, 5, 4, 3]

def histogram(x):
    line_count = 0
    for i in x:
        print '*' * i
        line_count += 1
    return line_count

histogram(x)
