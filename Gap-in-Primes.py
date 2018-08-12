def gap(g, m, n):
    prime = [2]
    m += (m + 1) % 2
    while prime[-1] < n:
        prime.append(m) if all(m % j for j in range(3, int(m**.5)+1)) else False
        m += 2 if m > 2 else 1
        if len(prime) > 1:
            if prime[-1] - prime[-2] == g:
                return [prime[-2], prime[-1]]
