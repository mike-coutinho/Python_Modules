class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self._height = height
        self._days = days
        self.internal_system = self.Internal_system()
        self.show()

    class Internal_system:
        def __init__(self):
            self.growth_calls = 0
            self.age_calls = 0
            self.show_calls = 0
            self.shade_calls = 0

        def show_stats(self, obj) -> None:
            print(f"Stats: {self.growth_calls} grow,"
                  f" {self.age_calls} age, {self.show_calls} show")
            if isinstance(obj, Tree):
                print(f"{self.shade_calls} shade")

    @staticmethod
    def check_older_than_a_year(age) -> bool:
        return age > 365

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
        self.internal_system.show_calls += 1

    def grow(self, rate) -> None:
        self._height += rate
        self.internal_system.growth_calls += 1

    def age(self, days) -> None:
        self._days += days
        self.internal_system.age_calls += 1

    @classmethod
    def anonymous(cls):
        cls.name = "Unknown plant"
        cls._height = 0.0
        cls._days = 0
        return cls(cls.name, cls._height, cls._days)


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
    def __init__(self, name: str, height: float,
                 days: int, trunk_diameter: float
                 ):
        self.trunk_diameter = trunk_diameter
        super().__init__(name, height, days)

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 2)}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of"
              f"{self._height}cm long and {self.trunk_diameter}cm wide.")
        self.internal_system.shade_calls += 1


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 days: int, harvest_season: str, nutritional_value: int
                 ):
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


class Seed(Flower):
    def __init__(self, name: str, height: float, days: int, color: str):
        self.seeds = 0
        super().__init__(name, height, days, color)

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")

    def bloom(self):
        self.seeds += 42
        super().bloom()


def statistics(obj) -> None:
    print(f"[statistics for {obj.name}]")
    obj.internal_system.show_stats(obj)


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    result = Plant.check_older_than_a_year(30)
    print("Is 30 days more than a year? ->", result)
    result = Plant.check_older_than_a_year(400)
    print("Is 400 days more than a year? ->", result)
    print()

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "Red")
    statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    statistics(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    statistics(oak)

    print()
    print("=== Seed")
    sunflower_seed = Seed("Sunflower", 80, 45, "Yellow")
    print("[make sunflower grow, age and bloom]")
    sunflower_seed.grow(30)
    sunflower_seed.age(20)
    sunflower_seed.bloom()
    statistics(sunflower_seed)

    print()
    print("=== Anonymous")
    anom = Plant.anonymous()
    statistics(anom)
