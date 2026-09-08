def print_line():
    print("-" * 70)


def show_book(book):
    print(
        f"编号：{book.book_id}\n"
        f"书名：{book.title}\n"
        f"作者：{book.author}\n"
        f"状态：{'已借出' if book.is_borrowed else '可借阅'}"
    )


def show_books(books):
    """显示图书列表"""
    if not books:
        print("暂无图书。")
        return

    print("-" * 70)
    print(f"{'编号':<10}{'书名':<20}{'作者':<15}{'状态'}")
    print("-" * 70)

    for book in books:
        status = "已借出" if book.is_borrowed else "可借阅"
        print(
            f"{book.book_id:<10}"
            f"{book.title:<20}"
            f"{book.author:<15}"
            f"{status}"
        )

    print("-" * 70)


def input_not_empty(message):
    """获取非空输入"""
    while True:
        value = input(message).strip()

        if value:
            return value

        print("输入内容不能为空，请重新输入。")


def confirm(message):
    """获取确认信息"""
    answer = input(f"{message}（y/n）：").strip().lower()
    return answer == "y"