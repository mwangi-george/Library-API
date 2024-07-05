from pydantic import BaseModel, Field
from typing import Union


# TODO: Models


class BookDetails(BaseModel):
    title: str = Field(
        title="Book Title",
        description="This refers to the title of the book",
        max_length=40,
        min_length=1
    )
    author: Union[str, list[str]]
    release_year: int
    is_liked: bool


class MultipleBooksResponse(BaseModel):
    books: list[BookDetails]
    total: int


class BookCreatedConfirmation(BaseModel):
    created_book_id: int = Field(
        description="This is the id of the created book in the database server"
    )


class BookDeletionResponse(BaseModel):
    message: str
