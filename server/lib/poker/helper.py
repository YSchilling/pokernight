from ..playing_cards.card import Card
from ..playing_cards.enums import CardValue
from ..playing_cards.enums import CardColor
from .player import Player

import collections
import enum


class PokerHand(enum.Enum):
    ROYAL_FLUSH = 0
    STRAIGHT_FLUSH = 1
    FOUR_OF_A_KIND = 2
    FULL_HOUSE = 3
    FLUSH = 4
    STRAIGHT = 5
    THREE_OF_A_KIND = 6
    TWO_PAIR = 7
    PAIR = 8
    HIGH_CARD = 9


def calculate_winner(players: list[list[Player]], community_cards: list[Card]):
    for player in players:
        calculate_player_best_hand(player, community_cards)

    # select best hand


def calculate_player_best_hand(player: Player, community_cards: list[Card]):
    cards = player.cards + community_cards

    # check color
    color_counter = collections.Counter([card.color for card in cards])
    # check kind
    kind_counter = collections.Counter([card.value for card in cards])
    # check straight
    # check if ace in cards


def cards_form_straight(cards: list[Card]) -> (bool, Card):
    cards.sort(key=lambda x: x.value.value, reverse=True)
    for card in cards:
        if card.value == CardValue.ACE:
            cards.append(Card(CardColor.SPADES, CardValue.LOW_ACE))
            break

    straight: list[Card] = []

    for card in cards:
        if len(straight) == 0:
            straight.append(card)
            continue

        last_card_value = straight[-1].value.value
        this_card_value = card.value.value

        if this_card_value + 1 == last_card_value:
            straight.append(card)
            continue

        straight.clear()
        straight.append(card)

    if len(straight) < 5:
        return (False, None)

    return (True, straight[0])
