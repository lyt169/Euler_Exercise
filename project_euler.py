__author__ = 'F056831'

%matplotlib inline
import time
import math

########################################################################################################################
# return first n prime numbers in a list
def first_n_primes(n):
    upper_bound_n = int(n * math.log1p(n) + n * (math.log1p(math.log1p(n)) - 0.9385)) + 1
    num_range = range(2, upper_bound_n + 1)

    # sieve of Eratosthenes: multiples ? ?n
    multiple_range = range(2, int(math.sqrt(upper_bound_n) + 1))

    # list of non-primes where js are multiples of i in multiple_range
    non_primes = [j for i in multiple_range for j in range(i * 2, upper_bound_n + 1, i)]
    # this list will be unsorted and contains duplicates
    non_primes = set(non_primes)

    # https://stackoverflow.com/questions/2104305/finding-elements-not-in-a-list
    primes = [p for p in num_range if p not in non_primes]

    return primes

def all_primes_less_than_n(n):
    num_range = range(2, n + 1)

    # sieve of Eratosthenes: multiples ? ?n
    multiple_range = range(2, int(math.sqrt(n) + 1))

    # list of non-primes where js are multiples of i in multiple_range
    non_primes = [j for i in multiple_range for j in range(i * 2, n + 1, i)]
    # this list will be unsorted and contains duplicates
    non_primes = set(non_primes)

    # https://stackoverflow.com/questions/2104305/finding-elements-not-in-a-list
    primes = [p for p in num_range if p not in non_primes]

    return primes


def q2():
    #####################    Project Euler  ########################
    #  Q2
    # x = [1,2]
    # i = 2
    #
    # while True:
    #     x.append(x[i-1] + x[i-2])
    #     i = i+1
    #     if x[i-1] > 4000000:
    #         del x[i-1]
    #         break
    #
    # sum(x[1::3])

    x = [1,1,2]
    s = 2

    while True:
        x[0] = x[1] + x[2]
        x[1] = x[0] + x[2]
        x[2] = x[0] + x[1]

        if x[2] > 4000000:
            break
        else:
            s = s + x[2]
    print(s)

########################################################################################################################
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
def q3():

    ########################################################################################################################

    x = 600851475143
    y = x
    p = 2   # starter

    while p < y:
        while y % p == 0:
            y = y / p
        p += 1

    print ('the largest factor of ' + str(x) + ' is ' + str(p - 1))

########################################################################################################################
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 � 99
# Find the largest palindrome made from the product of two 3-digit numbers.
def q4():
    # num_list = lambda num: map(int, str(num))
    # list_num = lambda num: int(''.join(str(i) for i in num))
    # all_num = list(range(x_min, x_max))

    start_time = time.clock()
    i = 999
    palindrome = [10000, 100, 100]

    while i >= 100:
        j = 999
        while j >= 100:
            n = i * j
            if n > palindrome[0] and str(n) == str(n)[::-1]:
                palindrome[0] = n
                palindrome[1] = i
                palindrome[2] = j
                break
            j -= 1
        i -= 1

    print(str(palindrome[0]) + ' = ' + str(palindrome[1]) + ' * ' + str(palindrome[2]))
    print time.clock() - start_time, "seconds"
    # 0.158 sec. Further simplification in maths, Begoner's thread on Mon, 23 May 2005, 00:15 is  10 times faster.

########################################################################################################################
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def q5():

    # method: for each number up to 20, record the frequency of prime factors as a list
    # take the maximum freq for each prime factor and multiply them together
    import time
    import numpy as np

    start_time = time.clock()
    prime = [2,3,5,7,11,13,17,19]       # all prime numbers under 20

    def prime_factors(n):
        f = [0] * len(prime)

        for i in range(len(prime)):              # for each prime number smaller than input number
            while n % prime[i] == 0:        # if input is evenly divisible by prime number
                n /= prime[i]                   #   divide by prime
                f[i] += 1                       #   AND counter + 1
            i += 1                          # once indivisible, check the next prime number
        return f

    factors = []
    for y in range(2, 21):
        factors.append(prime_factors(y))

    max_factors = np.amax(factors, axis=0)

    result = np.product([j**k for j, k in zip(prime, max_factors)])

    print(result)
    print time.clock() - start_time, "seconds"

########################################################################################################################
# Problem 6
# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 ? 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def q6():

    x = 0
    y = 0

    for i in range(1,101):
        x += i ** 2
        y += i

    print(y**2 - x)

########################################################################################################################
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def q7():

    # method: for numbers up to 10bn, use the Sieve of Eratosthenes (ca 240 BC)
    # Make a list of all the integers less than or equal to n (greater than one) and strike out the multiples of all primes
    # less than or equal to the square root of n, then the numbers that are left are the primes. (See also our glossary page.)
    # https://primes.utm.edu/prove/prove2_1.html

    # however, I don't want to create a list of primes, hence they suggested Wheel Factorization.
    # Method: divide by 2, 3 and 5; and then by all the numbers congruent to 1, 7, 11, 13, 17, 19, 23, and 29 modulo 30
    # again stopping when you reach the square root.
    # but modular arithmetic as per above requires n*((sqrt(n)-5) + 3) iterations + mini loop to check congruents.
    # it seems convoluted to me.
    # https://primes.utm.edu/glossary/page.php?sort=WheelFactorization
    # http://www.primesdemystified.com/

    # Then I found Wilson's Theorem
    # Wilson's theorem states that a natural number n > 1 is a prime number if and only if the product of all the positive
    # integers less than n is one less than a multiple of n
    # http://www.math.cornell.edu/~putnam/modular.pdf
    import time

    def all_primes_upto_n(n):
        list = [2, 3, 5, 7]                   # initial list: first 4 primes
        n_less_1_factorial = 9*8*7*6*5*4*3*2  # for n = 10
        if n < 10:
            return [x for x in list if x <= n]
        else:
            for p in range(11, n + 1):
                n_less_1_factorial *= (p - 1)

                if (n_less_1_factorial + 1) % p == 0:
                    list.append(p)
            return list

    def nth_prime_number(n):
        n_less_1_factorial = 1                  # initial (n-1)!
        i = 2 + 1                               # starting after 1st prime, hence 3
        counter = 1                             # nth prime found

        while counter < n:
            n_less_1_factorial *= (i - 1)* (i - 2)

            if (n_less_1_factorial + 1) % i == 0:
                counter += 1

            i += 2                              # skip all evens
        return i - 2

    start_time = time.clock()
    nth_prime_number(10001)
    print time.clock() - start_time, "seconds"
    # 20.8813556837 seconds

    #http://www.secnetix.de/olli/Python/list_comprehensions.hawk

    """
    I'm using G. Robin's improved formula to find an upper bound for n where n ? 7022
    https://www.maa.org/sites/default/files/jaroma03200545640.pdf
    p_n ? n log n + n(log log n ? 0.9385).
    https://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number
    """

def q7_list_comprehension():

    # ANS 104743

    import math
    import time

    start_time = time.clock()
    n = 10001
    # G Robin's upper bound of nth prime
    upper_bound_n = int(n * math.log1p(n) + n * (math.log1p(math.log1p(n)) - 0.9385)) + 1
    num_range = range(2, upper_bound_n + 1)

    # sieve of Eratosthenes: multiples ? ?n
    multiple_range = range(2, int(math.sqrt(upper_bound_n) + 1))

    # list of non-primes where js are multiples of i in multiple_range
    # this list will be unsorted and contains duplicates
    non_primes = [j for i in multiple_range for j in range(i * 2, upper_bound_n + 1, i)]
    non_primes = set(non_primes)

    # inverse list of non-: This is very slow
    # https://stackoverflow.com/questions/2104305/finding-elements-not-in-a-list
    primes = [p for p in num_range if p not in non_primes]
    print primes[n-1]

    # 104743
    # 146.480933589 seconds

    print time.clock() - start_time, "seconds"

    def nth_prime_number(n):
        upper_bound_n = int(n * math.log1p(n) + n * (math.log1p(math.log1p(n)) - 0.9385)) + 1
        num_range = range(2, upper_bound_n + 1)

        # sieve of Eratosthenes: multiples ? ?n
        multiple_range = range(2, int(math.sqrt(upper_bound_n) + 1))

        # list of non-primes where js are multiples of i in multiple_range
        non_primes = [j for i in multiple_range for j in range(i * 2, upper_bound_n + 1, i)]
        # this list will be unsorted and contains duplicates
        non_primes = set(non_primes)

        # inverse list of non-: This is very slow
        # https://stackoverflow.com/questions/2104305/finding-elements-not-in-a-list
        primes = [p for p in num_range if p not in non_primes]

        return primes[n-1]

    import math

########################################################################################################################
# Problem 8
# The four adjacent digits in the 1000-digit number that have the greatest product are 9 � 9 � 8 � 9 = 5832
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
def q8():

    # The four adjacent digits in the 1000-digit number that have the greatest product are 9 � 9 � 8 � 9 = 5832
    # Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
    # 73167176531330624919225119674426574742355349194934
    # 96983520312774506326239578318016984801869478851843
    # 85861560789112949495459501737958331952853208805511
    # 12540698747158523863050715693290963295227443043557
    # 66896648950445244523161731856403098711121722383113
    # 62229893423380308135336276614282806444486645238749
    # 30358907296290491560440772390713810515859307960866
    # 70172427121883998797908792274921901699720888093776
    # 65727333001053367881220235421809751254540594752243
    # 52584907711670556013604839586446706324415722155397
    # 53697817977846174064955149290862569321978468622482
    # 83972241375657056057490261407972968652414535100474
    # 82166370484403199890008895243450658541227588666881
    # 16427171479924442928230863465674813919123162824586
    # 17866458359124566529476545682848912883142607690042
    # 24219022671055626321111109370544217506941658960408
    # 07198403850962455444362981230987879927244284909188
    # 84580156166097919133875499200524063689912560717606
    # 05886116467109405077541002256983155200055935729725
    # 71636269561882670428252483600823257530420752963450

    import numpy as np

    x = str(73167176531330624919225119674426574742355349194934)
    x += str(65727333001053367881220235421809751254540594752243)
    x += str(85861560789112949495459501737958331952853208805511)
    x += str(96983520312774506326239578318016984801869478851843)
    x += str(12540698747158523863050715693290963295227443043557)
    x += str(66896648950445244523161731856403098711121722383113)
    x += str(62229893423380308135336276614282806444486645238749)
    x += str(30358907296290491560440772390713810515859307960866)
    x += str(70172427121883998797908792274921901699720888093776)
    x += str(52584907711670556013604839586446706324415722155397)
    x += str(53697817977846174064955149290862569321978468622482)
    x += str(83972241375657056057490261407972968652414535100474)
    x += str(82166370484403199890008895243450658541227588666881)
    x += str(16427171479924442928230863465674813919123162824586)
    x += str(17866458359124566529476545682848912883142607690042)
    x += str(24219022671055626321111109370544217506941658960408)
    x += str('07198403850962455444362981230987879927244284909188')
    x += str(84580156166097919133875499200524063689912560717606)
    x += str('05886116467109405077541002256983155200055935729725')
    x += str(71636269561882670428252483600823257530420752963450)

    max_prod = 1

    for i in range(0, 988):   # last start is 988th number, index 987, range excl last number.
        slice_13 = x[i:13 + i]

        if len(filter(lambda k: k == '0', slice_13)) == 0:      # if there is no 0 in the list
            list_13 = [long(j) for j in slice_13]               # use long, if you use int, you will drop the largest prod and get [[9, 7, 8, 1, 7, 9, 7, 7, 8, 4, 6, 1, 7], 2091059712, 503]
            if np.product(list_13) > max_prod:
                max_i = i
                max_list = list_13
                max_prod = np.product(list_13)

    print([max_list, max_prod, max_i])
    # [[9, 7, 8, 1, 7, 9, 7, 7, 8, 4, 6, 1, 7], 2091059712, 987]

########################################################################################################################
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
def q9():
    for a in range(1, 332):
        for b in range(a + 1, 1000 - a):
            c = ((a**2) + (b**2)) ** 0.5
            if a + b + c == 1000:
                answer = a * b * c
                break

    print([a, b, c, answer])

########################################################################################################################
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def q10():

    import math
    import time

    start_time = time.clock()


    def all_prime_less_than(n):
        #upper_bound_n = int(n * math.log1p(n) + n * (math.log1p(math.log1p(n)) - 0.9385)) + 1
        num_range = range(2, n + 1)

        # sieve of Eratosthenes: multiples ? ?n
        multiple_range = range(2, int(math.sqrt(n) + 1))

        # list of non-primes where js are multiples of i in multiple_range
        non_primes = [j for i in multiple_range for j in range(i * 2, n + 1, i)]
        # this list will be unsorted and contains duplicates
        non_primes = set(non_primes)

        # inverse list of non-: This is very slow
        # https://stackoverflow.com/questions/2104305/finding-elements-not-in-a-list
        primes = [p for p in num_range if p not in non_primes]

        return primes

    print sum(all_prime_less_than(2000000))
    print time.clock() - start_time, "seconds"

    # output
    # 142913828922
    # 4.01048755827 seconds

########################################################################################################################
# Problem 11
# In the 20�20 grid below, four numbers along a diagonal line have been marked in red.
# The product of these numbers is 26 � 63 � 78 � 14 = 1788696.
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20�20 grid?

def q11():

    # ANSWER 180604
    grid = 	[[8, 2,22,97,38,15, 0,40, 0,75, 4, 5, 7,78,52,12,50,77,91, 8],
            [49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48, 4,56,62, 0],
            [81,49,31,73,55,79,14,29,93,71,40,67,53,88,30, 3,49,13,36,65],
            [52,70,95,23, 4,60,11,42,69,24,68,56, 1,32,56,71,37, 2,36,91],
            [22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
            [24,47,32,60,99, 3,45, 2,44,75,33,53,78,36,84,20,35,17,12,50],
            [32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
            [67,26,20,68, 2,62,12,20,95,63,94,39,63, 8,40,91,66,49,94,21],
            [24,55,58, 5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
            [21,36,23, 9,75, 0,76,44,20,45,35,14, 0,61,33,97,34,31,33,95],
            [78,17,53,28,22,75,31,67,15,94, 3,80, 4,62,16,14, 9,53,56,92],
            [16,39, 5,42,96,35,31,47,55,58,88,24, 0,17,54,24,36,29,85,57],
            [86,56, 0,48,35,71,89, 7, 5,44,44,37,44,60,21,58,51,54,17,58],
            [19,80,81,68, 5,94,47,69,28,73,92,13,86,52,17,77, 4,89,55,40],
            [04,52, 8,83,97,35,99,16, 7,97,57,32,16,26,26,79,33,27,98,66],
            [88,36,68,87,57,62,20,72, 3,46,33,67,46,55,12,32,63,93,53,69],
            [4,42,16,73,38,25,39,11,24,94,72,18, 8,46,29,32,40,62,76,36],
            [20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74, 4,36,16],
            [20,73,35,29,78,31,90, 1,74,31,49,71,48,86,81,16,23,57, 5,54],
            [1,70,54,71,83,51,54,69,16,92,33,48,61,43,52, 1,89,19,67,48]]

    max_product = 0

    # i = down        j = across
    for i in range(0, 20):
        for j in range(0, 20):
            if j < 17:
                max_product = max(max_product, grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3])

            if i < 17:
                max_product = max(max_product, grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j])

            if i < 17 and j < 17:
                max_product = max(max_product, grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3])

            if i < 17 and j > 2:
                max_product = max(max_product, grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] * grid[i + 3][j - 3])

    print max_product


    # Output 51267216     ----- somehow this answer is wrong.........
    # Try 2 Output 70600674                         ,   left diagonal logic was wrong,i+1 j-1

########################################################################################################################
# Problem 12 - 	Highly divisible triangular number

# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be
# 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?
def q12():
    import math
    import numpy as np
    import time

    def prime_exponents_plus_1(n):
        prime_bound = math.log1p(n) / math.log1p(2)
        list_prime = first_100_primes[0 : int(prime_bound) + 2]
        list_ei_plus_1 = [1] * len(list_prime)

        for i in range(0, len(list_prime)):
            while n % list_prime[i] == 0 and n > 1:
                list_ei_plus_1[i] += 1
                n //= list_prime[i]
            i += 1
        return list_ei_plus_1

    start_time = time.clock()

    first_100_primes = first_n_primes(100)
    n = 1
    t = 1

    while np.product(prime_exponents_plus_1(t)) < 500:
        n += 1
        t += n

    print t
    print time.clock() - start_time, "seconds"


    # Output 76576500
    # 0.135099573122 seconds

    ##############
    # Reference .......
    # Approach 1: I try to find rules to determine the upper bound and lower bound of N for N having D divisors. 180614

    # upper bound for number of divisors
    # Inequality:t(n) <= 2*sqrt(n)
    # https://codeforces.com/blog/entry/14463

    # Lower bound for number of divisors
    # https://www.sciencedirect.com/science/article/pii/S0022314X05001009
    # This is particularly difficult to understand.....

    # Then I realised this is an Euler 500 question.
    # https://stackoverflow.com/questions/31270226/how-to-calculate-smallest-number-with-certain-number-of-divisors

    # Let's go back to an easier approach.....
    # https://www.math.upenn.edu/~deturck/m170/wk2/numdivisors.html
    # https://ideone.com/JNRMsQ
    # Maximum number of divisors of any number less than 1000000 = 240
    # Maximum number of divisors of any number less than 1000000000 = 1344

    # n_range = range(1000000,1000000001)
    # n_range_sum = [reduce(lambda x, y: x+y, range(1,p + 1)) for p in n_range]
    #
    # sum_to_999999 = reduce(lambda x, y: x+y, range(1,1000000))
    # n_range_sum = n_range_sum + sum_to_999999

    # finding the upper bound of prime factors for n
    # https://www.quora.com/Is-there-a-relation-between-a-number-and-its-largest-prime-factor

    # Maximum number of divisors of any number less than 1000000 = 240

    # first_100_primes = first_n_primes(100)
    # number = range(1, 20000)
    # triangle_number = list(map(lambda x: np.sum(number[:x]), number))

    # for n in triangle_number:
    #     if np.product(prime_exponents_plus_1(n)) > 500:
    #         print n
    #         break

    # Output 76576500
    # 9.70111876255 seconds in total
    # 9.52584185775 seconds  to generate the triangle numbers
    # 0.176853981415 seconds

########################################################################################################################
# Problem 13
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

import numpy as np
def q13():

    def numbers():
        return [37107287533902102798797998220837590246510135740250,
                46376937677490009712648124896970078050417018260538,
                74324986199524741059474233309513058123726617309629,
                91942213363574161572522430563301811072406154908250,
                23067588207539346171171980310421047513778063246676,
                89261670696623633820136378418383684178734361726757,
                28112879812849979408065481931592621691275889832738,
                44274228917432520321923589422876796487670272189318,
                47451445736001306439091167216856844588711603153276,
                70386486105843025439939619828917593665686757934951,
                62176457141856560629502157223196586755079324193331,
                64906352462741904929101432445813822663347944758178,
                92575867718337217661963751590579239728245598838407,
                58203565325359399008402633568948830189458628227828,
                80181199384826282014278194139940567587151170094390,
                35398664372827112653829987240784473053190104293586,
                86515506006295864861532075273371959191420517255829,
                71693888707715466499115593487603532921714970056938,
                54370070576826684624621495650076471787294438377604,
                53282654108756828443191190634694037855217779295145,
                36123272525000296071075082563815656710885258350721,
                45876576172410976447339110607218265236877223636045,
                17423706905851860660448207621209813287860733969412,
                81142660418086830619328460811191061556940512689692,
                51934325451728388641918047049293215058642563049483,
                62467221648435076201727918039944693004732956340691,
                15732444386908125794514089057706229429197107928209,
                55037687525678773091862540744969844508330393682126,
                18336384825330154686196124348767681297534375946515,
                80386287592878490201521685554828717201219257766954,
                78182833757993103614740356856449095527097864797581,
                16726320100436897842553539920931837441497806860984,
                48403098129077791799088218795327364475675590848030,
                87086987551392711854517078544161852424320693150332,
                59959406895756536782107074926966537676326235447210,
                69793950679652694742597709739166693763042633987085,
                41052684708299085211399427365734116182760315001271,
                65378607361501080857009149939512557028198746004375,
                35829035317434717326932123578154982629742552737307,
                94953759765105305946966067683156574377167401875275,
                88902802571733229619176668713819931811048770190271,
                25267680276078003013678680992525463401061632866526,
                36270218540497705585629946580636237993140746255962,
                24074486908231174977792365466257246923322810917141,
                91430288197103288597806669760892938638285025333403,
                34413065578016127815921815005561868836468420090470,
                23053081172816430487623791969842487255036638784583,
                11487696932154902810424020138335124462181441773470,
                63783299490636259666498587618221225225512486764533,
                67720186971698544312419572409913959008952310058822,
                95548255300263520781532296796249481641953868218774,
                76085327132285723110424803456124867697064507995236,
                37774242535411291684276865538926205024910326572967,
                23701913275725675285653248258265463092207058596522,
                29798860272258331913126375147341994889534765745501,
                18495701454879288984856827726077713721403798879715,
                38298203783031473527721580348144513491373226651381,
                34829543829199918180278916522431027392251122869539,
                40957953066405232632538044100059654939159879593635,
                29746152185502371307642255121183693803580388584903,
                41698116222072977186158236678424689157993532961922,
                62467957194401269043877107275048102390895523597457,
                23189706772547915061505504953922979530901129967519,
                86188088225875314529584099251203829009407770775672,
                11306739708304724483816533873502340845647058077308,
                82959174767140363198008187129011875491310547126581,
                97623331044818386269515456334926366572897563400500,
                42846280183517070527831839425882145521227251250327,
                55121603546981200581762165212827652751691296897789,
                32238195734329339946437501907836945765883352399886,
                75506164965184775180738168837861091527357929701337,
                62177842752192623401942399639168044983993173312731,
                32924185707147349566916674687634660915035914677504,
                99518671430235219628894890102423325116913619626622,
                73267460800591547471830798392868535206946944540724,
                76841822524674417161514036427982273348055556214818,
                97142617910342598647204516893989422179826088076852,
                87783646182799346313767754307809363333018982642090,
                10848802521674670883215120185883543223812876952786,
                71329612474782464538636993009049310363619763878039,
                62184073572399794223406235393808339651327408011116,
                66627891981488087797941876876144230030984490851411,
                60661826293682836764744779239180335110989069790714,
                85786944089552990653640447425576083659976645795096,
                66024396409905389607120198219976047599490197230297,
                64913982680032973156037120041377903785566085089252,
                16730939319872750275468906903707539413042652315011,
                94809377245048795150954100921645863754710598436791,
                78639167021187492431995700641917969777599028300699,
                15368713711936614952811305876380278410754449733078,
                40789923115535562561142322423255033685442488917353,
                44889911501440648020369068063960672322193204149535,
                41503128880339536053299340368006977710650566631954,
                81234880673210146739058568557934581403627822703280,
                82616570773948327592232845941706525094512325230608,
                22918802058777319719839450180888072429661980811197,
                77158542502016545090413245809786882778948721859617,
                72107838435069186155435662884062257473692284509516,
                20849603980134001723930671666823555245252804609722,
                53503534226472524250874054075591789781264330331690]
    number = numbers()     # just so I can hide the list away
    total_10 = '1'

    def first_n_digits(i):
        return list(map(lambda x: int(str(x)[:i]), number))

    for i in range(1, 50):
        sum_i = np.sum(first_n_digits(i))

        if total_10[:10] == str(sum_i)[:10]:        # if precision is fine
            break

        total_10 = str(sum_i)                       # replace with higher precision
        i += 1

    return int(total_10[:10])
# output 5537376230


########################################################################################################################
# Problem 14
# The following iterative sequence is defined for the set of positive integers:
#
# n  n/2 (n is even)
# n  3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13  40  20  10  5  16  8  4  2  1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

import math

def chain(n):
    step = 1
    power = math.log1p(2)

    while n != 1:

        # if n is even, half n. if n is odd, 3n + 1
        if n % 2 == 0:

            # optimiser 1: if new n is a power of 2, reduce down to 1.
            if math.log1p(n) % power == 0:
                step += (math.log1p(n) / power)     # exponent = number of steps
                n = 1

            else:
                n /= 2
        else:
            n = 3 * n + 1

        step += 1

    return step

def calculate_steps():
    n = 1000000

    step = 1
    max_step = 1
    max_number = 1

    while n > 333333:         # optimiser 2: no need to look under 333333 = (1000000 - 1)/ 3
        step = chain(n)
        if max_step < chain(n):
            max_step == step
            max_number == n

    n -= 1
    print max_number, max_step

# Write a function that generates all consistent expressions involving parentheses, for a given number of pairs.
# Consistent means you never close a parentheses that wasn�t previously open.
#
# n = 1:     ()
# n = 2:     (()), ()()
# n = 3:     ((())), (()()),  (())(), ()(()), ()()()


import numpy as np
import itertools

def brackets(n):
    a = range(1, n+1)                       # generate 1,2,3,4,...,n
    b = list(np.repeat(a, a))               # generate 1,2,2,3,3,3,4,4,4,4,...

    c = set(itertools.combinations(b, n))   # calculate all unique combinations of b,
    # counter = 0

    for x in c:
        f = ''
        g = [0] * n

        for i in a:
            g[i-1] = sum(1 for y in x if y == i)

            if sum(g[:i]) <= i and x[n-1] == n:
                f = f + '(' + ')' * g[i-1]

        if len(f) == n*2 : print f      #counter += 1
    # return counter




