import csv
from typing import List, TypeVar

Type = TypeVar("Type")


class CsvReader:
    def __init__(self, base_path='inputs/'):
        self.base = base_path

    def read(self, csv_path: str,  type: Type) -> List[any]:
        full_path = self.base + csv_path
        try:
            data_obj = []
            with open(full_path) as stream:
                reader = csv.reader(stream)
                next(reader, None)
                for row in reader:
                    obj = type(*row)
                    data_obj.append(obj)
            return data_obj
        except FileNotFoundError as e:
            raise Exception(
                f"File not found. {full_path}.", e)
        except Exception as e:
            raise Exception(f"Fatal error", e)