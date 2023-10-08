from lib.poker.game_config import GameConfig
from lib.poker.poker_game import PokerGame
from lib.poker.player import Player
from lib.playing_cards.card import Card
from lib.playing_cards.enums import CardColor
from lib.playing_cards.enums import CardValue
from lib.poker.helper import cards_form_straight


def main():
    '''
    # create game
    config = GameConfig(1000, 2, 50)
    game = PokerGame(config)

    # add players
    for i in range(1, 5):
        player = Player(f"Player {i}")
        game.join_player(player)

    for player in game.player_manager.players:
        print(player)

    # start round
    print(game.card_manager.deck)
    game.start_round()
    print(game.card_manager.deck)

    for player in game.player_manager.players:
        print(player)
    '''

    player = Player("kek")
    player.cards = [
        Card(CardColor.CLUBS, CardValue.TWO),
        Card(CardColor.SPADES, CardValue.THREE)
    ]

    community_cards = [
        Card(CardColor.CLUBS, CardValue.KING),
        Card(CardColor.CLUBS, CardValue.FIVE),
        Card(CardColor.CLUBS, CardValue.SIX),
        Card(CardColor.HEARTS, CardValue.ACE),
        Card(CardColor.DIAMONDS, CardValue.ACE),
    ]

    print(cards_form_straight(community_cards + player.cards).value)


if __name__ == "__main__":
    main()
