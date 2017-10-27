def printer_error(s):
    correct = 'abcdefghijklm'
    control_no = 0
    total = len(s)
    for i in s:
        if i not in correct:
            control_no += 1
    return '{}/{}'.format(control_no, total)
