from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    try:
        base_creature = factory.create_base()
        evolved_creature = factory.create_evolved()
    except Exception as error:
        print(f"Error creating creatures: {error}")
        return
    print(base_creature.describe())
    print(base_creature.attack())
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def fight(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    try:
        creature1 = factory1.create_base()
        creature2 = factory2.create_base()
    except Exception as error:
        print(f"Error creating creatures for battle: {error}")
        return
    print(f"{creature1.describe()}")
    print("vs.")
    print(f"{creature2.describe()}")
    print("Fight!")
    print(creature1.attack())
    print(creature2.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    print("Testing factory:")
    test_factory(flame_factory)

    print("\nTesting factory:")
    test_factory(aqua_factory)

    print("\nTesting battle:")
    fight(flame_factory, aqua_factory)
