import pytest
from exercises.oo import RationalNumber as RN


@pytest.mark.skip('Not implemented yet.')
def test_rational_number_denominator_zero():
    with pytest.raises(ValueError):
        r = RN(7, 0)
        r = RN(11, 0)


@pytest.mark.skip('Not implemented yet.')
def test_rational_number_reduce():
    assert RN._reduce(12, 6).__str__() == '2/1'
    assert RN._reduce(3, 12).__str__() == '1/4'


@pytest.mark.skip('Not implemented yet.')
def test_rational_number_equal():
    a = RN(4, 3)
    b = RN(4, 3)
    c = RN(5, 3)
    assert a == b
    assert b == a
    assert not a == c
    assert not c == a
    assert not b == c
    assert not c == b


@pytest.mark.skip('Not implemented yet.')
def test_rational_number_addition():
    a = RN(4, 3)
    b = RN(8, 3)
    c = RN(12, 3)
    assert a + b == c

    d = RN(3, 4)
    e = RN(3, 5)
    f = RN(27, 20)
    assert d + e == f


@pytest.mark.skip('Not implemented yet.')
def test_rational_number_subtraction():
    a = RN(5, 4)
    b = RN(4, 4)
    c = RN(1, 4)
    assert a - b == c

    d = RN(5, 4)
    e = RN(4, 5)
    f = RN(9, 20)
    assert d - e == f


@pytest.mark.skip('Not implemented yet.')
def test_rational_number_multiplication():
    a = RN(3, 5)
    b = RN(7, 5)
    c = RN(21, 25)
    assert a * b == c

    d = RN(4, 5)
    e = RN(5, 4)
    f = RN(1, 1)
    assert d * e == f


@pytest.mark.skip('Not implemented yet.')
def test_rational_number_division():
    a = RN(3, 5)
    b = RN(6, 5)
    c = RN(1, 2)
    assert a / b == c

    d = RN(3, 7)
    e = RN(8, 5)
    f = RN(15, 56)
    assert d / e == f
