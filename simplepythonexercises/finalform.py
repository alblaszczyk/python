VOWELS = 'aeiouy'

def translate(x):
    finalform = ''
    for letter in x:
        if letter in VOWELS or letter == " ":
            finalform = finalform + letter
        elif letter not in VOWELS:
            finalform = finalform + letter + "o" + letter
    return finalform
print translate('srutututu majtki z drutu')
