class Primes_class():
    def first(self, n):
        num_prime = [2,3]
        i = 5
        while len(num_prime) < n + 1:
            num_prime.append(i) if all(i % j for j in num_prime[:int(i**(1/2.7))]) else False
            i += 2 if i > 2 else 1
        return num_prime[:n]

Primes = Primes_class()
