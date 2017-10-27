def disemvowel(string):
    vowels = 'aeiou'
    lstify = []
    for c in string:
        if c.lower() not in vowels:
            lstify.append(c)
        for c in lstify:
            string = ''.join(lstify)
    return string
