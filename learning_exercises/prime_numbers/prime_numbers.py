"""Create a Python script to calculate prime numbers.

Exercise 1: calculate the first 10 prime numbers (excluding 0 and 1)

Exercise 2: calculate the prime number closest to 200.

Exercise 3: calculate the first 5 digit prime number.

Exercise 4: calculate the first n prime numbers

"""
import math
from typing import Union, List


def get_prime_number(end: int = 10_000, amount: int = None, digits: int = None) -> Union[int, List]:
    """Calculate prime number(s)

    Args:
        end(optional): get all prime numbers till this number
        amount(optional): get this amount of prime numbers
        digits(optional): get the first prime number with this amount of digits

    Returns:
        int: if digits is given it will return the first number with the amount of digits given.
        list: of prime numbers till the end or amount was reached.
        None: if either digits was given and never reached or given range has no prime number.
    """
    def _get_prime_numbers(numbers):
        for number in numbers:
            if number not in numbers:
                continue
            numbers = [n for n in numbers if n % number != 0 or n == number]
            if amount and numbers.index(number) == amount:
                number_index = numbers.index(number)
                return numbers[:number_index]
            if digits:
                if len(str(number)) == digits:
                    return number
        if amount or digits:
            numbers.extend(list(range(numbers[-1], numbers[-1]+500)))
            return _get_prime_numbers(numbers)
        return numbers

    return _get_prime_numbers(list(range(2, end)))


def get_closest_number(number: int, number_list: list) -> int:
    """Get the closest number from a list to the given number

    Note:
        if more than one number inside the list has the same difference to the given number the first one found will
        be returned.

    Args:
        number: wanted number or closest to it
        number_list: list of numbers to search from

    Returns:
        int: the number from the list which has the smallest difference to given number
    """
    numbers = [int(abs(n - number)) for n in number_list]
    closest = min(numbers)
    closest_index = numbers.index(closest)
    return number_list[closest_index]


if __name__ == '__main__':
    # Exercise 1:
    first_ten_primes = get_prime_number(amount=10)
    print(f"Exercise 1: the first 10 prime numbers are: {first_ten_primes}")

    # Exercise 2:
    primes_near_200 = get_prime_number(end=210)
    closest_prime_to_200 = get_closest_number(200, primes_near_200)
    print(f"Exercise 2: the prime number closest to 200 is: {closest_prime_to_200}")

    # Exercise 3:
    first_5_digit_prime = get_prime_number(digits=5)
    print(f"Exercise 3: the first prime number with 5 digits is: {first_5_digit_prime}")

    # Exercise 4:
    # The amount of the following call is variable so whatever you chose it will calculate the first 'n' prime numbers
    first_100_primes = get_prime_number(amount=100)
    print(f"Exercise 4: the first n (e.g. n = 100) prime numbers are: {first_100_primes}")
