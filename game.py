import random
from player import Player
from roles import Mafia, Detective, Doctor, Townsfolk

class Game:
    def __init__(self, player_names):
        self.players = []
        self.assign_roles(player_names)

    def assign_roles(self, player_names):
        roles = [Mafia(), Detective(), Doctor()] + [Townsfolk() for _ in range(len(player_names) - 3)]
        random.shuffle(roles)

        for name, role in zip(player_names, roles):
            self.players.append(Player(name, role))

    def vote(self):
        while True:
            for player in self.players:
                if player.is_alive:
                    print(f"{player.name} ({player.role.name}), who do you want to vote off?")
                    # Here we would have the voting logic based on player input

    def day(self):
        self.vote()
        # Here we would have additional logic for mafia, detective, and doctor actions

    def play(self):
        while True:
            self.day()
            # Here we would check win conditions and potentially end the game
