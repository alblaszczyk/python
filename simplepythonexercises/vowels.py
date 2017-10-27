VOWELS = 'aeiouy'
def yes_vowels(x):
    counter = 0
    for letter in x:
        if letter in VOWELS:
            counter += 1
            return counter
    if counter > 0:
        return True
    else:
        return False

print yes_vowels('zmrzsln')
