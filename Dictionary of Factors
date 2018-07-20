def factorsRange(n, m):
    dict_factors = {}
    for num in range(n, m + 1):
        factors = ['None']
        for i in range(2, num//(2 + num % 2) + 1):
            if num % i == 0:
                if factors[0] == 'None':
                    factors[0] = i
                else:
                    factors.append(i)
        dict_factors[num] = factors
    return dict_factors
