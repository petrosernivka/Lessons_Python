def is_prime(n):
    if n in (0, 1):
        return False
    num_prime = []
    i = 2
    for i in range(2, n + 1):
        check = 0
        for j in num_prime:
            if n % j == 0:
                check += 1
        if check == 0:
            num_prime.append(i)
    return True if n in num_prime else False
