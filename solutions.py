import logging
import sys

from euler.even_fibonacci import N2FibonacciIterator
from euler.largest_prime_factor import largest_prime_factor
from euler.largest_product_in_a_grid import largest_product_in_a_grid
from euler.largest_product_in_a_series import adjacent_multiplicand
from euler.largest_sum import first_n_digits_of_sum
from euler.lattice_paths import lattice_paths
from euler.lexographical_permutations import lexilogical_ordering
from euler.maximum_path_sum import Tree
from euler.multiples_of_3_and_5s import use_mathematical_simplification
from euler.name_scores import calculate_score
from euler.power_digit_sum import power_digit_sum
from euler.reciprocal_cycles import string_division
from euler.smallest_multiple import smallest_multiple_up_to
from euler.sum_square_difference import sum_square_difference
from euler.util import prime
from euler.util.fibonacci import FibonacciIterator


def q1():
    return use_mathematical_simplification(999)


def q2():
    upper_bound = 4000000

    #
    fib_generator = FibonacciIterator()
    fib_generator.set_upper_bound(upper_bound)

    #
    fib_generator = N2FibonacciIterator()
    fib_generator.set_upper_bound(upper_bound)
    return sum(fib_generator.sequence)


def q3():
    # Q3 :: Largest Prime Factor of 600851475143
    return largest_prime_factor(600851475143)


def q5():
    return smallest_multiple_up_to(20)


def q6():
    # Q6 :: Sum Square Difference
    return sum_square_difference(100)


def q7():
    return prime.nth_prime_number(10001)


def q8():
    """ Adjacent Multiplicand"""
    return adjacent_multiplicand(
        string='73167176531330624919225119674426574742355349194934969835203127'
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


def q11():
    return largest_product_in_a_grid(
        grid=['08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08',
            '49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00',
            '81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65',
            '52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91',
            '22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80',
            '24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50',
            '32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70',
            '67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21',
            '24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72',
            '21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95',
            '78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92',
            '16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57',
            '86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58',
            '19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40',
            '04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66',
            '88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69',
            '04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36',
            '20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16',
            '20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54',
            '01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48', ],
        window_size=4,
    )


def q13():
    with open('data/p013_numbers.txt') as numbers_file:
        numbers = [
            number.replace('\n', '')
            for number in numbers_file.readlines()
        ]
        logging.debug(len(numbers))

        return first_n_digits_of_sum(10, numbers)


def q15():
    return lattice_paths(20)


def q16():
    """ Q16 :: Digit of 2^1000"""
    return power_digit_sum(1000)


def q18():
    tree = Tree('data/p018_tree.txt')
    maximum_path_sum = tree.find_maximum_path_sum()
    return maximum_path_sum


def q20():
    import math
    return sum(map(int, str(math.factorial(100))))


def q22():
    with open('data/p022_names.txt', 'r') as file:
        names_text = file.readlines()[0]

        names = names_text.replace('"', '').split(',')
        names.sort()

        name_scores = map(calculate_score, names)
        cumulative = sum(map(lambda x: x[0] * x[1], enumerate(name_scores, 1)))

    return cumulative


def q24():
    nth = 1000000
    zero_to = 9

    return lexilogical_ordering(nth, zero_to)


def q26():
    """ Q26 :: Reciprocal cycles [https://projecteuler.net/problem=26]

    Find value of d for which 1/d contains the longest recurring cycle
        in its decimal fraction part"""
    calculated = map(string_division, range(2, 1000 + 1))
    n, _ = max(enumerate(calculated, 2), key=lambda x: x[1])
    return n


def q48():
    return str(sum(map(lambda x: x ** x, range(1, 1000))))[-10:]


def q67():
    tree = Tree('data/p067_triangle.txt')
    maximum_path_sum = tree.find_maximum_path_sum()
    return maximum_path_sum


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    print(q13())
    # assert q22() == 871198282
    # assert q26() == 26
