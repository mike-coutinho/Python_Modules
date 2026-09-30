def input_temperature(temp_str: str) -> int | None:
    print(f"Input data is '{temp_str}'")
    try:
        test = int(temp_str)
        print(f"Temperature is now {temp_str}°C.\n")
        return test
    except Exception as error:
        print(f"Caught input_temperature error: {error}\n")
        return None


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    input_temperature("25")
    input_temperature("abc")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
