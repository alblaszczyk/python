x = ['chuj', 'matrioszka', 'oj']

def longest_word(x):
    lst = []
    for i in x:
        lst.append(len(i))
    max_value = lst[0]
    for i in lst:
        if max_value < i:
            max_value = i
    return max_value

print longest_word(x)
