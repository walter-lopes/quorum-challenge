import csv
import pathlib


class CsvWriter:

    def __init__(self, base_path='outputs/'):
        self.base_path = base_path

    def write(self, data, file_path: str):
        try:
            filename = self.base_path + file_path
            path = pathlib.Path(filename)
            path.parent.mkdir(exist_ok=True)
            with open(filename, "w") as stream:
                writer = csv.writer(stream)
                writer.writerow(data[0].header())
                writer.writerows(data)
                return True
        except Exception as e:
            raise Exception(f"Fatal error", e)
