N_PLAYERS = 3


def main():
    _players = greet_players()


def greet_players() -> tuple[str, ...]:
    print("---------------------------")
    print("    ROCK-PAPER-SCISSORS")
    print("---------------------------")
    print()

    players = []
    for i in range(1, N_PLAYERS + 1):
        player = input(f"Hello player {i}, what is your name? ")
        players.append(player)

    return tuple(players)


if __name__ == "__main__":
    main()
