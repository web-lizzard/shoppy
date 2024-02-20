from dataclasses import dataclass


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
