#!python3
from pathlib import Path
import sys

ARGS = sys.argv[1:]


class DataGatherer:
    def __init__(self, filepath: Path) -> None:
        self.filepath = filepath
        self.raw_data = self._parse_file()
        self.unique_words = ""
        self.total_words = ""
        self.line_count = ""

    def _parse_file(self) -> bytes:
        with open(self.filepath, "rb") as file_data:
            return file_data.read()

    def count_unique_words(self): ...

    def count_number_of_lines(self): ...


def main():
    if len(ARGS) != 2:
        raise Exception(f"{len(ARGS)} is not the right number of args! It should be 2!")

    flag_val, input_path = ARGS

    results = DataGatherer(input_path)


if __name__ == "__main__":
    main()
