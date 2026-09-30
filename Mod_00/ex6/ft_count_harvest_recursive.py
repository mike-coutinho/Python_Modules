def recursive(i, days):
    if i <= days:
        print("Day", i)
        recursive(i + 1, days)


def ft_count_harvest_recursive():
    days_until_harvest = int(input("Days until harvest: "))
    i = int(1)
    recursive(i, days_until_harvest)
    print("Harvest time!")
