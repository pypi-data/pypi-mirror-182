from __future__ import annotations

from uuid import uuid4
from typing import NamedTuple


class LotteryTicket(NamedTuple):
    """
    This is an individual lottery ticket
    """
    number: str

    @classmethod
    def create_lottery_ticket(cls):
        return cls(str(uuid4()))


class Person(NamedTuple):
    """
    This is a person and represents an individual player in our game
    """
    name: str
    age: int
    money: int
    lottery_tickets: list[LotteryTicket]

    @classmethod
    def create_person(cls, name, age, money, lottery_tickets: list[LotteryTicket] | None = None) -> Person:
        lottery_tickets = lottery_tickets if lottery_tickets is not None else []
        return cls(name, age, money, lottery_tickets)

    def has_winning_lottery_ticket(self, lottery_ticket: LotteryTicket) -> bool:
        return lottery_ticket in self.lottery_tickets

