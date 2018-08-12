def filter_list(l):
    new_l = []
    for i in l:
        if type(i) == int:
            new_l.append(i)
    return new_l
