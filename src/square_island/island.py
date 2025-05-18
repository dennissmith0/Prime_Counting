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

def count_blocked_by_prime(start, end, p):
    """
    Count j in [start,end] with j % p == 0 and j % 6 in (1,5).
    """
    first = math.ceil(start / p) * p
    count = 0
    n = first
    while n <= end:
        if n % 6 in (1, 5):
            count += 1
        n += p
    return count

def count_blocked_positions(a, b):
    """
    Count all positions in [a^2, b^2] that are blocked by a prime p with 5 <= p < a.
    A position j is blocked by p if j % p == 0 and j % 6 in (1,5).
    """
    start, end = a * a, b * b
    # Generate all primes up to b, consider only those with 5 <= p < a
    primes = [p for p in simple_sieve(b) if p >= 5 and p < a]
    total_count = 0
    for p in primes:
        total_count += count_blocked_by_prime(start, end, p)
    return total_count

def count_raw_p3_positions(a, b):
    """
    Total prime-candidate slots (≡1 or 5 mod 6) in island [a^2, b^2], before removing corners.
    """
    return (b * b - a * a + 1) // 3

def count_effective_p3_positions(a, b):
    """
    Prime-candidate slots in island [a^2, b^2] minus the two corner positions a^2 and b^2.
    """
    return count_raw_p3_positions(a, b) - 2

def count_primes_in_island(a, b):
    """
    Returns the number of primes in the island [a^2, b^2] using the p3 method.
    """
    blocked = count_blocked_positions(a, b)
    total_candidates = count_effective_p3_positions(a, b)
    return total_candidates - blocked

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
        count = count_blocked_positions(pair[0], pair[1])
        save_result_to_db(pair, count)
        logging.info(f"Processed pair {pair}: {count}")

if __name__ == "__main__":
    logging.info("Starting square-island computation...")
    process_and_cache_pairs(100)
    logging.info("Computation complete.")