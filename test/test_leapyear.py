import pytest
from src.leapyear import isLeapYear


@pytest.mark.parametrize("year, expected", [(2020, True),
                                            (2000, True)])
def test_is_leap_year(year, expected):
    assert isLeapYear(year) == expected


@pytest.mark.parametrize("year, expected", [(2021, False),
                                             (1900, False),
                                             (1800, False),
                                             (1700, False)])
def test_is_not_leap_year(year, expected):
    assert isLeapYear(year) == expected


def test_is_not_leap_year_but_divisible_by_four():
    assert isLeapYear(1900) == False


@pytest.mark.parametrize("year, expected", [(2000, True),
                                            (1800, True)])
def test_leap_year_divisible_by_400(year, expected):
    assert isLeapYear(year) == expected



def test_leap_year_divisible_by_4_but_not_100():
    assert isLeapYear(1622) == True


# ekstra regel som eliminerer år delbare på 4000.
@pytest.mark.parametrize("year, expected", [(4000, False),
                                            (8000, False)])
def test_leap_year_divisible_by_4000(year, expected):
    assert isLeapYear(year) == expected