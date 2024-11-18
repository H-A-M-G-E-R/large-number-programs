#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Calculate last digits of mega and tralum
# See https://kyodaisuu.github.io/mega/
# Author: Fish (original mega.py) and H A M (tralum and speedup)

# Use gmpy2 for faster calculations.
from gmpy2 import mpz

def main():
    """Calculate last digits of mega and tralum"""
    import sys
    import time
    # Since Python 3.11, there's a maximum limit of 4300 digits.
    sys.set_int_max_str_digits(100000)
    # Test that this program is working properly
    test()
    # Set the number you want to compute.
    if len(sys.argv) == 1:
        print('No argument specified. Defaulting to mega.')
        number = 'mega'
    else:
        number = sys.argv[1]
    # Calculate last digits of the number and save to a text file
    for d in (10, 100, 1000, 10000, 100000):  # for these digits
        time_sta = time.time()
        if number == 'mega':
            m = mega(d)
        elif number == 'tralum':
            m = tralum(d)
        else:
            raise Exception("Invalid number. Valid numbers: 'mega', 'tralum'")
        time_end = time.time()
        tim = time_end - time_sta
        filename = number + str(d) + '.txt'
        with open(filename, mode='w') as f:
            f.write(str(m))
        print('Last {0} digits of {1} calculated in {2:.3}s and written to {3}.'.format(
            d, number, tim, filename))


def test():
    """Test calculation"""
    assert pow2mod(23, 1) == 8
    assert pow2mod(1003, 3) == 8
    assert pow2mod(234000, 7) == 1749376
    for d in range(17):
        assert mega(d) == 1993539660742656 % (10**d)
    for d in range(18):
        assert tralum(d) == 40766388459274240 % (10**d)


def pow2mod(n, d):
    """Last d digits of 2^n. Namely 2^n mod (10^d)"""
    # From Euler's theorem, 2^φ(5^d) = 1 (mod 5^d)
    # where φ(5^d) = (5^d)(1-1/5) = 4*5^(d-1)
    # Therefore 2^(φ(5^d) + d) = 2^d (mod 10^d)
    # 2^n can be recursively calculated as 2^n = 2^((n-d) % φ(5^d) + d) (mod 10^d) for n>d
    if n > d:
        n = (n - d) % (4 * 5**(d-1)) + d
    # Now we calculate (2^n) mod (10^d)
    # We use pow function with modular exponentiation for efficient calculation.
    return pow(2, n, 10**d)


def pow256mod(n, d):
    """Last d digits of 256^n"""
    # 256^n = 2^(8 * n)
    # For the recursion of pow2 mod function to work, the result should be larger than d
    return (pow2mod(8*n, d) - d) % (10**d) + d


def mn(n, d):
    """Last d digits of m(n)

    where m(n) =
      (1) 0 when n = 0
      (2) 256^(m(n-1)) + m(n-1) otherwise
    """
    if n < 4:
        return (0, 1, 257, 256**257+257)[n] % (10**d)
    m = mn(n-1, d)
    m = pow256mod(m, d) + m
    return m % (10**d)


def mega(d):
    """Last d digits of mega"""
    d = mpz(d)
    if d < 1:
        return mpz(0)
    m = mn(mpz(256), d)
    m = pow256mod(m, d)
    m = pow256mod(m, d)
    return m


def f3(n, d):
    """Last d digits of f3(n) in the fast-growing hierarchy

    where f3(n) = f2^n(n), and f2(n) = 2^n*n
    """
    m = n
    for i in range(n):
        m = pow2mod(m, d) * m
    return m % (10**d)


def tralum(d):
    """Last d digits of tralum"""
    d = mpz(d)
    if d < 1:
        return mpz(0)
    return f3(mpz(10), d)


if __name__ == '__main__':
    main()
