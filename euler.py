# Helper functions for Project Euler problems
# syntaxaire


# From Problem 1: Multiples of 3 and 5
# final solution for hackerrank, O(1)
def sum_of_multiples_of_n_up_to_m(n, m, inclusive=True):
    """Return the sum of the multiples of n up to (or under) m.
    Example: the sum of multiples of 3 under 17 is 3 + 6 + 9 + 12 + 15 = 45.
    See: https://oeis.org/A045943"""
    if inclusive:
        count = m // n
    else:
        count = (m-1) // n
    term = n * count**2 + n * count
    term = term >> 1
    return term


# From Problem 3: Largest Prime Factor
def prime_factors(number):
    """
    Reduce a positive integer above 1 to its prime factors by trial division.
    """
    factors = []
    count = 2
    while count <= number:
        while not (number % count):
            factors.append(count)
            number = int(number / count)
        count += 1
    return factors


# From Problem 5: Smallest multiple
def lcm(number_list):
    """Return the least common multiple of a list of positive integers."""
    factored_list = []
    factor_set = set()
    product = 1
    for i in range(len(number_list)):
        temp_factors = prime_factors(number_list[i])
        factored_list.append(temp_factors)
        for j in temp_factors:
            factor_set.add(j)
    for factor in factor_set:
        product = product * (factor ** max([factored_list[x].count(factor)
                             for x in range(len(factored_list))]))
    return product


# From Problem 7: 10001st prime
def sieve_eratosthenes_up_to(limit):
    """Return a list of primes up to a specified positive integer above 1."""
    intarray = [True] * (limit + 1)  # [1] of the array is integer '1'
    intarray[0], intarray[1] = False, False
    for i in range(2, int(limit ** 0.5) + 1):
        if intarray[i]:
            for j in range(i ** 2, limit + 1, i):
                intarray[j] = False
    sieved = dict(zip(range(0, limit + 1), intarray))
    return list(i for i in sieved if sieved[i])


# From Problem 8: Largest product in a series
def digit_product(digits):
    """Return the product of the digits in a string of digits."""
    x = 1
    for i in digits:
        x *= int(i)
    return x


# From Problem 12: Highly divisible triangular number
def factor_list(number):
    """
    Return a sorted list containing all factors of a positive integer,
    including 1 and itself.
    """
    factors = set()
    for i in range(1, int(number ** 0.5) + 1):
        if not(number % i):
            factors.add(i)
            factors.add(number // i)
    factors = list(factors)
    factors.sort()
    return factors


# From Problem 12: Highly divisible triangular number
def gen_triangular_numbers():
    """Yield triangular numbers one at a time."""
    tri = 0
    seq = 0
    while True:
        seq += 1
        tri = tri + seq
        yield tri


# From Problem 14: Longest Collatz sequence
def gen_collatz(n):
    """Yield the Collatz sequence beginning with n, one term at a time."""
    yield n
    while n != 1:
        if n % 2:
            n = n * 3 + 1
            yield n
        else:
            n //= 2
            yield n


# From Problem 22: Names scores
def alphabet_position(x):
    """
    Return the alphabetical index of a character.
    (A == a == 1, Z == z == 26)
    """
    assert(x.isalpha())
    assert(len(x) == 1)
    if x.isupper():
        return(ord(x) - 64)
    if x.islower():
        return(ord(x) - 96)


# From Problem 23: Non-abundant sums
def isabundant(x):
    """Return True if x is an abundant number, False otherwise."""
    # proper divisors do not include the number being factored
    factors = euler.factor_list(x)[:-1]
    if sum(factors) > x:
        return True
    else:
        return False


# From Problem 25: 1000-digit Fibonacci number
def gen_fibonacci():
    """Yield the Fibonacci sequence one term at a time."""
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


# From Problem 28: Number spiral diagonals
def gen_number_spiral_diagonals(max):
    """
    Yield terms of the sequence of the diagonals on the spiral of positive
    integers up to max,  one at a time, where max is a positive integer.

    Example:
    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13
    Calling gen_number_spiral_diagonals(25) would yield
    1, 3, 5, 7, 9, 13, 17, 21, 25 in sequence.
    """
    term = 1
    inc = 2
    yield term
    while True:
        for _ in range(4):
            if term + inc > max:
                return
            term += inc
            yield term
        inc += 2


# From Problem 35: Circular primes
def rotations(s):
    """Return a list containing the rotations of a string. If string is one character,
    the list contains only that character."""
    ret = list()
    if len(s) == 1:
        ret.append(s)
    else:
        for i in range(1, len(s) + 1):
            ret.append(s[len(s)-i:] + s[:len(s)-i])
    return ret


#