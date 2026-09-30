import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    player_list = ["player 1", "player 2", "player 3", "player 4",
                   "player 5", "player 6", "player 7", "player 8",
                   "player 9", "player 10", "player 11", "player 12",
                   "player 13", "player 14", "player 15", "player 16",
                   "player 17", "player 18", "player 19", "player 20",
                   "player 21", "player 22", "player 23", "player 24",
                   "player 25", "player 26", "player 27",]

    actions = ["scored a goal", "received a yellow card",
               "received a red card", "made an assist",
               "missed a penalty", "was substituted", "was injured",
               "made a great save", "made a bad tackle", "was offside",
               "scored an own goal", "made a hat-trick", "was sent off",
               "made a great pass", "made a bad pass", "was fouled"]
    while True:
        event: tuple[str, str]
        event = random.choice(player_list), random.choice(actions)
        yield event


def consume_event(list_pa: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:
    while list_pa:
        item_to_remove = random.choice(list_pa)
        list_pa.remove(item_to_remove)
        yield item_to_remove


if __name__ == "__main__":
    list_pa = []
    for i in range(1000):
        event: tuple[str, str] = next(gen_event())
        print(f"Event {i}: {event[0]} {event[1]}")
        if i < 10:
            list_pa.append(event)

    print("Built list of 10 events:", list_pa)
    for item_to_remove in consume_event(list_pa):
        print("Got event from list:", item_to_remove)
        print("Remains in list:", list_pa)
