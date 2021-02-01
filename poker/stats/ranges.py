from dataclasses import dataclass

from poker.model import card


@dataclass
class HandType:
    top: card.Values
    bottom: card.Values
    suited: bool

    def __hash__(self):
        return hash((self.top, self.bottom, self.suited))

    def __eq__(self, other):
        if not isinstance(other, HandType):
            raise ValueError(
                "== is not defined beteween {self.__class} and {other.__class__}"
            )
        return (
            (self.top == other.top)
            and (self.bottom == other.bottom)
            and (self.suited == other.suited)
        )

    def __str__(self):

        top_str = card.VALUE_TO_STRING_MAPPING[self.top]
        bottom_str = card.VALUE_TO_STRING_MAPPING[self.bottom]

        if self.top == self.bottom:
            suited = ""
        else:
            suited = "s" if self.suited else "o"

        return f"{top_str}-{bottom_str}{suited}"


def get_game_range(game):

    hand_ranges = {}

    for hand in game.hands:
        if hand.our_cards is not None:
            hand_type = get_hand_type(hand.our_cards)
            if hand_type not in hand_ranges:
                hand_ranges[hand_type] = 1
            else:
                hand_ranges[hand_type] += 1

    return hand_ranges


def get_hand_type(cards):

    if len(cards) != 2:
        raise ValueError("Hands can only have two cards in texas holdem")

    cards = sorted(cards, reverse=True)

    return HandType(
        top=cards[0].value, bottom=cards[1].value, suited=cards[0].suit == cards[1].suit
    )
