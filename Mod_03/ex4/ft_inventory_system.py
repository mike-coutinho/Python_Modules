import sys


def do_it():
    inventory = {}
    for arg in sys.argv[1:]:
        if ':' not in arg:
            print(f"Error - invalid parameter '{arg}'")
        else:
            key, value = arg.split(':', 1)
            if key in inventory:
                print(f"Redundant item '{key}' - discarding")
                continue
            elif not key:
                print("Name of the item cannot be an empty string - dicarding")
                continue
            try:
                inventory[key] = int(value)
            except ValueError as error:
                print(f"Quantity error for '{key}': {error}")
    print(f"Got inventory: {inventory}")
    if inventory:
        print(f"Item list: {list(inventory.keys())}")
        print(f"Total quantity of the {len(inventory)}"
              f" items: {sum(inventory.values())}")
        for key in inventory:
            tmp = inventory[key] / sum(inventory.values()) * 100
            print(f"Item {key} represents {round(tmp, 1)}%")
        most_abundant = max(inventory, key=inventory.get)
        print(f"Item most abundant: {most_abundant} "
              f"with quantity {inventory[most_abundant]}")
        least_abundant = min(inventory, key=inventory.get)
        print(f"Item least abundant: {least_abundant} "
              f"with quantity {inventory[least_abundant]}")
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")
    else:
        print("Nothing to do :)")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    do_it()
