import functools

from euler.util.prime import prime_numbers_smaller_than


def find_gcd(number1, number2):
    bigger, smaller = max(number1, number2), min(number1, number2)
    mod = bigger % smaller
    while mod > 1:
        bigger, smaller = smaller, mod
        mod = bigger % smaller

    return mod == 0 and smaller or mod


def multiply(*prime_powers):
    multiplied = {}
    for prime_power in prime_powers:
        for prime, power in prime_power.items():
            multiplied[prime] = multiplied.get(prime, 0) + power

    return multiplied


def decompose_to_prime_powers(number, primes=None):
    """ Decomposes a given number into a set of prime number paired with
    powers which multiplied out, gives the original number

        Args
        ----
            :param number: int
                The given number to decompose

            :param primes: list
                Prime numbers that does not exceed the number

        Returns
        -------
            {
                N1: P1,
                N2: P2,
                N3: P3,
                ...
                Nm, Pm,
            } ... (N1 ^ P1) * (N2 ^ P2) * ... = number
    """
    if primes is None: primes = prime_numbers_smaller_than(number)

    prime_composition = {}
    for prime_number in primes:
        while not number % prime_number:
            prime_composition[prime_number] = prime_composition.get(prime_number, 0) + 1
            number /= prime_number
            if number == 1:
                return prime_composition

    assert False, "Bad Programmer Error"


def multiply_out_numbers_in_powers(number_in_powers):
    """ Finds the multiplicative sum [pi] of factors with indicated powers

    :param number_in_powers: dict
    :returns: (key ^ value) * (key ^ value) ...
    """
    powers = [number ** power for number, power in number_in_powers.items()]
    return functools.reduce(lambda x, y: x * y, powers)