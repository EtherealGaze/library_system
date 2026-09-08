import json
from pathlib import Path
from models import Book

BASE_DIR=Path(__file__).parent
DATA_DIR=BASE_DIR/"data"
DATA_FILE=DATA_DIR/"books.json"
def load_books():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r",encoding="utf-8") as file:
            data=json.load(file)

        if not isinstance(data,list):
            print("文件格式错误，用空数据")
            return []

        return [Book.from_dict(book_dict) for book_dict in data]

    except json.JSONDecodeError:
        print("JSON 文件格式错误，已使用空数据。")
        return []

    except OSError as error:
        print(f"读取文件失败：{error}")
        return []

def save_books(books):
    try:
        DATA_DIR.mkdir(exist_ok=True)
        data=[book.to_dict() for book in books]
        with DATA_FILE.open("w",encoding="utf-8") as file:
                json.dump(data,file)

        return True
    except OSError as error:
        print(f"保存文件失败{error}")
        return False