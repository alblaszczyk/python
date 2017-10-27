def friend(x):
    friends_lst = []
    for i in x:
        if len(i) == 4:
            friends_lst.append(i)
    return friends_lst
