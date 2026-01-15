import sys

from src.infrastructure.repositories.csv_book_repository import CsvBookRepository


class CommandHandler:
    def __init__(self) -> None:
        self._csv_book_repository = CsvBookRepository("books.csv")
        self._commands = {
            "1": self._add_item,
            "2": self._list_items,
            "3": self._search_items,
            "4": self._exit,
        }

    def run(self) -> None:
        while True:
            print("1:追加, 2:一覧, 3:検索, 4:終了")
            choice = input("選んでください: ")

            command = self._commands.get(choice)

            if not command:
                print("無効な入力")
                continue

            command()

    def _add_item(self) -> None:
        title = input("タイトル: ")
        author = input("著者: ")
        price = input("価格: ")

        if title == "" or author == "" or price == "":
            print("エラー")
        else:
            self._csv_book_repository.save(title, author, price)

    def _list_items(self) -> None:
        books = self._csv_book_repository.load()

        if len(books) == 0:
            print("データがありません")
            return

        for book in books:
            print(f"タイトル: {book[0]} 著者: {book[1]} 価格: {book[2]}")

    def _search_items(self) -> None:
        query = input("検索キーワード: ")

        books = self._csv_book_repository.load()

        if len(books) == 0:
            print("データがありません")
            return

        books = [book for book in books if query in book[0] or query in book[1]]

        if len(books) == 0:
            print("データが見つかりません")
            return

        for book in books:
            print(f"タイトル: {book[0]} 著者: {book[1]} 価格: {book[2]}")

    def _exit(self) -> None:
        print("終了します")
        sys.exit()
