VOWELS = 'aeiouy'
import sys
def translate(x):
    finalform = ''
    for letter in x:
        if letter in VOWELS or letter == " ":
            finalform = finalform + str(letter)
        elif letter not in VOWELS:
            finalform = finalform + str(letter) + "o" + str(letter)
    return finalform
print translate(sys.argv[1])
