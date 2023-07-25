# Prime Counting Algorithms

This repository contains two Python scripts that calculate the number of prime numbers up to a given limit `n`.

## Algorithm 1: Original Version

The original version, `pCount_og.py` of the algorithm first generates a list of all multiples of 6 up to `n`. It then generates a list of "possible primes" - numbers that are 1 more or 1 less than a multiple of 6. Following this, it generates a list of all possible products of these possible primes, and subtracts the length of this list from the length of the list of possible primes (plus 2, to account for the primes 2 and 3) to calculate the number of primes up to `n`.

The time complexity of this algorithm is O(n²), since it involves generating all possible products of the possible primes. The space complexity is also O(n²), due to storing these products in a list.

## Algorithm 2: Refactored Version

The refactored version, `pCount.py`, of the algorithm follows the same basic approach as the original version, but is written in a more "Pythonic" style using list comprehensions. However, it does not include the optimization from the original version that stops generating products as soon as a product exceeds `n`.

The time and space complexity of the refactored version are also O(n²) for the same reasons as the original version.

## Algorithm 3: Optimized Version

The optimized version, also in `pCount.py`, of the algorithm incorporates the optimization from the original version into the refactored code. It includes a break statement within the loop that generates the list of products, which stops the loop as soon as a product is found that exceeds `n`. This reduces the number of unnecessary calculations and the size of the list of products, resulting in a significant performance improvement.

The time complexity of the optimized version is still technically O(n²) in the worst-case scenario, but in practice it should be significantly faster than the other versions for large values of `n`. The space complexity is also reduced compared to the other versions, as the list of products is typically much smaller.

## Example:

Run `example.py` to see the refactored and optimized version concurrently count the amount of primes up to 100000.

```python
$ python example.py
9592
Time for refactored code:  72.72154593467712
9592
Time for optimized code:  4.55500054359436
```
