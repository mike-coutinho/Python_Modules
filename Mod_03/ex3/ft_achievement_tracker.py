import random


class Player:
    def __init__(self, name: str, achiev: set):
        self.name = name
        self.a = achiev


def gen_player_achievements() -> None:
    achiev: list = ['Crafting Genius', 'Strategist', 'World Savior',
                    'Speed Runner', 'Survivor',
                    'Master Explorer', 'Treasure Hunter',
                    'Unstoppable', 'First Steps', 'Collector Supreme',
                    'Sharp Mind', 'Boss Slayer']

    achieve_set: set = set(achiev)
    alice = Player("Alice", set(random.sample(achiev, 5)))
    bob = Player("Bob", set(random.sample(achiev, 3)))
    charlie = Player("Charlie", set(random.sample(achiev, 4)))
    dylan = Player("Dylan", set(random.sample(achiev, 6)))

    players = [alice, bob, charlie, dylan]
    for player in players:
        print(f"Player {player.name}: {player.a}")

    print()
    print(f"All distinct achievements: {achieve_set}")
    print()
    common_achievements = bob.a.intersection(alice.a,
                                             charlie.a, dylan.a)
    print(f"Common achievements: {common_achievements}")
    print()
    res = alice.a.difference(bob.a.union(charlie.a, dylan.a))
    print(f"Only Alice has: {res}")
    res = bob.a.difference(alice.a.union(charlie.a, dylan.a))
    print(f"Only Bob has: {res}")
    res = charlie.a.difference(alice.a.union(bob.a, dylan.a))
    print(f"Only Charlie has: {res}")
    res = dylan.a.difference(alice.a.union(bob.a, charlie.a))
    print(f"Only Dylan has: {res}")
    print()
    print(f"Alice is missing: {achieve_set.difference(alice.a)}")
    print(f"Bob is missing: {achieve_set.difference(bob.a)}")
    print(f"Charlie is missing: {achieve_set.difference(charlie.a)}")
    print(f"Dylan is missing: {achieve_set.difference(dylan.a)}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    gen_player_achievements()
