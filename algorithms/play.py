import time


# Standard Sieve of Eratosthenes to find the number of primes up to n
def standard_sieve(n):
    # Create a boolean array "prime[0..n]" and initialize all entries as true
    # A value in prime[i] will finally be false if i is Not a prime, otherwise true
    prime = [True for _ in range(n+1)]
    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    # Count and return the number of prime numbers
    return len([x for x in range(2, n+1) if prime[x]])

# Further optimized Sieve of Eratosthenes to strictly follow the form 6n +/- 1
def altered_sieve(n):
    # Create a boolean array "prime[0..n]" and initialize all entries as true.
    # A value in prime[i] will finally be false if i is Not a prime, otherwise true.
    prime = [True for _ in range(n+1)]
    
    # Manually set multiples of 2 and 3 as not prime
    for i in range(2, int(n / 2) + 1):
        prime[2 * i] = False
    for i in range(2, int(n / 3) + 1):
        prime[3 * i] = False
    
    # Start the sieve
    p = 5  # Starting from the next prime after 3
    w = 2  # The wheel to cycle through 6n - 1 and 6n + 1
    while p * p <= n:
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        
        # Increment by w to skip multiples of 2 and 3
        # and cycle through 6n - 1 and 6n + 1
        p += w
        w = 6 - w
    
    # Count and return the number of prime numbers
    # Adding 2 for the primes 2 and 3
    return len([x for x in range(5, n+1) if prime[x]]) + 2

# Implementing the "Multiples of Consequence" algorithm to find prime numbers
def multiples_of_consequence(n):
    # Initialize a list to keep track of potential primes
    # We'll mark the indices corresponding to non-primes as False
    is_prime = [True] * (n + 1)
    
    # Manually handle the cases for 2 and 3
    is_prime[0] = is_prime[1] = False
    for i in range(4, n + 1, 2):
        is_prime[i] = False
    for i in range(6, n + 1, 3):
        is_prime[i] = False
    
    # Start with a count of 2 for the primes 2 and 3
    prime_count = 2
    
    # Loop through potential primes (p) starting from 5
    for p in range(5, n + 1, 6):
        # Iterate over p and p + 2 (to cover both 6n - 1 and 6n + 1 forms)
        for base in [p, p + 2]:
            if base > n:
                break
            
            if not is_prime[base]:
                continue
            
            # Increment the prime count for base
            prime_count += 1
            
            # Calculate "Multiples of Consequence" for the current base
            for k in range(1, (n // base) + 1):
                for offset in [6 * k - 2, 6 * k]:
                    multiple = base + base * offset
                    if multiple > n:
                        break
                    is_prime[multiple] = False
    
    return prime_count

start_time = time.time()
print(standard_sieve(10000000))  # Should print 9592 for 10k
print('Time for standard Eratosthenes: ', time.time() - start_time)

# start_time = time.time()
# print(altered_sieve(10000))  # Should print 9592 for 10k
# print('Time for altered sieve: ', time.time() - start_time)

start_time = time.time()
print(multiples_of_consequence(10000000))  # Should print 9592 for 10k
print('Time for multiples of consequence: ', time.time() - start_time)

# start_time = time.time()
# print(multiples_of_consequence(100000))  # Should print 9592 for 10k
# print('Time for multiples of consequence numpy: ', time.time() - start_time)