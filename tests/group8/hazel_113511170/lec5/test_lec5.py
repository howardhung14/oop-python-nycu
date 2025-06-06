#########################
## EXAMPLE: returning a tuple
#########################
import lec5
import pytest
import add_path


# please write a test for quotient_and_remainder function
def test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(20, 6) == (3, 2)
    assert lec5.quotient_and_remainder(20, 7) == (2, 6)
    assert lec5.quotient_and_remainder(20, 8) == (2, 4)
    assert lec5.quotient_and_remainder(20, 9) == (2, 2)
    assert lec5.quotient_and_remainder(20, 10) == (2, 0)
    assert lec5.quotient_and_remainder(20, 11) == (1, 9)

    try:
        lec5.quotient_and_remainder(20, 0)
    except ZeroDivisionError:
         print("ZeroDivisionError")
    assert lec5.quotient_and_remainder(20, 11) == (1, 9)


def test_sum_elem_method1():
    assert lec5.sum_elem_method1([1, 2, 3, 4]) == 10
    assert lec5.sum_elem_method1([-1, -2, -3, -4]) == -10
    assert lec5.sum_elem_method1([13, 34, 0, 88, 88, 0, 9]) == 232
    assert lec5.sum_elem_method1([5]) == 5
    assert lec5.sum_elem_method1([]) == 0


def test_sum_elem_method2():
    assert lec5.sum_elem_method2([1, 2, 3, 4]) == 10
    assert lec5.sum_elem_method2([-1, -2, -3, -4]) == -10
    assert lec5.sum_elem_method2([13, 34, 0, 88, 88, 0, 9]) == 232
    assert lec5.sum_elem_method2([5]) == 5
    assert lec5.sum_elem_method2([]) == 0

def new_test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(24, 6) == (4, 0)
    assert lec5.quotient_and_remainder(25, 7) == (3, 4)
    assert lec5.quotient_and_remainder(12, 8) == (1, 4)
    assert lec5.quotient_and_remainder(30, 9) == (3, 3)
    assert lec5.quotient_and_remainder(19, 10) == (1, 9)

    try:
        lec5.quotient_and_remainder(11, 0)
    except ZeroDivisionError:
         print("ZeroDivisionError")
    assert lec5.quotient_and_remainder(23, 13) == (1, 10)