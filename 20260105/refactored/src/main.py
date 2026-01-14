import sys

from infrastructure.repositories.csv_book_repository import CsvBookRepository


def f():
    try:
        g = open("data.txt", "r")
        h = g.readlines()
        g.close()
        return h
    except:
        return []


def main():
    csv_book_repository = CsvBookRepository("books.csv")

    while True:
        print("1:追加, 2:一覧, 3:検索, 4:終了")
        i = input("選んでください: ")
        if i == "1":
            j = input("タイトル: ")
            k = input("著者: ")
            l = input("価格: ")
            if j == "" or k == "" or l == "":
                print("エラー")
            else:
                csv_book_repository.save(j, k, l)
        elif i == "2":
            m = f()
            for n in m:
                o = n.split(",")
                print(
                    "タイトル:"
                    + o[0]
                    + " 著者:"
                    + o[1]
                    + " 価格:"
                    + o[2].replace("\n", "")
                )
        elif i == "3":
            p = input("検索キーワード: ")
            q = f()
            r = 0
            for s in q:
                t = s.split(",")
                if p in t[0] or p in t[1]:
                    print("発見:" + t[0] + "(" + t[1] + ")")
                    r = r + 1
            if r == 0:
                print("なし")
        elif i == "4":
            print("終了します")
            sys.exit()
        else:
            if i == "999":
                open("data.txt", "w").close()
                print("初期化しました")
            else:
                print("無効な入力")


if __name__ == "__main__":
    main()
