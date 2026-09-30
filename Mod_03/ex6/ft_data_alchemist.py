import random


def do_it() -> None:
    print("=== Game Data Alchemist ===\n")
    player_list = ["Player 1", "Player 2", "player 3", "Player 4",
                   "player 5", "player 6", "Player 7", "player 8",
                   "Player 9", "player 10"]
    print(f"Initial list of players: {player_list}\n")

    cap_list: list
    cap_list = [player.capitalize() for player in player_list]
    print(f"New list with all names capitalized: {cap_list}\n")

    only_cap: list
    only_cap = [player for player in player_list if player[0].isupper()]
    print(f"New list of capitalized names only: {only_cap}\n")

    names_dict: dict[str, int]
    names_dict = {player: random.randint(50, 700) for player in cap_list}
    print(f"Scores dict: {names_dict}\n")

    average = sum(names_dict.values()) / len(names_dict)
    print(f"Score average is {average:.2f}\n")

    high_scores = {
        player: value for player,
        value in names_dict.items() if value > average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    do_it()
