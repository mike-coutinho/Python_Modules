from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self):
        self.data_stored = []
        self.data_index = -1

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.data_stored:
            raise Exception("Error: No item in data to output")
        return self.data_stored.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if (isinstance(data, list)
            and all(isinstance(item, (int, float))
            and not isinstance(item, bool)
                    for item in data)):
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self.data_index += 1
                self.data_stored.append((self.data_index, str(item)))
        else:
            self.data_index += 1
            self.data_stored.append((self.data_index, str(data)))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and all(
                isinstance(item, str) for item in data):
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper text data")
        if isinstance(data, list):
            for item in data:
                self.data_index += 1
                self.data_stored.append((self.data_index, item))
        else:
            self.data_index += 1
            self.data_stored.append(((self.data_index), data))


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        required_keys = {"log_level", "log_message"}
        if (isinstance(data, dict)
            and len(data) == 2
            and set(data.keys()) == required_keys
            and all(isinstance(key, str) and isinstance(value, str)
            and key.strip()
            and value.strip()
                    for key, value in data.items())):
            return True

        if (isinstance(data, list)
            and all(isinstance(key_value_pairs, dict)
            and len(key_value_pairs) == 2
            and set(key_value_pairs.keys()) == required_keys
            and all(isinstance(key, str) and isinstance(value, str)
                    and key.strip()
                    and value.strip()
                    for key, value in key_value_pairs.items())
                    for key_value_pairs in data)):
            return True
        return False

    def ingest(self, data: list | dict) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper log data")
        if isinstance(data, list):
            for dict in data:
                first_value = dict["log_level"]
                second_value = dict["log_message"]
                self.data_index += 1
                self.data_stored.append(
                    (self.data_index, first_value + ": " + second_value))
        else:
            first_value = data["log_level"]
            second_value = data["log_message"]
            self.data_index += 1
            self.data_stored.append(
                (self.data_index, first_value + ": " + second_value))


def tests_on_numeric_processor():
    print("Testing Numeric Processor...")

    numeric_processor = NumericProcessor()

    output = numeric_processor.validate(42)
    print(f" Trying to validate input '42': {output}")
    output = numeric_processor.validate('Hello')
    print(f" Trying to validate input 'Hello': {output}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")

    try:
        numeric_processor.ingest('foo')
    except Exception as error:
        print(f" {error}")

    test_list = [1, 2, 3, 4, 5]
    print(f" Processing data: {test_list}")
    print(" Processing ints: 6, 7, 8")

    try:
        numeric_processor.ingest(test_list)
        numeric_processor.ingest(6)
        numeric_processor.ingest(7)
        numeric_processor.ingest(8)
    except Exception as error:
        print(f" {error}")

    data = numeric_processor.data_stored
    print(f" Data stored in numeric processor: {data}")
    print(" Extracting 3 values...")
    try:
        for i in range(3):
            rank, data = numeric_processor.output()
            print(f"  Numeric value {rank}: {data}")
    except Exception as error:
        print(error)

    print(" Extracting 3 more values and check if the oldest 3 were removed")
    for i in range(3):
        try:
            rank, data = numeric_processor.output()
            print(f"  Numeric value {rank}: {data}")
        except Exception as error:
            print(error)


def tests_on_text_processor():
    print("\nTesting Text Processor...")

    text_processor = TextProcessor()

    print(f" Trying to validate input '42': {text_processor.validate(42)}")

    test_list = ['Hello', 'Nexus', 'World']
    print(f" Processing data: {test_list}")

    try:
        text_processor.ingest(test_list)
    except Exception as error:
        print(f" {error}")

    print(f" Data stored in text processor: {text_processor.data_stored}")
    print(" Extracting 1 values...")
    for i in range(1):
        try:
            rank, data = text_processor.output()
            print(f"  Text value {rank}: {data}")
        except Exception as error:
            print(f" {error}")

    print(" Extracting 3 more values and check if the oldest was removed")
    for i in range(3):
        try:
            rank, data = text_processor.output()
            print(f"  Text value {rank}: {data}")
        except Exception as error:
            print(f"  {error}")


def tests_on_log_processor():
    print("\nTesting Log Processor...")

    log_processor = LogProcessor()

    output = log_processor.validate('Hello')
    print(f" Trying to validate input 'Hello': {output}")

    output = log_processor.validate({'log_level': 'NOTICE'})
    print(f" Trying to validate dict with only 1 key-value pair: {output}")

    output = log_processor.validate([{'log_level': 'NOTICE'},
                                    {'log_level': 'ERROR',
                                     'log_message': 'Unauthorized access!!'}])
    print(f" Trying to validate list dict only 1 key-value pair: {output}")

    test_for_log = {'log_level': 'ERROR', 'log_message': 2}
    output = log_processor.validate(test_for_log)
    print(f" Trying to validate dict with an int: {output}")

    test_for_log = {'log_level': 'ERROR', 'log_message': ''}
    output = log_processor.validate(test_for_log)
    print(f" Trying to validate dict with an empty string: {output}")

    test_for_log = {'ss': 'ERROR', 'awd': 'Unauthorized access!!'}
    output = log_processor.validate(test_for_log)
    print(f" Trying to validate dict with wrong key: {output}")

    test_for_log = [{'log_level': 'NOTICE',
                     'log_message': 'Connection to server'},
                    {'log_level': 'ERROR',
                     'log_message': 'Unauthorized access!!!'}]
    print(f" Processing data: {test_for_log}")

    try:
        log_processor.ingest(test_for_log)
        log_processor.ingest({'log_level': 'test1', 'log_message': 'test2'})

    except Exception as error:
        print(f" {error}")

    print(f" Data stored in log processor: {log_processor.data_stored}")
    print(" Extracting 2 values...")
    for i in range(2):
        try:
            rank, data = log_processor.output()
            print(f"  Log value {rank}: {data}")
        except Exception as error:
            print(f"  {error}")

    print(" Extracting 2 more values and check if the oldest 2 was removed")
    for i in range(2):
        try:
            rank, data = log_processor.output()
            print(f"  Log value {rank}: {data}")
        except Exception as error:
            print(f"  {error}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    tests_on_numeric_processor()
    tests_on_text_processor()
    tests_on_log_processor()
