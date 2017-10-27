squares = set()

# todo: populate "squares" with the set of all of the integers less
# than 2000 that are square numbers


# Note: If you want to call the nearest_square function, you must define
# the function on a line before you call it. Feel free to move this code up!
n = 1
while n**2 < 2000:
    squares.add(n**2)
    n += 1
