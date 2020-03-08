from euler.maths.prime import generate_to_sie
from euler.util.decorators import timed_function


def q51():
    prime_numbers = generate_to_sie(10 ** 6)
    for prime_number in prime_numbers:
        prime_number_string = str(prime_number)
        digit_count = len(prime_number_string)

        # for number_of_digit_to_change(1, digit_count+1):


    return -1


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert (timed_function(q51)() == -1)
