import time

# Function to find amount of twin primes within a given range of squares of input numbers
def find_twin_primes_between_squares(input_pair):
    lower_square = input_pair[0] ** 2
    upper_square = input_pair[1] ** 2
    twin_primes_in_range = []  # List to keep track of twin primes within the square range

    # Initialize lists to keep track of primes and twin primes
    primes = [2, 3]  # Initial prime numbers

    # Function to check if a number is prime
    def is_prime(n):
        for prime in primes:
            if n % prime == 0:
                return False
        return True

    # Loop through numbers up to upper_square in the form 6k ± 1
    for k in range(1, (upper_square // 6) + 2):  # 6 * k_max will be just over upper_square
        for delta in [-1, 1]:
            num = 6 * k + delta
            if num > upper_square:
                break
            if num > 3 and is_prime(num):  # We skip 2 and 3, as they are already in the list
                primes.append(num)

    # Check for twin primes within the square range
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2:
            if lower_square < primes[i] < upper_square:
                print(f"Twin prime found on square island: {primes[i]}, {primes[i + 1]}")
                twin_primes_in_range.append((primes[i], primes[i + 1]))

    return  input_pair, twin_primes_in_range, len(twin_primes_in_range)

# Test the function with input pair (p, p + 2)
start_time = time.time()
print(find_twin_primes_between_squares((5627, 5629)))
print('Time: ', (time.time() - start_time) / 60, ' minutes')
