from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capacities import HealCapability, TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        return creature.attack()

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            if isinstance(creature, TransformCapability):
                return (f"{creature.transform()}\n{creature.attack()}\n"
                        f"{creature.revert()}")

        raise TypeError("Battle error, aborting tournament: Invalid Creature"
                        f" '{creature.__class__.__name__}' for this "
                        "aggressive strategy")

    def is_valid(self, creature: Creature) -> bool:
        if hasattr(creature, "transform"):
            return True
        return False


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            if isinstance(creature, HealCapability):
                return f"{creature.attack()}\n{creature.heal('itself')}"

        raise TypeError("Battle error, aborting tournament: Invalid Creature"
                        f" '{creature.__class__.__name__}' for this "
                        "defensive strategy")

    def is_valid(self, creature: Creature) -> bool:
        if hasattr(creature, "heal"):
            return True
        return False
