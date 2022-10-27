from function import isLeapYear


def test_if_divisible_by_4_but_not_by_100_is_leap_year():
    assert isLeapYear(1944)


def test_if_divisible_by_400_is_leap_year():
    assert isLeapYear(2000)


def test_if_not_divisible_by_4_not_leap_year():
    assert not isLeapYear(1993)


def test_if_divisible_by_100_but_not_400_is_leap_year():
    assert not isLeapYear(1900)

#Change to upload