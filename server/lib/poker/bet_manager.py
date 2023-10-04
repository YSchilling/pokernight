from .game_config import GameConfig

class BetManager:
    def __init__(self, config: GameConfig) -> None:
        self.small_blind_value = config.starting_blind_value
        self.small_blind_pos = 1
        self.big_blind_pos = 2