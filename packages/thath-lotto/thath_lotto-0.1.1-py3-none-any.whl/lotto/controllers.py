from __future__ import annotations

from random import choice
from dataclasses import dataclass, field

from .models import LotteryTicket, Person


@dataclass
class Lotto:
    """
    This represents the lottery  in our application and holds most of the
    business logic
    """
    name: str
    ticket_price: int
    lottery_tickets_sold: list[LotteryTicket] = field(default_factory=list)
    winning_ticket: LotteryTicket | None = None

    def sell_lottery_tickets(self, person: Person, amount: int) -> None:
        if (amount * self.ticket_price) > person.money:
            raise ValueError("Not enough money for amount of lottery requested")

        new_lottery_tickets = [LotteryTicket.create_lottery_ticket() for _ in range(amount)]

        self.lottery_tickets_sold.extend(new_lottery_tickets)
        person.lottery_tickets.extend(new_lottery_tickets)

    def _get_winning_lottery_ticket(self) -> LotteryTicket:
        if self.winning_ticket is None:
            self.winning_ticket = choice(self.lottery_tickets_sold)
        return self.winning_ticket

    def find_winner(self, players: list[Person]) -> Person | None:
        """
        Finds the lottery winner provided a list of players
        """
        winning_ticket = self._get_winning_lottery_ticket()

        for player in players:
            if player.has_winning_lottery_ticket(winning_ticket):
                return player
