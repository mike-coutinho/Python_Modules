from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (BattleStrategy, NormalStrategy,
                 AggressiveStrategy, DefensiveStrategy)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]):
    if len(opponents) < 2:
        raise ValueError("Two or more opponents are required for a battle.")

    format_opps = []
    for factory, strategy in opponents:
        factory_name = factory.__class__.__name__
        strategy_name = strategy.__class__.__name__

        factory_name = factory_name.removesuffix("CreatureFactory")
        strategy_name = strategy_name.removesuffix("Strategy")

        format_opps.append(f"({factory_name}+{strategy_name})")
    result = (f"[ {', '.join(format_opps)} ]")
    print(result)

    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print("* Battle *")
            print(f"{creature1.describe()}")
            print(" vs.")
            print(f"{creature2.describe()}")
            print(" now fight!")

            try:
                print(f"{strategy1.act(creature1)}")
                print(f"{strategy2.act(creature2)}\n")
            except TypeError as error:
                print(f"{error}\n")
                return


if __name__ == "__main__":
    flame_factory = FlameFactory()
    healing_factory = HealingCreatureFactory()
    aqua_factory = AquaFactory()
    trasform_factory = TransformCreatureFactory()

    print("Tournament 0 (basic)")
    battle([(flame_factory, NormalStrategy()),
            (healing_factory, DefensiveStrategy())])

    print("Tournament 1 (error)")
    battle([(flame_factory, AggressiveStrategy()),
            (healing_factory, DefensiveStrategy())])

    print("Tournament 2 (multiple)")
    battle([(aqua_factory, NormalStrategy()),
            (healing_factory, DefensiveStrategy()),
            (trasform_factory, AggressiveStrategy())])
