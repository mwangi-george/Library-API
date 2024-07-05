from fastapi import FastAPI
from app.routes.book import create_book_routes


def create_app() -> FastAPI:
    # return app
    app = FastAPI(
        title="Library Backend Services",
        description="Made with ❤️ by George Mwangi"
    )
    book_router = create_book_routes()
    app.include_router(book_router)

    return app


app = create_app()
