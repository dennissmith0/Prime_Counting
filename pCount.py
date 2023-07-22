import time

def createList(r1, r2):
    # Testing if range r1 and r2 are equal
    if (r1 == r2):
        return r1

    else:

        # Create empty lists
        res = [] # reserve
        poss = [] # possible primes
        mult = [] # multiples of primes

        # loop to append successors to list until r2 is reached.
        while(r1 < r2+1):

            res.append(r1)
            r1 += 1

            """
            # extract all multiples of 6 from reserve list
            multiples_6 = [n for n in res if n % 6 == 0]
            # convert list to int
            multiples_6 = [int(x) for x in multiples_6]
            """

        # extract all multiples of 6 from reserve list
        multiples_6 = [n for n in res if n % 6 == 0]
          # convert list to int
        multiples_6 = [int(x) for x in multiples_6]


        # create list with + 1 and - 1 values from each multiple of 6 
          # because these are the only numbers that can be prime
        for val in multiples_6:
          poss.append(val-1)
          poss.append(val+1)


        # create list of multiples with all poss2ible combinations of elements in the possible list, unless that value exceeds r2
        mult.append(poss[0]*poss[0])
        start = 0
        print('Poss Length:', len(poss)-1)

        for i in range(len(poss)):
          #print(i)
          #for y in range(start,len(poss)):
          for y in range(i,len(poss)):
            val = poss[i]*poss[y]
            #print(val)
            upperLimit = r2
            if val <= upperLimit and val not in mult:    # NEED CONDITION: if upperLimit is a multiple of 6, minus one from the account
                mult.append(val)
                # start =+ 1
            elif val >= upperLimit:
                break
          #if val >= upperLimit:
          #  break
          if val >= upperLimit * 2:
            break
        
        #print(poss)
        #print(mult)


        # subtract the amount of multiples from the amount of possible primes, add 2 (for 2 and 3), and this is the amount of primes up to upperLimit
        return len(poss) - len(mult) + 2, #mult, poss



exit = "N"

while exit.upper() != "Y":

  # Driver Code
  r1, r2, = 2, int(input("Enter an integer: ")),
  start = time.time()

  print(createList(r1, r2,))


  end = time.time()
  print('Time ', end - start)

  exit = input("Would you like to exit? (Y/N)")
  

