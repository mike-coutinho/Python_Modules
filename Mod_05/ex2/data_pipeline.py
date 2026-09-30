from typing import Any, Protocol
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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CsvPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            print("Can't use plugin because there is no data to export")
            return
        print("CSV Output:")
        process_data = ",".join(item for i, item in data)
        print(process_data)


class JsonPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            print("Can't use plugin because there is no data to export")
            return

        process_data = {f"item_{item_id}": value for item_id, value in data}

        print("JSON Output:")
        print(process_data)


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        data = []
        for processors in self.processors:
            for i in range(nb):
                try:
                    item = processors.output()
                except Exception:
                    continue
                data.append(item)
            plugin.process_output(data)
            data = []


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...")
    datastream = DataStream()
    datastream.print_processors_stats()

    print("Registering Numeric Processor\n")
    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    datastream.register_processor(numeric_processor)
    datastream.register_processor(text_processor)
    datastream.register_processor(log_processor)

    data_to_test = [
        'Hello world', [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42, ['Hi', 'five']]

    print(f"Send first batch of data on stream: {data_to_test}")
    datastream.process_stream(data_to_test)
    datastream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    datastream.output_pipeline(3, CsvPlugin())
    print()
    datastream.print_processors_stats()

    data_to_test = [
        21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
             'log_message': 'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168], 'World hello']

    print(f"Send another batch of data: {data_to_test}")
    datastream.process_stream(data_to_test)
    datastream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    datastream.output_pipeline(5, JsonPlugin())
    datastream.print_processors_stats()
