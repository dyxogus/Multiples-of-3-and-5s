from euler.util.prime import is_prime


def spiral_primes():
    primes_encountered = 0
    none_primes = 0

    number = 1
    one_side = 1
    while none_primes > primes_encountered * 9:
        add_by = one_side * 2

        for _ in range(4):
            number += add_by

            if is_prime(number):
                primes_encountered += 1
            else:
                none_primes += 1

            one_side += 1

    return (one_side - 1) * 2 - 1