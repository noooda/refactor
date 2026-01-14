import csv


class CsvBookRepository:
    def __init__(self, path: str) -> None:
        self._path = path

    def save(self, title: str, author: str, price: int) -> None:
        with open(self._path, mode="a", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([title, author, price])
