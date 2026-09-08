class Book:
    def __init__(self,book_id,title,author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            return False

        self.is_borrowed = True
        return True

    def return_book(self):
        if not self.is_borrowed:
            return False

        self.is_borrowed = False
        return True

    def __str__(self):
        status="已借出"if self.is_borrowed else "可借阅"
        return f"{self.book_id}|{self.title}|{self.author}|{status}"

    def show_information(self):
        print("编号"+self.book_id)
        print("书名"+self.title)
        print("作者"+self.author)
        print("是否借出"+str(self.is_borrowed))

    def to_dict(self):
        """将对象转化为字典，方便保存JSON"""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "is_borrowed": self.is_borrowed
        }

#类方法
    @classmethod
    def from_dict(cls, data):
        """从字典穿件Book对象"""
        book= cls(book_id=data["book_id"],
                   title=data["title"],
                   author=data["author"],
                   )
        book.is_borrowed = data.get("is_borrowed", False)
        return book