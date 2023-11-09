from ..playing_cards.card import Card
from ..playing_cards.enums import CardValue
from ..playing_cards.enums import CardColor
from .player import Player

import enum


class PokerHandCategory(enum.Enum):
    ROYAL_FLUSH = 0  # same worth
    STRAIGHT_FLUSH = 1  # highcard
    FOUR_OF_A_KIND = 2  # quadruplet -> kicker
    FULL_HOUSE = 3  # triplet -> pair
    FLUSH = 4  # highcards until 5
    STRAIGHT = 5  # highcard
    THREE_OF_A_KIND = 6  # triplet -> kicker -> kicker
    TWO_PAIR = 7  # pair -> pair -> kicker
    PAIR = 8  # pair -> kicker -> kicker -> kicker
    HIGH_CARD = 9  # highcard -> highcard -> highcard -> highcard -> highcard


class PokerHand:
    def __init__(self, player_cards: list[Card], community_cards: list[Card]) -> None:
        self.cards = player_cards + community_cards
        (category, ranking_cards) = HandAnalyzer().analyze_hand(self.cards)
        self.category: PokerHandCategory = category
        self.ranking_cards = ranking_cards

    # ---------- COMPARE TO OTHER HANDS ----------

    def __eq__(self, other):
        if self.category.value != other.category.value:
            return False

        if self.category == PokerHandCategory.ROYAL_FLUSH:
            return True

        self_values = [card.value.value for card in self.ranking_cards]
        other_values = [card.value.value for card in other.ranking_cards]

        return self_values == other_values

    def __lt__(self, other):
        if self.category.value != other.category.value:
            return self.category.value > other.category.value

        if self.category == PokerHandCategory.ROYAL_FLUSH:
            return False

        for i in range(len(self.ranking_cards)):
            self_card = self.ranking_cards[i]
            other_card = other.ranking_cards[i]
            if self_card.value.value == other_card.value.value:
                continue
            elif self_card.value.value < other_card.value.value:
                return True
            else:
                return False

        else:
            return False


class HandAnalyzer:
    def analyze_hand(self, cards: list[Card]) -> tuple[PokerHandCategory, list[Card] | None]:

        result, category, ranking = self._check_straight_flush(cards.copy())
        if result:
            return (category, ranking)

        result, ranking = self._check_four_of_a_kind(cards.copy())
        if result:
            return (PokerHandCategory.FOUR_OF_A_KIND, ranking)

        result, ranking = self._check_full_house(cards.copy())
        if result:
            return (PokerHandCategory.FULL_HOUSE, ranking)

        result, ranking = self._check_flush(cards.copy())
        if result:
            return (PokerHandCategory.FLUSH, ranking)

        result, ranking = self._check_straight(cards.copy())
        if result:
            return (PokerHandCategory.STRAIGHT, ranking)

        result, ranking = self._check_three_of_a_kind(cards.copy())
        if result:
            return (PokerHandCategory.THREE_OF_A_KIND, ranking)

        result, ranking = self._check_two_pair(cards.copy())
        if result:
            return (PokerHandCategory.TWO_PAIR, ranking)

        result, ranking = self._check_pair(cards.copy())
        if result:
            return (PokerHandCategory.PAIR, ranking)

        ranking = self._check_high_cards(cards.copy())
        return (PokerHandCategory.HIGH_CARD, ranking)

    def _check_straight_flush(self, cards: list[Card]) -> tuple[bool, PokerHandCategory | None, list[Card] | None]:
        flush_result, flush = self._cards_form_flush(cards)
        if flush_result:
            straight_result, straight = self._cards_form_straight(flush)
            if straight_result:
                high_card = straight[0]
                if high_card.value == CardValue.ACE:
                    return (True, PokerHandCategory.ROYAL_FLUSH, None)
                else:
                    return (True, PokerHandCategory.STRAIGHT_FLUSH, [high_card])

        return (False, None, None)

    def _check_four_of_a_kind(self, cards: list[Card]) -> tuple[bool, list[Card]]:
        multiple_result = self._categorize_multiple(cards)
        biggest_multiple = multiple_result[0]
        if len(biggest_multiple) == 4:
            four_kind_card = biggest_multiple[0]
            cards_without_four_kind_card = [
                card for card in cards if card.value != four_kind_card.value]
            kicker = sorted(cards_without_four_kind_card,
                            key=lambda card: card.value.value, reverse=True)[0]
            return (True, [four_kind_card, kicker])

        return (False, None)

    def _check_full_house(self, cards: list[Card]) -> (bool, list[Card]):
        multiple_result = self._categorize_multiple(cards)
        biggest_multiple = multiple_result[0]
        second_biggest_multiple = multiple_result[1]
        if len(biggest_multiple) == 3 and len(second_biggest_multiple) >= 2:
            return (True, [biggest_multiple[0], second_biggest_multiple[0]])

        return (False, None)

    def _check_flush(self, cards: list[Card]) -> (bool, list[Card]):
        flush_result, flush_cards = self._cards_form_flush(cards)
        if not flush_result:
            return (False, None)

        flush_high = sorted(
            flush_cards, key=lambda card: card.value.value, reverse=True)[:5]
        return (True, flush_high)

    def _check_straight(self, cards: list[Card]) -> (bool, list[Card]):
        straight_result, straight = self._cards_form_straight(cards)
        if straight_result:
            high_card = straight[0]
            return (True, [high_card])

        return (False, None)

    def _check_three_of_a_kind(self, cards: list[Card]) -> (bool, list[Card]):
        multiple_result = self._categorize_multiple(cards)
        biggest_multiple = multiple_result[0]
        if len(biggest_multiple) == 3:
            tripplet_card = biggest_multiple[0]
            cards_without_tripplet_card = sorted([
                card for card in cards if card.value != tripplet_card.value], key=lambda card: card.value.value, reverse=True)
            kicker = cards_without_tripplet_card[0]
            second_kicker = cards_without_tripplet_card[1]
            return (True, [tripplet_card, kicker, second_kicker])

        return (False, None)

    def _check_two_pair(self, cards: list[Card]) -> (bool, list[Card]):
        multiple_result = self._categorize_multiple(cards)
        biggest_multiple = multiple_result[0]
        second_biggest_multiple = multiple_result[1]
        if len(biggest_multiple) == 2 and len(second_biggest_multiple) == 2:
            sorted_pairs = sorted(
                (biggest_multiple + second_biggest_multiple), key=lambda card: card.value.value, reverse=True)
            high_pair_card = sorted_pairs[0]
            low_pair_card = sorted_pairs[2]
            cards_without_pairs = sorted([
                card for card in cards if card.value != high_pair_card.value and card.value != low_pair_card.value], key=lambda card: card.value.value, reverse=True)
            kicker = cards_without_pairs[0]
            return (True, [high_pair_card, low_pair_card, kicker])

        return (False, None)

    def _check_pair(self, cards: list[Card]) -> (bool, list[Card]):
        multiple_result = self._categorize_multiple(cards)
        biggest_multiple = multiple_result[0]
        if len(biggest_multiple) == 2:
            pair_card = biggest_multiple[0]
            cards_without_pair = sorted([
                card for card in cards if card.value != pair_card.value], key=lambda card: card.value.value, reverse=True)
            return (True, [pair_card] + cards_without_pair[:3])

        return (False, None)

    def _check_high_cards(self, cards: list[Card]) -> list[Card]:
        cards.sort(key=lambda card: card.value.value, reverse=True)
        return cards[:5]

    def _categorize_multiple(self, cards: list[Card]) -> list[list[Card]]:
        values = [[] for _ in range(13)]

        for card in cards:
            index = card.value.value - 2
            values[index].append(card)

        values.sort(key=lambda x: len(x), reverse=True)

        return [x for x in values if x != []]

    def _cards_form_flush(self, cards: list[Card]) -> (bool, list[Card]):
        colors = [[], [], [], []]

        for card in cards:
            colors[card.color.value-1].append(card)

        max_color = max(colors, key=lambda x: len(x))

        if len(max_color) < 5:
            return (False, None)

        return (True, max_color)

    def _cards_form_straight(self, cards: list[Card]) -> (bool, list[Card]):
        cards.sort(key=lambda card: card.value.value, reverse=True)
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


def calculate_winner(players: list[Player], community_cards: list[Card]) -> list[Player]:
    # categorize hands
    hands = [(player, PokerHand(player.cards, community_cards))
             for player in players]

    # select best hand
    winner = [hands[0]]
    for hand in hands[1:]:
        if hand[1] == winner[0][1]:
            winner.append(hand)
        elif winner[0][1] < hand[1]:
            winner.clear()
            winner.append(hand)

    return [player for (player, _) in winner]
