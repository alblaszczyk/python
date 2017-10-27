# -*- coding: utf-8 -*-
def reverse(x):
    result = ""
    length = len(x)

    for i in x:
        result += x[length - 1]
        length -= 1

    return result

print reverse("Matkoboska, ja się zabiję")
