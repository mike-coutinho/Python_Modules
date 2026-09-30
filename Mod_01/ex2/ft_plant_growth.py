class Plant:
    def __init__(self, name, height, days) -> None:
        self.name = str(name)
        self.height = float(height)
        self.days = int(days)
        self.growth = float(0)

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 2)}cm, {self.days} days old")

    def grow(self) -> None:
        rate = 0.8
        self.height += rate
        self.growth += rate

    def age(self) -> None:
        self.days += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", "25", "30")
    rose.show()
    for i in range(1, 8):
        print("=== Day {0} ===". format(i))
        rose.grow()
        rose.age()
        rose.show()
    print("Growth this week: {0}cm". format(rose.growth))
