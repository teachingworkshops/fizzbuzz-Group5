import pytest
import G5_FizzBuzz as fb

@pytest.mark.parametrize("a,b,expected",
                            [(-1, 1, False),
                            (-1, -1, False),
                            (0, 0, False),
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
                            (11, 11, True),
                            (28, 28, True)])

def test_fizzbuzz(a, b, expected):
    assert fb.checkFizzBuzz(a, b) == expected