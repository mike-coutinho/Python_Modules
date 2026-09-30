class Plant:
    def __init__(self, name: str, height, days) -> None:
        self.name: str = name
        self._height = float(height)
        self._days = int(days)
        self.growth = float(0)
        print("Plant created: ", end="")
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

    def grow(self) -> None:
        rate = 0.8
        self._height += rate
        self.growth += rate

    def age(self) -> None:
        self._days += 1


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-3)
    rose.set_age(-3)
    print()
    print(f"Current state: {rose.name}: ", end="")
    print(f"{round(rose.get_height(), 2)}cm, {rose.get_age()} days old")
