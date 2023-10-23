# Function to find blocked numbers within a given range
def find_blocked_numbers(upper_limit):
    # Initialize lists to keep track of primes and blocked numbers
    primes = [2, 3]  # Initial prime numbers
    blocked = []  # List to keep track of blocked numbers

    # Function to check if a number is prime
    def is_prime(n):
        for prime in primes:
            if n % prime == 0:
                return False
        return True

    # Loop through numbers up to upper_limit in the form 6k ± 1
    for k in range(1, (upper_limit // 6) + 2):  # 6 * k_max will be just over upper_limit
        for delta in [-1, 1]:
            num = 6 * k + delta
            if num > upper_limit:
                break
            if num > 3 and is_prime(num):  # We skip 2 and 3, as they are already in the list
                primes.append(num)
            elif num > 7:  # We start adding to blocked list only after 5 and 7
                blocked.append(num)

    return blocked, primes

# Test the function for numbers up to 100
print(find_blocked_numbers(300))
