def getCount(inputStr):
    num_vowels = 0
    vowels = 'aeiou'
    for i in inputStr:
        if i.lower() in vowels:
            num_vowels += 1
    return num_vowels
