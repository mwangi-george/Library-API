from fastapi import (
    APIRouter,
    status
)
from app.schemas.book import (
    BookDetails,
    MultipleBooksResponse,
    BookCreatedConfirmation,
    BookDeletionResponse,
)
from app.services.book import BookService
from fastapi.responses import PlainTextResponse


# TODO: Routes Definition


def create_book_routes():

    book_service = BookService()
    book_router = APIRouter(
        prefix="/book",
        tags=["Books API Endpoints"]
    )

    @book_router.get("/all", response_model=MultipleBooksResponse, status_code=status.HTTP_200_OK)
    async def get_multiple_books(start: int = 0, limit: int = 20) -> MultipleBooksResponse:
        books, total = await book_service.multiple_books(start, limit)
        books_formatted = MultipleBooksResponse(books=books, total=total)
        return books_formatted

    @book_router.get("/{book_id}", response_model=BookDetails, status_code=status.HTTP_200_OK)
    async def get_book_by_id(book_id: int = 0) -> BookDetails:
        details = await book_service.get_book(book_id)
        return details

    @book_router.post("/", status_code=status.HTTP_201_CREATED)
    async def add_book_to_server(book_details: BookDetails) -> BookCreatedConfirmation:
        created_book_id = await book_service.create_or_update_book(book_details=book_details)
        created_book_id_fmt = BookCreatedConfirmation(
            created_book_id=created_book_id
        )
        return created_book_id_fmt

    @book_router.put("/{book_id}", response_model=BookDetails)
    async def update_book_info(book_id: int, book_profile: BookDetails) -> BookDetails:
        updated_book_id = await book_service.create_or_update_book(book_profile, book_id)
        book_details = await book_service.get_book(updated_book_id)
        return book_details

    @book_router.delete("/{book_id}", response_model=BookDeletionResponse)
    async def remove_book_by_id(book_id: int) -> BookDeletionResponse:
        await book_service.delete_book(book_id)
        msg = BookDeletionResponse(message="Book Deleted Successfully!")
        return msg

    return book_router
