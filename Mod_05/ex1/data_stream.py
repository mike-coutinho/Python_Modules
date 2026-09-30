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


class DataStream:
    def __init__(self):
        self.processors = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            for processor in self.processors:
                if processor.validate(item):
                    processor.ingest(item)
                    break
            else:
                print(f"DataStream error - "
                      f"Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
        else:
            for processor in self.processors:
                print(f"{processor.__class__.__name__}: total "
                      f"{processor.data_index + 1} items processed, remaining "
                      f"{len(processor.data_stored)} on processor")
        print()


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    datastream = DataStream()
    datastream.print_processors_stats()

    print("Registering Numeric Processor\n")
    numeric_processor = NumericProcessor()
    datastream.register_processor(numeric_processor)

    data_to_test = [
        'Hello world', [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil isconnected'}],
        42, ['Hi', 'five']]

    print(f"Send first batch of data on stream: {data_to_test}")
    datastream.process_stream(data_to_test)
    datastream.print_processors_stats()

    print("Registering other data processors")
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    datastream.register_processor(text_processor)
    datastream.register_processor(log_processor)

    print("Send the same batch again")
    datastream.process_stream(data_to_test)
    datastream.print_processors_stats()

    print("Consume elements from data processors: Numeric 3, Text 2, Log 1")
    try:
        for i in range(3):
            numeric_processor.output()
        for i in range(2):
            text_processor.output()
        for i in range(1):
            log_processor.output()
    except Exception as error:
        print(error)

    datastream.print_processors_stats()
