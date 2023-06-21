class Role:
    def __init__(self, name):
        self.name = name

class Mafia(Role):
    def __init__(self):
        super().__init__("Mafia")

    def perform_action(self):
        print("Mafia action: Choose a player to eliminate.")

class Detective(Role):
    def __init__(self):
        super().__init__("Detective")

    def perform_action(self):
        print("Detective action: Choose a player to investigate.")

class Doctor(Role):
    def __init__(self):
        super().__init__("Doctor")

    def perform_action(self):
        print("Doctor action: Choose a player to protect.")

class Townsfolk(Role):
    def __init__(self):
        super().__init__("Townsfolk")
