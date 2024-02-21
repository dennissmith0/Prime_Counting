import time
from pCount import create_and_count, create_and_count_optimized #create_and_count_optimized_with_set
#from pCount_og import createList

def main():
    # start_time = time.time()
    # print(createList(2, 100000))  # Should print 9592 for 10k
    # print('Time for original code: ', time.time() - start_time)

    # # Now let's compare the performance of the refactored code and the optimized code.
    start_time = time.time()
    print(create_and_count(1000000))  # Should print 9592 for 10k
    print('Time for refactored code: ', time.time() - start_time)

    # start_time = time.time()
    # print(create_and_count_optimized(100))  # Should print 9592 for 10k
    # print('Time for optimized code: ', time.time() - start_time)
    
    # start_time = time.time()
    # print(create_and_count_optimized_with_set(1000000))  # Should print 9592 for 10k
    # print('Time for optimized code with set: ', time.time() - start_time)
    


if __name__ == "__main__":
    main()
