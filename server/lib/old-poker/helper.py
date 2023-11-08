from ..playing_cards.card import Card
from ..playing_cards.enums import CardValue
from ..playing_cards.enums import CardColor
from .player import Player

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
    flush_result, flush = cards_form_flush(cards)
    if flush_result:
        straight_result, straight = cards_form_straight(flush)
        if straight_result:
            high_card = straight[0]
            if Card(None, CardValue.ACE).eq_value(high_card):
                return PokerHand.ROYAL_FLUSH
            else:
                return PokerHand.STRAIGHT_FLUSH

    # check royal flush
    multiple_result = categorize_multiple(cards)
    biggest_multiple = multiple_result[0]
    second_biggest_multiple = multiple_result[1]
    if len(biggest_multiple) == 4:
        return PokerHand.FOUR_OF_A_KIND
    if len(biggest_multiple) == 3 and len(second_biggest_multiple) >= 2:
        return PokerHand.FULL_HOUSE

    if flush_result:
        return PokerHand.FLUSH

    straight_result, straight = cards_form_straight(cards)
    if straight_result:
        return PokerHand.STRAIGHT

    if len(biggest_multiple) == 3:
        return PokerHand.THREE_OF_A_KIND

    if len(biggest_multiple) == 2 and len(second_biggest_multiple) == 2:
        return PokerHand.TWO_PAIR

    if len(biggest_multiple) == 2:
        return PokerHand.PAIR

    return PokerHand.HIGH_CARD


def categorize_multiple(cards: list[Card]) -> list[Card]:
    values = [[] for _ in range(13)]

    for card in cards:
        index = card.value.value - 2
        values[index].append(card)

    values.sort(key=lambda x: len(x), reverse=True)

    return [x for x in values if x != []]


def cards_form_flush(cards: list[Card]) -> (bool, list[Card]):
    colors = [[], [], [], []]

    for card in cards:
        colors[card.color.value-1].append(card)

    max_color = max(colors, key=lambda x: len(x))

    if len(max_color) < 5:
        return (False, None)

    return (True, max_color)


def cards_form_straight(cards: list[Card]) -> (bool, list[Card]):
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

        if len(straight) == 5:
            break

        last_card_value = straight[-1].value.value
        this_card_value = card.value.value

        if this_card_value + 1 == last_card_value:
            straight.append(card)
            continue

        straight.clear()
        straight.append(card)

    if len(straight) < 5:
        return (False, None)

    return (True, straight[:5])
