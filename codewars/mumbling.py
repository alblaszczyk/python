def accum(s):
    counter = 1
    lst = []
    for i in s:
        lst.append(i.lower() * counter)
        counter += 1
    my_string = '-'.join(str(i) for i in lst)
    return my_string.title()
