class Plant:
    def __init__(self, name, height, days) -> None:
        self.name = str(name)
        self.height = float(height)
        self.days = int(days)
        self.growth = float(0)
        print("Created: ", end="")
        self.show()

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
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)
