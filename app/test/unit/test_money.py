import pytest
from domain.value_objects.money import Currency, Money


def test_money_to_string():
    m = Money(amount=1050)

    assert str(m) == "10.50 PLN"


def test_money_adding():
    m1 = Money(amount=100)
    m2 = Money(amount=100)

    m3 = m1 + m2

    assert m3.amount == 200


def test_money_subtracting():
    m1 = Money(amount=100)
    m2 = Money(amount=50)

    m3 = m1 - m2

    assert m3.amount == 50


def test_money_multiplying_by_int():
    m1 = Money(amount=100)

    m2 = m1 * 2

    assert m2.amount == 200


def test_money_dividing_by_int():
    m1 = Money(amount=200)

    m2 = m1 / 2

    assert m2.amount == 100


def test_adding_with_different_currency_raise_exception():
    m1 = Money(amount=2000, currency=Currency.PLN)
    m2 = Money(amount=200, currency=Currency.USD)

    with pytest.raises(ValueError) as e:
        m3 = m1 + m2

        assert (
            str(e)
            == "Adding two money representation with different currency is not allowed!"
        )


def test_subtracting_with_different_currency_raise_exception():
    m1 = Money(amount=2000, currency=Currency.PLN)
    m2 = Money(amount=200, currency=Currency.USD)

    with pytest.raises(ValueError) as e:
        m3 = m1 - m2

        assert str(
            "Subtracting two money representation with different currency is not allowed!"
        )


def test_mint_converting_money_from_float_correctly():
    m = Money.mint(amount=200)

    assert m.amount == 20000
