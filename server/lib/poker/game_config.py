class GameConfig:
    def __init__(self, player_starting_money: int, blind_increase_rate: int, starting_blind_value: int):
        self.player_starting_money = player_starting_money
        self.blind_increase_rate = blind_increase_rate
        self.starting_blind_value = starting_blind_value