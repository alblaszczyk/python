a = ['x', 'z', 'a', 't', 'mama']
def is_member(x, a):
    for i in a:
        if x == i:
            return True
    else:
        return False
print is_member('c', a)
