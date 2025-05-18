import math
import sqlite3
import logging
import os

# Ensure directories exist
os.makedirs(os.path.join(os.path.dirname(__file__), '../../logs'), exist_ok=True)
os.makedirs(os.path.join(os.path.dirname(__file__), '../../data'), exist_ok=True)

logging.basicConfig(
    filename=os.path.join(os.path.dirname(__file__), '../../logs/app.log'),
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

DB_PATH = os.path.join(os.path.dirname(__file__), '../../data/results.db')


def simple_sieve(limit):
    """
    Return a list of all primes <= limit using the Sieve of Eratosthenes.
    """
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def generate_pairs(n):
    """Generate n pairs of numbers that are 1 and 5 mod 6."""
    pairs = []
    num = 5
    while len(pairs) < n:
        if num % 6 == 1 or num % 6 == 5:
            pairs.append((num, num + 2))
            num += 4
        else:
            num += 1
    return pairs

def count_valid_multiples(start, end, num):
    """Count valid multiples of num in range [start, end] not divisible by 2 or 3."""
    lcm = num * 6 // math.gcd(num, 6)
    first_multiple = math.ceil(start / num) * num
    while first_multiple % 2 == 0 or first_multiple % 3 == 0:
        first_multiple += num
    last_multiple = (end // num) * num
    while last_multiple % 2 == 0 or last_multiple % 3 == 0:
        last_multiple -= num
    if first_multiple > last_multiple:
        return 0
    count = (math.floor((last_multiple - first_multiple) / lcm) * 2 +
             math.ceil((lcm - (first_multiple % 6 - 1)) / 6) +
             math.ceil((lcm - (first_multiple % 6 - 5)) / 6))
    return count

def count_all_valid_multiples(a, b):
    """
    Count all valid multiples for prime numbers up to floor(sqrt(a)) in range [a^2, b^2].
    Only considers primes >= 5.
    """
    start, end = a**2, b**2
    # Generate only prime divisors up to floor(sqrt(a))
    limit = int(math.sqrt(a))
    primes = [p for p in simple_sieve(limit) if p >= 5]
    total_count = 0
    for num in primes:
        total_count += count_valid_multiples(start, end, num)
    return total_count

def save_result_to_db(pair, count, db_path=DB_PATH):
    """Save a result to the SQLite database."""
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pair_start INTEGER,
            pair_end INTEGER,
            count INTEGER
        )
    ''')
    c.execute(
        'INSERT INTO results (pair_start, pair_end, count) VALUES (?, ?, ?)',
        (pair[0], pair[1], count)
    )
    conn.commit()
    conn.close()
    logging.info(f"Saved result for pair {pair}: {count}")

def process_and_cache_pairs(n):
    """Process n pairs and cache results to DB."""
    pairs = generate_pairs(n)
    for pair in pairs:
        count = count_all_valid_multiples(pair[0], pair[1])
        save_result_to_db(pair, count)
        logging.info(f"Processed pair {pair}: {count}")

if __name__ == "__main__":
    logging.info("Starting square-island computation...")
    process_and_cache_pairs(100)
    logging.info("Computation complete.")