import time


def create_and_count(n):
    # List of possible primes
    poss = [val + delta for val in range(6, n+1, 6) for delta in (-1, 1)]

    # Create list of all products of possible primes (multiples)
    mult = {i * j for i_index, i in enumerate(poss) for j in poss[i_index:] if i * j <= n}

    # Number of primes is difference of possible primes and multiples, plus 2 (for 2 and 3)
    return len(poss), len(mult) #+ 2


def create_and_count_optimized(n):
    # Create list of all multiples of 6 up to n
    #multiples_6 = [x for x in range(2, n+1) if x % 6 == 0]

    # Create list of all numbers 1 more or 1 less than a multiple of 6 (possible primes)
    #poss = [val + delta for val in multiples_6 for delta in (-1, 1) if val + delta <= n]
    poss = [val + delta for val in range(6, n+1, 6) for delta in (-1, 1) if val + delta <= n]


    # Create list of all products of possible primes (multiples)
    mult = set()
    for i_index, i in enumerate(poss):
        for j in poss[i_index:]:
            product = i * j
            if product > n:
                break
            mult.add(product)

    # Number of primes is difference of possible primes and multiples, plus 2 (for 2 and 3)
    return len(poss) - len(set(mult)) + 2
