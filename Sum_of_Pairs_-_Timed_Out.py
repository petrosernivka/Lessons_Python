#1. Execution Timed Out:

def sum_pairs(ints, s):
    for n in range(1, len(ints)):
        for m in range(0, n):
            if ints[n] + ints[m] == s:
                return [ints[m], ints[n]]
#--------------------------------------------------------------------------------
                
#2. Execution Timed Out:

def sum_pairs(ints, s):
    for i in range(1, len(ints)):
        second_num = list(filter(lambda j: j + ints[i] == s , ints[0:i]))
        if second_num:
            return [second_num[0], ints[i]]
#--------------------------------------------------------------------------------

#3. Execution Timed Out:

def sum_pairs(ints, s):
    for i in range(1, len(ints)):
        if s - ints[i] in ints[0: i]:
            return [s - ints[i], ints[i]]
#--------------------------------------------------------------------------------

#4. Exit Code: 137

def sum_pairs(ints, s):
    import itertools
    pairs_elem = list(itertools.combinations(ints, 2))
    pairs_index = list(itertools.combinations(list(range(len(ints))), 2))
    min_sec_elem = 99999999
    rez = 0
    for i in pairs_elem:
        if sum(list(i)) == s and pairs_index[pairs_elem.index(i)][1] < min_sec_elem:
            min_sec_elem = pairs_index[pairs_elem.index(i)][1]
            rez = i
            
    return list(rez) if rez else None

