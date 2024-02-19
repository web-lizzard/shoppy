from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum
from typing import Union


class Currency(StrEnum):
    PLN = "PLN"
    USD = "USD"


@dataclass(frozen=True)
class Money:
    amount: int
    currency: Currency = Currency.PLN

    @classmethod
    def mint(
        cls, amount: float | Decimal, currency: Currency = Currency.PLN
    ) -> "Money":
        return Money(amount=int(amount * 100), currency=currency)

    def __str__(self) -> str:
        amount = self.amount / 100
        return f"{amount:.2f} {self.currency}"

    def __add__(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError(
                "Adding two money representation with different currency is not allowed!"
            )
        return self.__class__(amount=self.amount + other.amount, currency=self.currency)

    def __sub__(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError(
                "Subtracting two money representation with different currency is not allowed!"
            )
        return self.__class__(amount=self.amount - other.amount, currency=self.currency)

    def __mul__(self, other: int) -> "Money":
        return self.__class__(amount=self.amount * other)

    def __truediv__(self, other: int) -> "Money":
        return self.__class__(amount=int(self.amount / other))


@dataclass(frozen=True)
class Quantity:
    value: int

    def __post_init__(self):
        if self.value < 0:
            raise ValueError("Quantity cannot be negative")

    def __add__(self, other: "Quantity"):
        return self.__class__(self.value + other.value)

    def __sub__(self, other: "Quantity"):
        return self.__class__(self.value - other.value)

    def __mul__(self, other: int):
        return self.__class__(self.value * other)

    def __truediv__(self, other: int) -> "Quantity":
        return self.__class__(self.value // other)

    def __repr__(self):
        return f"Quantity({self.value})"

    def __eq__(self, quantity: object) -> bool:
        if isinstance(quantity, Quantity):
            return quantity.value == self.value
        if isinstance(quantity, int):
            return self.value == quantity

        raise TypeError("Not supported type")
