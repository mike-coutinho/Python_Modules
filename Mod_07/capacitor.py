from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_factory(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    try:
        base_creature = factory.create_base()
        evolved_creature = factory.create_evolved()
    except Exception as error:
        print(f"Error creating creatures: {error}")
        return
    print(" base:")
    print(base_creature.describe())
    print(base_creature.attack())
    try:
        print(base_creature.heal("itself"))
    except Exception as error:
        print(f"Error calling heal on base creature: {error}")
    print(" evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    try:
        print(evolved_creature.heal("itself and others"))
    except Exception as error:
        print(f"Error calling heal on evolved creature: {error}")


def test_transform_factory(factory: TransformCreatureFactory) -> None:
    print("\nTesting Creature with transform capability")
    try:
        base_creature = factory.create_base()
        evolved_creature = factory.create_evolved()
    except Exception as error:
        print(f"Error creating creatures: {error}")
        return
    print(" base:")
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.transform())
    print(base_creature.attack())
    print(base_creature.revert())
    print(" evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.transform())
    print(evolved_creature.attack())
    print(evolved_creature.revert())


if __name__ == "__main__":
    healing_factory = HealingCreatureFactory()
    test_healing_factory(healing_factory)

    transform_factory = TransformCreatureFactory()
    test_transform_factory(transform_factory)
