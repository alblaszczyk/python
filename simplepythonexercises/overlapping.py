x = [1,2,3,4]
y = [7,6,5,9]
def overlapping(x,y):
    for element_1 in x:
        for element_2 in y:
            if element_1 == element_2:
                return True
    else:
        return False
print overlapping(x,y)
