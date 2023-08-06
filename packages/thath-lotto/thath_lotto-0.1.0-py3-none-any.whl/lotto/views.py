from __future__ import annotations

import json

from .models import Person, LotteryTicket


def display_winner(winner: Person, winning_ticket: LotteryTicket) -> None:
    """
    Displays the winner player
    """
    print(f"The winner of this lottery is {winner.name}")
    print(f"This was their winning ticket: {winning_ticket.number}")


def display_winner_as_json(winner: Person, winning_ticket: LotteryTicket) -> None:
    """
    Displays the winner player
    """
    print(json.dumps({
        "winner": winner.name,
        "winning_ticket": winning_ticket.number
    }))
