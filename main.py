from models import Book
from services import *
from storage import load_books, save_books
from utils import confirm, input_not_empty, show_book, show_books


def show_menu():
    print()
    print("=" * 70)
    print("                       图书管理系统")
    print("=" * 70)
    print("1. 添加图书")
    print("2. 查看图书")
    print("3. 查询图书")
    print("4. 借阅图书")
    print("5. 归还图书")
    print("6. 删除图书")
    print("0. 退出系统")
    print("=" * 70)


def add_book_action(books):
    print("\n--- 添加图书 ---")

    book_id = input_not_empty("请输入图书编号：")

    if find_book(books, book_id) is not None:
        print("图书编号已经存在，不能重复添加。")
        return

    title = input_not_empty("请输入书名：")
    author = input_not_empty("请输入作者：")

    book = Book(book_id, title, author)

    if add_book(books, book):
        save_books(books)
        print("图书添加成功。")
    else:
        print("图书添加失败。")


def list_books_action(books):
    print("\n--- 图书列表 ---")
    show_books(books)


def search_books_action(books):
    print("\n--- 查询图书 ---")

    if not books:
        print("暂无图书。")
        return

    keyword = input_not_empty("请输入编号、书名或作者：")
    result = search_books(books, keyword)

    if result:
        show_books(result)
    else:
        print("没有找到符合条件的图书。")


def borrow_book_action(books):
    print("\n--- 借阅图书 ---")

    book_id = input_not_empty("请输入要借阅的图书编号：")
    success, message = borrow_book(books, book_id)

    print(message)

    if success:
        save_books(books)


def return_book_action(books):
    print("\n--- 归还图书 ---")

    book_id = input_not_empty("请输入要归还的图书编号：")
    success, message = return_book(books, book_id)

    print(message)

    if success:
        save_books(books)


def delete_book_action(books):
    print("\n--- 删除图书 ---")

    book_id = input_not_empty("请输入要删除的图书编号：")
    book = find_book(books, book_id)

    if book is None:
        print("图书不存在。")
        return

    print("找到以下图书：")
    show_book(book)

    if not confirm("确定要删除这本图书吗"):
        print("已取消删除。")
        return

    success, message = delete_book(books, book_id)
    print(message)

    if success:
        save_books(books)


def main():
    books = load_books()

    while True:
        show_menu()
        choice = input("请选择功能：").strip()

        if choice == "1":
            add_book_action(books)

        elif choice == "2":
            list_books_action(books)

        elif choice == "3":
            search_books_action(books)

        elif choice == "4":
            borrow_book_action(books)

        elif choice == "5":
            return_book_action(books)

        elif choice == "6":
            delete_book_action(books)

        elif choice == "0":
            save_books(books)
            print("数据已保存，感谢使用，再见！")
            break

        else:
            print("输入错误，请输入 0 到 6 之间的数字。")


if __name__ == "__main__":
    main()