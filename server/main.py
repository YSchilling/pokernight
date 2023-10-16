from lib.poker.game_config import GameConfig
from lib.poker.poker_game import PokerGame
from lib.poker.player import Player
from lib.playing_cards.card import Card
from lib.playing_cards.enums import CardColor
from lib.playing_cards.enums import CardValue
from lib.poker.helper import calculate_player_best_hand


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
        Card(CardColor.HEARTS, CardValue.TWO),
        Card(CardColor.HEARTS, CardValue.THREE)
    ]

    community_cards = [
        Card(CardColor.CLUBS, CardValue.NINE),
        Card(CardColor.HEARTS, CardValue.SIX),
        Card(CardColor.HEARTS, CardValue.KING),
        Card(CardColor.CLUBS, CardValue.ACE),
        Card(CardColor.CLUBS, CardValue.TEN),
    ]

    print(calculate_player_best_hand(player, community_cards))


if __name__ == "__main__":
    main()
