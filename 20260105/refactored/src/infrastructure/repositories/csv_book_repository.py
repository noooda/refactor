import csv


class CsvBookRepository:
    def __init__(self, path: str) -> None:
        self._path = path

    def save(self, title: str, author: str, price: str) -> None:
        with open(self._path, mode="a", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([title, author, price])

    def load(self) -> list[list[str]]:
        with open(self._path, mode="r", newline="", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            return [row for row in reader]
