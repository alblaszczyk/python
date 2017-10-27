# Make sure that the_flying_circus() returns True
def the_flying_circus():
    if (5 > 4) and (5 >= 5):
        return True
    elif 6 > 5 and not 10 == 10:
        return True
    else:
      return False
    return the_flying_circus()
