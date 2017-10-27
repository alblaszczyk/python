from math import sqrt
def is_square(n):
    if n < 0:
        return False
    else:
        if n % sqrt(n) == 0:
            return True
        else:
            return False
