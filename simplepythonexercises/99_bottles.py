def standard_verse(i):
    print i, "bottles of beer on the wall,", i, "bottles of beer."
    i -= 1
    print "take one down, pass it around,", i, "bottles of beer on the wall."

def two_verse():
    print "2 bottles of beer on the wall, 2 bottles of beer."
    print "take one down, pass it around, 1 bottle of beer on the wall."

def one_verse():
    print "1 bottle of beer on the wall, 1 bottle of beer."
    print "take one down, pass it around, no more bottles of beer on the wall."

def no_verse():
    print "No more bottles of beer on the wall, no more bottles of beer."
    print "Go to the store, buy some more, 99 bottles of beer on the wall."

def song():
    for i in range(99,-1,-1):
        if i > 2:
            standard_verse(i)
        elif i == 2:
            two_verse()
        elif i == 1:
            one_verse()
        else:
            no_verse()

print song()
