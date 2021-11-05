from fastapi import FastAPI, Query, Path, Body
from schemas import Book, Author, BookOut
from typing import List

app = FastAPI()


@app.post('/book', response_model=Book, response_model_exclude_unset=False)
# @app.post('/book', responce_model=Book, response_model_exclude/include={"pages", "date"}
def create_book(item: Book, author: Author, quantity: int = Body(...)):
    return {"item": item, "author": author, "quantity": quantity}


@app.post('/book', response_model=BookOut)
def create_book_two(item: Book):
    return BookOut(**item.dict(), id=5)


@app.post('/author')
def create_author(author: Author = Body(..., embed=True)):
    return {"author": author}


@app.get('/book')
# def get_book(q: str = Query(..., min_length=2, max_length=7, description="search book")):
def get_book(q: List[str] = Query(["first item", "2nd item"], description="search book", deprecated=True)):
    return q


"""параметры и валидация при запросе одной книги"""
@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=23), pages: int = Query(None, gt=17, le=479)):
    return {"pk": pk, "pages": pages}
