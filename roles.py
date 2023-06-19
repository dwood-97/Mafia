class Role:
    def __init__(self, name):
        self.name = name


class Mafia(Role):
    def __init__(self):
        super().__init__("Mafia")


class Detective(Role):
    def __init__(self):
        super().__init__("Detective")


class Doctor(Role):
    def __init__(self):
        super().__init__("Doctor")


class Townsfolk(Role):
    def __init__(self):
        super().__init__("Townsfolk")
