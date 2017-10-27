wordlist = ['hello', 'mike', 'alcohol', 'konstantynopolitanczykowianeczka', 'oh']

def map_my_words(x):
    lst = []
    for i in x:
        lst.append(len(i))
    return lst
print map_my_words(wordlist)
