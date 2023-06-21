# File: game.py
import random
from player import Player
from roles import Mafia, Detective, Doctor, Townsfolk
from src.chatgpt_narrator import narrate


class Game:
    def __init__(self, player_names, scene):
        self.players = []
        self.scene = scene
        self.assign_roles(player_names)
        self.narrate_start()

    def assign_roles(self, player_names):
        roles = [Mafia(), Detective(), Doctor()] + [
            Townsfolk() for _ in range(len(player_names) - 3)
        ]
        random.shuffle(roles)
        for name, role in zip(player_names, roles):
            self.players.append(Player(name, role))

    def narrate_start(self):
        prompt = (
            f"[Narrator's Opening Monologue]\n\n"
            f"Narrator: Ladies and gentlemen, welcome to the thrilling game of Mafia. "
            f"In the small town of {self.scene}, danger lurks in the shadows, and trust is a scarce commodity. "
            f"Our {len(self.players)} players have gathered tonight to uncover the deceitful Mafia members among them. "
            f"But before we dive into the day phase, let's recap what happened during the night.\n\n"
        )
        print(narrate(prompt))

    def narrate_night_phase(self):
        prompt = (
            f"[Night Phase]\n\n"
            f"Narrator: All players, please close your eyes and drift off into the realm of dreams. "
            f"Mafia members, awaken silently and choose your next victim.\n\n"
            f"[Mafia makes their choice]\n\n"
            f"Narrator: The Mafia members have made their decision. Their choice is final. "
            f"Mafia, please go back to sleep. Detective, now it's your turn. Awaken and select a player to investigate.\n\n"
            f"[Detective makes their choice]\n\n"
            f"Narrator: The Detective has made their investigation. The truth will soon be revealed. "
            f"Detective, go back to sleep. And finally, the Doctor, it's your time to shine. "
            f"Awaken and select a player to protect.\n\n"
            f"[Doctor makes their choice]\n\n"
            f"Narrator: The Doctor has made their choice to protect a player. Doctor, go back to sleep.\n\n"
        )
        print(narrate(prompt))

    def narrate_day_phase(self):
        prompt = (
            f"[Day Phase]\n\n"
            f"Narrator: The sun rises over {self.scene}, and the townsfolk assemble in the town hall. "
            f"It's time for open discussion and debate. Remember, townsfolk, your task is to identify the Mafia members "
            f"hidden within your ranks. Use your words wisely and trust your instincts.\n\n"
        )
        print(narrate(prompt))

    def vote(self):
        votes = {}
        for player in self.players:
            if player.is_alive:
                print(
                    f"{player.name} ({player.role.name}), who do you want to vote off?"
                )
                voted_off = input()  # simulate user input
                votes[voted_off] = votes.get(voted_off, 0) + 1
        voted_off = max(votes, key=votes.get)
        for player in self.players:
            if player.name == voted_off:
                player.is_alive = False
                break
        prompt = f"{voted_off} was voted off during the day."
        print(narrate(prompt))

    def day(self):
        self.narrate_night_phase()
        self.narrate_day_phase()
        self.vote()
        self.print_state()

    def print_state(self):
        alive_players = [player.name for player in self.players if player.is_alive]
        print("Alive players are: " + ", ".join(alive_players))

    def play(self):
        while True:
            self.day()
            if self.check_end():
                break

    def check_end(self):
        mafia = [
            player
            for player in self.players
            if isinstance(player.role, Mafia) and player.is_alive
        ]
        townsfolk = [
            player
            for player in self.players
            if not isinstance(player.role, Mafia) and player.is_alive
        ]
        if len(mafia) == 0 or len(mafia) >= len(townsfolk):
            prompt = "The game has ended."
            print(narrate(prompt))
            return True
        return False
