class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self._height = height
        self._days = days
        self.show()

    def set_height(self, height) -> None:
        if height > 0:
            self._height = height
            print("Height updated: {0}cm".format(height))
        else:
            print("{0}: Error, height can't be negative".format(self.name))
            print("Height update rejected")

    def set_age(self, age) -> None:
        if age > 0:
            self._days = age
            print("Age updated: {0} days".format(age))
        else:
            print("{0}: Error, age can't be negative".format(self.name))
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def show(self) -> None:
        print(f'{self.name}: ', end="")
        print(f'{round(self._height, 2)}cm, {self._days} days old')

    def grow(self, rate) -> None:
        self._height += rate

    def age(self, days) -> None:
        self._days += days


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: str):
        self.color = color
        self.blooming = False
        super().__init__(name, height, days)

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.blooming is False:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")

    def bloom(self) -> None:
        self.blooming = True
        self.show()


class Tree(Plant):
    def __init__(
            self, name: str, height: float, days: int,
            trunk_diameter: float
            ):
        self.trunk_diameter = trunk_diameter
        super().__init__(name, height, days)

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 2)}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name, height, days,
                 harvest_season: str, nutritional_value: int) -> None:
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        super().__init__(name, height, days)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def age(self, days) -> None:
        super().age(days)
        self.nutritional_value += days


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15, 10, "Red")
    print("[asking the rose to bloom]")
    rose.bloom()
    print()

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April", 0)
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42)
    tomato.age(20)
    tomato.show()
