from .controllers import Lotto
from .models import Person
from .views import display_winner, display_winner_as_json


def main(display_type: str):
    lotto = Lotto("Oregon State Lotto", 5)

    per_1 = Person.create_person("David", 42, 100)
    per_2 = Person.create_person("Sherryl", 55, 1_000)

    lotto.sell_lottery_tickets(per_1, 3)
    lotto.sell_lottery_tickets(per_2, 5)

    winner = lotto.find_winner([per_1, per_2])

    view_func = display_winner if display_type == "txt" else display_winner_as_json

    view_func(winner, lotto.winning_ticket)


if __name__ == '__main__':
    main("txt")
