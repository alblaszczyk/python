# -*- coding: utf-8 -*-
import string

def cleanse(x):
    x = x.replace(" ","")
    x = x.lower()
    x = x.translate(None, string.punctuation)
    return x

def reverse(x):
    result = ""
    length = len(x)

    for i in x:
        result += x[length - 1]
        length -= 1

    result = cleanse(result)
    return result

def better_palindrome(x):
    if cleanse(x) == reverse(x):
        return True
    else:
        return False
        
print better_palindrome('Sit on a potato pan, Otis')
