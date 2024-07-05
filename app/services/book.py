from app.schemas.book import BookDetails
from typing import Tuple, Optional


# TODO: Functions to process http requests


class BookService:
    def __init__(self) -> None:
        pass

    # Simulating a database
    all_books = {
        0: {
            "title": "George the Great!",
            "author": "George N. et al",
            "release_year": 2020,
            "is_liked": True
        }
    }

    async def get_book(self, book_id: int) -> BookDetails:
        book = self.all_books[book_id]
        return BookDetails(**book)

    async def multiple_books(self, start: int, limit: int) -> Tuple[list[BookDetails], int]:
        list_of_books = []
        keys = list(self.all_books.keys())
        total = len(keys)

        for index in range(0, len(keys), 1):
            if index < start:
                continue
            current_key = keys[index]
            book = await self.get_book(current_key)
            list_of_books.append(book)

            if len(list_of_books) >= limit:
                break
        return list_of_books, total

    async def create_or_update_book(self, book_details: BookDetails, new_book_id: Optional[int] = None) -> int:
        if new_book_id is None:
            new_book_id = len(self.all_books)

        self.all_books[new_book_id] = {
            "title": book_details.title,
            "author": book_details.author,
            "release_year": book_details.release_year,
            "is_liked": book_details.is_liked
        }
        return new_book_id

    async def delete_book(self, book_id: int):
        del self.all_books[book_id]
        return None
