
import time
from pCount import create_and_count, create_and_count_optimized

def main():
    # Now let's compare the performance of the refactored code and the optimized code.
    start_time = time.time()
    print(create_and_count(100000))  # Should print 9592
    print('Time for refactored code: ', time.time() - start_time)

    start_time = time.time()
    print(create_and_count_optimized(100000))  # Should print 9592
    print('Time for optimized code: ', time.time() - start_time)


if __name__ == "__main__":
    main()
