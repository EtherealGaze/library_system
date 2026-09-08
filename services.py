def find_book(books,book_id):
    for book in books:
        if book.book_id == book_id:
            return book
    return None

def search_books(books,keywords):
    keywords=keywords.lower()
    result=[]

    for book in books:
        if(keywords in book.title.lower()
        or keywords in book.book_id.lower()
        or keywords in book.author.lower()
        ):
            result.append(book)

    return result

def add_book(books,book):
    if find_book(books,book.book_id) is not None:
        return False

    books.append(book)
    return True

def delete_book(books,book_id):
    book=find_book(books,book_id)
    if book is None:
        return False,"图书不存在。"
    if book.is_borrowed:
        return False,"图书已经借出 不能删除。"

    books.remove(book)
    return True,"图书删除成功"

def borrow_book(books,book_id):
    book=find_book(books,book_id)

    if book is None:
        return False,"图书不存在。"

    if not book.borrow():
        return False,"这本书被借出。"

    return True,"借阅成功"

def return_book(books, book_id):
    """归还图书"""
    book = find_book(books, book_id)

    if book is None:
        return False, "图书不存在。"

    if not book.return_book():
        return False, "这本书没有被借出。"

    return True, "归还成功。"