from game import Game


def main():
    player_names = [
        "Sophia",
        "Ethan",
        "Olivia",
        "Liam",
        "Ava",
        "Noah",
        "Isabella",
        "Mason",
        "Mia",
        "James",
    ]
    scene = "a quiet little town in the 19th century"
    game = Game(player_names, scene)
    game.play()


if __name__ == "__main__":
    main()
