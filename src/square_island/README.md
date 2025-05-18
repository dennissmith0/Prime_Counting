# island.py

`island.py` implements the “square‑island” counting algorithm for prime candidates in intervals of the form [\((6k-1)^2\), \((6k+1)^2\)].

## Table of Contents

- [Overview](#overview)  
- [Requirements](#requirements)  
- [Usage](#usage)  
- [Functions](#functions)  
  - [`generate_pairs(n)`](#generate_pairsn)  
  - [`count_valid_multiples(start, end, num)`](#count_valid_multiplesstart-end-num)  
  - [`count_all_valid_multiples(a, b)`](#count_all_valid_multiplesa-b)  
- [Example Output](#example-output)  
- [Performance Considerations](#performance-considerations)  
- [Future Improvements](#future-improvements)  

## Overview

This script provides a fast arithmetic approach to count how many multiples of each potential divisor (excluding 2 and 3) “block” the candidate positions for primes in each square‑island. It does **not** enumerate primes directly, but computes the total number of non‑prime slots, which can be subtracted from the total candidate count to infer the count of primes.

The interval for island \(k\) is:
\[
\text{start} = (6k - 1)^2,\quad \text{end} = (6k + 1)^2.
\]

## Requirements

- Python 3.6 or higher  
- No external dependencies beyond the standard library  

## Usage

1. **Run the script**  
   ```bash
   python island.py
   ```
   By default, `main()` generates the first 100 square‑island pairs and prints the blocked‑slot count for each.

2. **Custom number of islands**  
   Edit the call in `main()`:
   ```python
   pairs = generate_pairs(<your_desired_n>)
   ```

3. **Integrate as a module**  
   ```python
   from island import generate_pairs, count_all_valid_multiples

   pairs = generate_pairs(50)
   for a, b in pairs:
       blocked = count_all_valid_multiples(a, b)
       total_candidates = (b**2 - a**2 + 1) * 2 // 6
       estimated_primes = total_candidates - blocked + 2  # include 2 and 3
       print(f"Island [{a**2},{b**2}]: primes ≈ {estimated_primes}")
   ```

## Functions

### `generate_pairs(n)`

Generates a list of `n` pairs \((a, b)\) such that:
- \(a = 6k - 1\), \(b = a + 2 = 6k + 1\)  
- Both \(a\) and \(b\) are valid prime candidates (≡1 or 5 mod 6).

**Parameters**  
- `n` (int): number of pairs to generate.

**Returns**  
- `List[Tuple[int, int]]`: first `n` \((a, b)\) pairs.

### `count_valid_multiples(start, end, num)`

Counts how many multiples of `num` in the range `[start, end]` fall on positions **not** divisible by 2 or 3 (i.e., valid “prime‑candidate” residues).

**Algorithm Highlights**  
1. Compute `lcm = lcm(num, 6)` to determine the repeating cycle of valid residues.  
2. Locate the first and last multiples of `num` within `[start, end]` that satisfy `mod 2 != 0` and `mod 3 != 0`.  
3. Use arithmetic to count how many such multiples occur every `lcm` steps, with edge‑case corrections.

**Parameters**  
- `start` (int): lower bound of the interval.  
- `end` (int): upper bound of the interval.  
- `num` (int): the divisor to test (should be ≥5, odd, and not divisible by 3).

**Returns**  
- `int`: count of valid multiples of `num` in the interval.

### `count_all_valid_multiples(a, b)`

Aggregates the counts for all `num` in `[5, √a]` that are odd and not multiples of 3.

**Parameters**  
- `a` (int), `b` (int): defines the interval `[a², b²]`.

**Returns**  
- `int`: total blocked‑slot count across all divisors up to √a.

## Example Output

```text
Pair 1: (5, 7) - Count: 4
Pair 2: (7, 9) - Count: 8
...
Pair 100: (601, 603) - Count: 23800
```

## Performance Considerations

- **Time complexity**: O(√n) per island (looping divisors up to √(6k−1)²).  
- **Memory**: minimal, only a few integer variables and counters.  
- **Accuracy**: relies on correct edge‑case handling in `ceil`/`floor` arithmetic.

## Future Improvements

- **Prime filtering**: use a small sieve to loop only prime `num` values instead of all odd non‑3‑divisible integers.  
- **Vectorization**: leverage NumPy or C-extension for hot loops.  
- **Parallelization**: split islands across multiple threads or processes.  
- **Enumeration**: after counting, reconstruct actual prime lists and twin pairs if needed.