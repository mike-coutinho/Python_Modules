import alchemy
from .. import potions


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: "
            f"brew '{alchemy.create_air()}' and '{alchemy.strength_potion()}'"
            f" mixed with '{potions.create_fire()}'")
