import math

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
    
    # Find first valid multiple >= start
    first_multiple = math.ceil(start / num) * num
    while first_multiple % 2 == 0 or first_multiple % 3 == 0:
        first_multiple += num
    
    # Find last valid multiple <= end
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
    """Count all valid multiples for numbers up to sqrt(a) in range [a^2, b^2]."""
    start, end = a**2, b**2
    total_count = 0
    for num in range(5, int(math.sqrt(a)) + 1):
        if num % 2 != 0 and num % 3 != 0:
            total_count += count_valid_multiples(start, end, num)
    return total_count

def main():
    pairs = generate_pairs(100)  # Generate first 10 pairs
    for i, (a, b) in enumerate(pairs):
        count = count_all_valid_multiples(a, b)
        print(f"Pair {i+1}: ({a}, {b}) - Count: {count}")

if __name__ == "__main__":
    main()