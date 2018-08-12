def solution(args):
    start = end = args[0]
    rez_fin = str(args[0])
    for i in args[1:]:
        if i == end + 1:
            end += 1
            if i == args[-1]:
                if end - 1 == start:
                    rez_fin += ',' + str(i)
                else:
                    rez_fin += '-' + str(i)
        else:
            if start == end:
                rez_fin += ',' + str(i)
            elif end - 1 == start:
                rez_fin += ',' + str(end) + ',' + str(i)
            else:
                rez_fin += '-' + str(end) + ',' + str(i)
            start = end = i
        
    return rez_fin
