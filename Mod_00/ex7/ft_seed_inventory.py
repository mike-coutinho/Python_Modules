def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        string_variable = "packets available"
    elif unit == "grams":
        string_variable = "grams total"
    elif unit == "area":
        string_variable = "square meters"
    else:
        print("Unknown unit type")
        return
    print(seed_type.capitalize(), "seeds:", end=" ")
    if string_variable == "square meters":
        print("covers", end=" ")
    print(quantity, string_variable)
