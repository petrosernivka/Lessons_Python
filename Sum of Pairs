def sum_pairs(ints, s):
    passed_elem = set()
    for i in ints:
        if s - i in passed_elem:
            return [s - i, i]
        passed_elem.add(i)
