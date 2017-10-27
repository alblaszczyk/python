x = [5,6,3,124,46,67,4567,2,345]

def simply_the_best(x):
    max_value = x[0]
    for i in x:
        if max_value < i:
            max_value = i
    return max_value

print simply_the_best(x)



    # max_value = x[0
    #for i in x:
        #if i in x:
            #if x[i] > x[i+1]:
                #max_value = x[i]
                #print(max_value)
            #else:
                #max_value = x[i+1]
        #return max_value
