from dataclasses import dataclass

@dataclass(frozen=True)
class Money:
    amount: int 
    currency: str = 'PLN'

    