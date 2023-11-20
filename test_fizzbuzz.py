import pytest
import G5_FizzBuzz as fb

@pytest.mark.parametrize("a,b,expected",
                            [(-1, 1, False),
                            (-1, -1, False),
                            (0, 0, False),
                            (00, 0, False),
                            (0.0, 0, False),
                            ("a", 1, False),
                            ("a b", 1, False),
                            (1, 3, False),
                            ("Fizz", 3, True),
                            ("Buzz", 5, True),
                            ("FizzBuzz", 15, True),
                            ("fizz", 3, True),
                            ("buzz", 5, True),
                            ("fizzBuzz", 15, True),
                            ("FIzz", 3, True),
                            ("BuZz", 5, True),
                            ("Fizzbuzz", 15, True),
                            ("Fizz Buzz", 15, True),
                            (1, 1, True),
                            (2, 2, True),
                            (28, 28, True),
                            (-99, 1, False),
                            (-1, 1, False),
                            (4, 4, True),
                            (7, 7, True),
                            ("Fizz", 9, True),
                            ("Buzz", 10, True),
                            (11, 11, True),
                            (14, 14, True),
                            (16, 16, True),
                            (29, 29, True),
                            ("fizz buzz", 30, True)])


def test_fizzbuzz(a, b, expected):
    assert fb.checkFizzBuzz(a, b) == expected