def cleanse(x):
    x = x.replace(" ","")
    x = x.lower()
    return x

print cleanse("I must be getting old")
