import itertools
import logging
import math
import sys
from functools import reduce

import numpy

from euler.champernownes_constant import champernownes_constant
from euler.coin_sums import coin_sums
from euler.even_fibonacci import N2FibonacciIterator
from euler.largest_sum import first_n_digits_of_sum
from euler.longest_collatz_sequence import collatz_length
from euler.maths import prime
from euler.maths.matrix import (
    adjacent_multiplicand_string,
    adjacent_multiplicand,
    horizontal,
    left_diagonal,
    right_diagonal
)
from euler.maths.multiplications import greatest_common_denominator, lowest_common_multiple
from euler.maths.palindromes import is_palindrome_simple_string, generate_palindromes
from euler.maths.prime import generate_to_sie, is_prime, is_truncable_prime, generate_primes_in_digit_range
from euler.maths.sigma import (sigma_n, sigma_n2, )
from euler.maths.triangle_numbers import (
    is_triangle_number,
    pentagonal,
    hexagonal,
    is_pentagonal_number,
)
from euler.maximum_path_sum import Tree
from euler.names_scores import translate
from euler.reciprocal_cycles import string_division
from euler.strings.digits import all_digits_sorted, all_digits
from euler.strings.number_to_string import numerical_score, digit_sum_of_number
from euler.util.dates import calculate_number_of_days_in_month
from euler.util.fibonacci import FibonacciIterator


def q1():
    def fizz_buzz(x, lower_bound=2, fizz=3, buzz=5):
        """ Finds all multiples of 3s and 5s until the given number

        :param x :int (The upper bound to perform fizz buzz on)
        :param lower_bound :int
        :param fizz :int
        :param buzz :int
        """
        return [number for number in range(lower_bound, x + 1)
                if (number % fizz) == 0 or (number % buzz) == 0]

    def sigma_n_with_multiplier(upper_bound, multiplier):
        """ Finds multiplicative sum [pi] of multiplicand no bigger than the upper bound.
        The multiplication with multiplicand x 1, therefore it does not include 0

        This uses a simple property that 1 + 2 + 3 + 4 + 5 ... + (n-1) + n = (n + 1) x n/2
        Taking the example of multiplicand of 3,
        3 + 6 + 9 + 12 + 15 + ... 3n
            = 3 x 1 + 3 x 2 + 3 x 3 + ... 3 x n
            = 3 x (1 + 2 + 3 + ... n)
            = 3 x (n + 1) x n/2
            = m * (n + 1) x n/2
             [m being the multiplicand]

        Do note that n will be the highest multiple of multiplicand smaller than upper bound
            :: n = math.floor(upper_bound / multiplicand

        :param upper_bound :int
        :param multiplier :int
        """
        # Catch negative n cases as well as 0 case here
        if upper_bound < multiplier: return 0

        n = math.floor(upper_bound / multiplier)
        return multiplier * sigma_n(n)

    upper_bound = 999

    sum3 = sigma_n_with_multiplier(upper_bound, 3)
    sum5 = sigma_n_with_multiplier(upper_bound, 5)
    sum15 = sigma_n_with_multiplier(upper_bound, 15)

    return sum3 + sum5 - sum15


def q2():
    upper_bound = 4000000

    #
    fib_generator = FibonacciIterator()
    fib_generator.set_upper_bound(upper_bound)

    #
    fib_generator = N2FibonacciIterator()
    fib_generator.set_upper_bound(upper_bound)
    return sum(fib_generator.sequence)


def q3(number=600851475143):
    # Q3 :: Largest Prime Factor of 600851475143
    for index, prime_number in enumerate(prime.iterator(), 1):
        while number % prime_number == 0:
            number /= prime_number

        if number <= 1:
            return prime_number

        if index >= len(prime.PRIME_ENTRIES):
            prime._generate_next_prime()


def q4(digit_given=3):
    largest_number = 0
    x_was = 0

    for x in range(10 ** digit_given, 10 ** (digit_given - 1), -1):
        for y in range(10 ** digit_given - 1, 10 ** (digit_given - 1), -1):
            number = x * y
            if number > largest_number:
                if is_palindrome_simple_string(str(x * y)):
                    largest_number = number
                    if x_was > y: return number
                    x_was = x
            else:
                break

    return largest_number


def q5(up_to=20):
    if up_to <= 1: return up_to

    cumulative = 2
    for number in range(3, up_to + 1):
        cumulative = lowest_common_multiple(cumulative, number)

    return int(cumulative)


def q6(n=100):
    # Q6 :: Sum Square Difference
    square_of_sum = sigma_n(n) ** 2
    sum_of_square = sigma_n2(n)
    return square_of_sum - sum_of_square


def q7():
    return prime.nth_prime_number(10001)


def q8():
    """ Adjacent Multiplicand"""
    return adjacent_multiplicand_string(
        input_string='73167176531330624919225119674426574742355349194934969835203127'
                     '74506326239578318016984801869478851843858615607891129494954595'
                     '01737958331952853208805511125406987471585238630507156932909632'
                     '95227443043557668966489504452445231617318564030987111217223831'
                     '13622298934233803081353362766142828064444866452387493035890729'
                     '62904915604407723907138105158593079608667017242712188399879790'
                     '87922749219016997208880937766572733300105336788122023542180975'
                     '12545405947522435258490771167055601360483958644670632441572215'
                     '53975369781797784617406495514929086256932197846862248283972241'
                     '37565705605749026140797296865241453510047482166370484403199890'
                     '00889524345065854122758866688116427171479924442928230863465674'
                     '81391912316282458617866458359124566529476545682848912883142607'
                     '69004224219022671055626321111109370544217506941658960408071984'
                     '03850962455444362981230987879927244284909188845801561660979191'
                     '33875499200524063689912560717606058861164671094050775410022569'
                     '83155200055935729725716362695618826704282524836008232575304207'
                     '52963450',
        window_size=13,
    )


def q9():
    upper_bound = 1000
    for a in range(upper_bound // 2):
        for b in range(a):
            c = upper_bound - a - b

            if a * a + b * b == c * c:
                return a * b * c

    raise Exception('NOTHING_FOUND')


def q10():
    return sum(prime.generate_to_sie(2000000))


def q11():
    grid = [
        ['08', '02', '22', '97', '38', '15', '00', '40', '00', '75', '04', '05', '07', '78', '52', '12', '50', '77',
         '91', '08'],
        ['49', '49', '99', '40', '17', '81', '18', '57', '60', '87', '17', '40', '98', '43', '69', '48', '04', '56',
         '62', '00'],
        ['81', '49', '31', '73', '55', '79', '14', '29', '93', '71', '40', '67', '53', '88', '30', '03', '49', '13',
         '36', '65'],
        ['52', '70', '95', '23', '04', '60', '11', '42', '69', '24', '68', '56', '01', '32', '56', '71', '37', '02',
         '36', '91'],
        ['22', '31', '16', '71', '51', '67', '63', '89', '41', '92', '36', '54', '22', '40', '40', '28', '66', '33',
         '13', '80'],
        ['24', '47', '32', '60', '99', '03', '45', '02', '44', '75', '33', '53', '78', '36', '84', '20', '35', '17',
         '12', '50'],
        ['32', '98', '81', '28', '64', '23', '67', '10', '26', '38', '40', '67', '59', '54', '70', '66', '18', '38',
         '64', '70'],
        ['67', '26', '20', '68', '02', '62', '12', '20', '95', '63', '94', '39', '63', '08', '40', '91', '66', '49',
         '94', '21'],
        ['24', '55', '58', '05', '66', '73', '99', '26', '97', '17', '78', '78', '96', '83', '14', '88', '34', '89',
         '63', '72'],
        ['21', '36', '23', '09', '75', '00', '76', '44', '20', '45', '35', '14', '00', '61', '33', '97', '34', '31',
         '33', '95'],
        ['78', '17', '53', '28', '22', '75', '31', '67', '15', '94', '03', '80', '04', '62', '16', '14', '09', '53',
         '56', '92'],
        ['16', '39', '05', '42', '96', '35', '31', '47', '55', '58', '88', '24', '00', '17', '54', '24', '36', '29',
         '85', '57'],
        ['86', '56', '00', '48', '35', '71', '89', '07', '05', '44', '44', '37', '44', '60', '21', '58', '51', '54',
         '17', '58'],
        ['19', '80', '81', '68', '05', '94', '47', '69', '28', '73', '92', '13', '86', '52', '17', '77', '04', '89',
         '55', '40'],
        ['04', '52', '08', '83', '97', '35', '99', '16', '07', '97', '57', '32', '16', '26', '26', '79', '33', '27',
         '98', '66'],
        ['88', '36', '68', '87', '57', '62', '20', '72', '03', '46', '33', '67', '46', '55', '12', '32', '63', '93',
         '53', '69'],
        ['04', '42', '16', '73', '38', '25', '39', '11', '24', '94', '72', '18', '08', '46', '29', '32', '40', '62',
         '76', '36'],
        ['20', '69', '36', '41', '72', '30', '23', '88', '34', '62', '99', '69', '82', '67', '59', '85', '74', '04',
         '36', '16'],
        ['20', '73', '35', '29', '78', '31', '90', '01', '74', '31', '49', '71', '48', '86', '81', '16', '23', '57',
         '05', '54'],
        ['01', '70', '54', '71', '83', '51', '54', '69', '16', '92', '33', '48', '61', '43', '52', '01', '89', '19',
         '67', '48'],
    ]

    grid = list(map(lambda line: list(map(int, line)), grid))
    largest = 0
    for line in grid + horizontal(grid) + left_diagonal(grid) + right_diagonal(grid):
        largest = max(adjacent_multiplicand(line, 4), largest)

    return largest


def q13():
    """ Q13 :: Large Sum [https://projecteuler.net/problem=13]

    Work out the first ten digits of the sum of the following
        one-hundred 50-digit numbers.
    """
    with open('data/p013_numbers.txt') as numbers_file:
        numbers = [
            number.replace('\n', '')
            for number in numbers_file.readlines()
        ]

        return first_n_digits_of_sum(10, numbers)


def q14():
    """ Q14 :: Longest Collatz sequence [https://projecteuler.net/problem=14]

    Which starting number, under one million, produces the longest chain?
    """
    # This cannot be speed-up further without using Cython
    max_sequence_length = max_collatz_number = 0

    for number in range(1, 1000000):
        sequence_length = collatz_length(number)
        if max_sequence_length < sequence_length:
            max_sequence_length = sequence_length
            max_collatz_number = number

    return max_collatz_number


def q15(n=20):
    """ Triangle number with 'various degrees'

    Memory :: n
    Complexity :: n^2

    TODO :: extend for max(n, m) where it supports a rectangle rather than
    a square

    :param n: int
    :return:
    """
    paths = [1] * (n + 1)
    for _ in range(n):
        for index in range(1, n + 1):
            paths[index] += paths[index - 1]

    return paths[-1]


def q16():
    """ Q16 :: Digit of 2^1000"""
    # Do not use this method of digit sum - it's much faster to use
    #   power and digit_sum_of_number - it's for the sake of question
    #   (what if I had to do this only with multiplication and arrays?)

    # Faster Variant
    #     return digit_sum_of_number(pow(2, 1000))
    number, power = 2, 1000

    digits = [1]
    for _ in range(power):
        digits = [digit * number for digit in digits]
        for digit_index in range(len(digits)):
            # We can achieve the same with div operation but it's faster this way
            while digits[digit_index] >= 10:
                digits[digit_index] -= 10
                try:
                    digits[digit_index + 1] += 1

                except IndexError:
                    digits.append(1)

    return sum(digits)


def q17(start=1, up_to=1000):
    return sum(translate(number) for number in range(start, up_to))


def q18():
    tree = Tree('data/p018_tree.txt')
    maximum_path_sum = tree.find_maximum_path_sum()
    return maximum_path_sum


def q19():
    number_of_sundays_on_first = 0
    day_on_sunday = 6

    for year in range(1901, 2001):
        for month in range(1, 13):
            number_of_days_in_month = calculate_number_of_days_in_month(year, month)
            day_on_sunday = ((day_on_sunday - (number_of_days_in_month % 7)) % 7) or 7
            if day_on_sunday == 1: number_of_sundays_on_first += 1

    return number_of_sundays_on_first


def q20():
    """ Q20 :: Factorial digit sum [https://projecteuler.net/problem=20]

    Find the sum of the digits in the number 100!
        For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
        The sum of the digits for 10! = 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
    """
    import math
    return sum(map(int, str(math.factorial(100))))


def q22():
    with open('data/p022_names.txt', 'r') as file:
        names_text = file.readlines()[0]
        names = sorted(names_text.replace('"', '').split(','))
        name_scores = map(numerical_score, names)
        score_sum = sum(map(lambda score: score[0] * score[1], enumerate(name_scores, 1)))

    return score_sum


def q24():
    nth = 1000000
    zero_to = 9

    nth -= 1
    digit_offsets = []
    digits = list(range(zero_to + 1))

    for digit in reversed(digits):
        factorial = math.factorial(digit)
        digit_offsets.append(int(math.floor(nth / factorial)))
        nth %= factorial

    answer_digits = [digits.pop(nth_digit) for nth_digit in digit_offsets]
    return int(''.join(map(str, answer_digits)))


def q25():
    # TODO :: implement this one-liner
    return 4782


def q26():
    """ Q26 :: Reciprocal cycles [https://projecteuler.net/problem=26]

    Find value of d for which 1/d contains the longest recurring cycle
        in its decimal fraction part
    """
    calculated = map(string_division, range(2, 1000 + 1))
    n, _ = max(enumerate(calculated, 2), key=lambda x: x[1])
    return n


def q28():
    """ Q28 :: Number spiral diagonals [https://projecteuler.net/problem=28]

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral?
    """
    side_length = 1001
    one_side = (side_length - 1) // 2

    return int(((16 * (one_side ** 3) + 30 * (one_side ** 2) + 26 * one_side) / 3) + 1)


def q29():
    # TODO :: implement this one-liner
    return 9183


def q30(power=5):
    # This function ran quite slow so it needed to be optimised - hence less readability
    digit_powered = [0] + [pow(number, power) for number in range(1, 10)]

    upper_limit_digits = 1
    while upper_limit_digits < math.log10(9 ** power * upper_limit_digits): upper_limit_digits += 1
    upper_limit = 9 ** power * upper_limit_digits

    # For iteration, generators are faster, For sum, lists are faster
    # Favour sum(element for <iterable>) over sum(map(lambda, <iterable>))
    answers = [
        number for number in range(2, upper_limit)
        if sum([digit_powered[digit] for digit in all_digits(number)]) == number
    ]

    return sum(answers)


# noinspection PyDefaultArgument
def q31():
    return coin_sums(coin_total=200, coins_available=[1, 2, 5, 10, 20, 50, 100, 200])


def q33():
    answers = set()
    for a, b in itertools.product(set(range(1, 10)), repeat=2):
        original = a * 10 + b
        for d in range(1, 10):
            e = a
            denominator = d * 10 + e

            for c, f in itertools.permutations(range(1, 10), 2):
                bc = b * c
                df = d * f
                ef = e * f

                if ((a * c) + (bc // 10)) == (df + (ef // 10)):
                    if (bc % 10) == (ef % 10):
                        if bc == df:
                            answers.add((original, denominator))

    top, bottom = 1, 1
    for a, b in answers:
        top *= min(a, b)
        bottom *= max(a, b)

    return int(bottom / greatest_common_denominator(top, bottom))


def q34():
    precomputed_factorials = [math.factorial(i) for i in range(10)]

    # factorial(9) = 362880
    # factorial(9) * 8 = 2903040 < 10,000,000
    # factorial(9) * 7 = 2540160
    # factorial(9) * 6 + 2 = 2177282
    # Therefore upper range is 2177282 - we could go further
    # upper_limit = 2177282
    upper_limit = 40586  # but since i've ran this once and it runs slowly - i'll just use 40586 here

    answer = []
    for number in range(upper_limit):
        factorial_sum = sum([precomputed_factorials[digit] for digit in all_digits(number)])
        if factorial_sum == number: answer.append(number)

    answer.remove(1)
    answer.remove(2)

    return sum(answer)


def q35():
    number = 1000000

    circular_prime_numbers = []
    prime_numbers = generate_to_sie(number + 1)
    prime_number_set = set(prime_numbers)
    lowests = set()

    for prime in prime_numbers:
        digits = [character for character in str(prime)]
        circular_primes = set()
        for i in range(len(digits)):
            circular_prime_digits = digits[i:len(digits)] + digits[0:i]
            circular_primes.add(int(''.join(circular_prime_digits)))

        lowest_circular_primes = min(circular_primes)
        if lowest_circular_primes not in lowests:
            lowests.add(lowest_circular_primes)

            if all(circular_prime in prime_number_set for circular_prime in
                   circular_primes):
                circular_prime_numbers += circular_primes

    return len(circular_prime_numbers)


def q36():
    up_to_digit = 6
    double_base_palindromes = [
        palindrome for palindrome in generate_palindromes(up_to_digit)
        if palindrome % 2 == 1 and is_palindrome_simple_string(bin(palindrome)[2:])
    ]

    return sum(double_base_palindromes)


def q37():
    truncatable_primes = list(filter(lambda prime_number: is_truncable_prime(prime_number), generate_to_sie(100)))

    middle_digits = [1, 3, 7, 9]
    ending_digits = [3, 7]  # on either ends

    digit_length = 3
    while len(truncatable_primes) < 15:  # we are given there are 11 truncatable primes other than 4 primes < 10
        for start_digit in ending_digits:
            for end_digit in ending_digits:
                numbers = [start_digit * 10 ** (digit_length - 1) + end_digit]

                for digit_index in range(1, digit_length - 1):
                    numbers = [
                        number + middle_digit * 10 ** digit_index
                        for number in numbers
                        for middle_digit in middle_digits
                    ]

                truncatable_primes += filter(lambda n: is_truncable_prime(n, digit_length), numbers)

        digit_length += 1

    not_truncatable_primes = {2, 3, 5, 7}  # discounted only for this question
    return sum(set(truncatable_primes) - not_truncatable_primes)


def q40():
    return numpy.product([champernownes_constant(10 ** power) for power in range(7)])


def q42():
    with open('data/p042_words.txt') as text_file:
        words = map(lambda raw_word: raw_word.replace('"', ''), text_file.read().split(','))
        return reduce(lambda count, word: is_triangle_number(numerical_score(word)) and count + 1 or count, words, 0)


def q45():
    last_hexagonal = 1
    pn = 2
    while True:
        # find the next valid triangle-pentagonal (better because pentagonal > hexagonal)
        while not is_pentagonal_number(pn): pn += 1
        pentagonal_ = pentagonal(pn)

        # only need to check for last_hexagonal to current pentagonal
        for hn in range(last_hexagonal, pn):
            if pentagonal_ == hexagonal(hn):
                if pentagonal_ > 571:  # given in answer
                    # Reconstruct triangle number
                    return hn * (2 * hn - 1)

        # noinspection PyUnboundLocalVariable
        last_hexagonal = hn
        pn += 1


def q48():
    """ Q48 :: Self Powers [https://projecteuler.net/problem=48]

    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
    """
    return int(str(sum(map(lambda x: x ** x, range(1, 1000))))[-10:])


def q49(given_digit=4, repeating_count=3):
    from euler.util.array import is_all_same
    import operator

    grouped_by_digits = {}
    for number in generate_primes_in_digit_range(given_digit - 1, given_digit):
        digits = ''.join(all_digits_sorted(number))
        grouped_by_digits[digits] = grouped_by_digits.get(digits, []) + [number]

    permuting_primes = []
    for _, primes_with_same_digits in grouped_by_digits.items():
        for choice in itertools.combinations(primes_with_same_digits, repeating_count):
            differences = list(map(operator.sub, choice[1:], choice[:-1]))
            if is_all_same(differences):
                permuting_primes.append(choice)

    answer = list(filter(lambda list_: 1487 not in list_, permuting_primes))[0]  # exclude 1487 group given
    return ''.join(map(str, answer))


def q50(upper_limit=10 ** 6):
    prime_numbers = generate_to_sie(upper_limit)
    all_added = sum(prime_numbers)

    longest_prime_sum, longest_sequence_length = 0, 0
    for index, prime_number in enumerate(prime_numbers):
        if index > 5: break

        consecutive_sum = all_added
        for sequence_length, current in reversed(
                list(enumerate(prime_numbers[index + 1:]))):
            consecutive_sum -= current

            if consecutive_sum > upper_limit: continue
            if sequence_length < longest_sequence_length: break
            if is_prime(consecutive_sum) and longest_sequence_length < sequence_length:
                longest_prime_sum = consecutive_sum
                longest_sequence_length = sequence_length

        all_added -= prime_number

    return longest_prime_sum


def q56(up_to_number=100):
    return max(map(digit_sum_of_number, [
        pow(a, b)  # Use pow instead of math.pow to produce correct results
        for a in range(up_to_number - 1, 90, -1)
        for b in range(up_to_number - 1, 90, -1)
    ]))


def q57(number=1000):
    count = 0
    small, big = 0, 1
    for i in range(number):
        small, big = big, big * 2 + small
        if len(str(small + big)) > len(str(big)):
            count += 1

    return count


def q58():
    primes_encountered, none_primes = 0, 0
    number, one_side = 1, 1

    while none_primes <= primes_encountered * 9 or primes_encountered == 0 or none_primes == 0:
        add_by = one_side * 2

        for _ in range(4):
            number += add_by

            if is_prime(number):
                primes_encountered += 1
            else:
                none_primes += 1

        one_side += 1

    return ((one_side - 1) * 2) - 1


def q67():
    tree = Tree('data/p067_triangle.txt')
    maximum_path_sum = tree.find_maximum_path_sum()
    return maximum_path_sum


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    import time

    start_time = time.time()

    print(q58())

    time_taken = (time.time() - start_time) * 1000
    print('Done: this took {}ms\n'.format(time_taken))
