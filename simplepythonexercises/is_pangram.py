import string
def is_pangram(gram):
    return all(i in gram.lower() for i in string.ascii_lowercase)

gram = "a quick brown fox jumps over the lazy dog"

print is_pangram(gram)
