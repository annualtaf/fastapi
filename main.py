from typing import Union

from fastapi import FastAPI,Body

app = FastAPI()

BOOKS = [
    {"title":"Title One","name":"python","category":"science"},
    {"title":"Title Two","name":"java","category":"maths"},
    {"title":"Title Three","name":"C","category":"english"},
    {"title":"Title Four","name":"C++","category":"social"}
]

@app.get("/")
def read_root():
    return BOOKS

@app.get("/books/{books_title}")
async def read_book(books_title:str):
    for book in BOOKS:
        if book.get('title').casefold()==books_title.casefold():
            return book

@app.get("/api-endpoint")
async def read_root():
    return {"message": "worlds"}

@app.get("/items/{item_id}")
def read_item(item_id:int, q:Union[str, None]=None):
    return {"item_id": item_id, "q":q}

# http://127.0.0.1:8000/books/?category=science&name=python
@app.get("/books/")
async def read_category_by_query(category:str,name:str):
    books_to_return = []
    print(category,name)
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# post request
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    # first validate if new_book details are valid
    BOOKS.append(new_book)

@app.post("/books/create_book")
async def update_book(updated_book=Body()):
    # first validate if new_book details are valid
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

@app.post("/books/delete_book")
async def delete_book(deleted_book=Body()):
    # first validate if new_book details are valid
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == deleted_book.get('title').casefold():
            BOOKS.pop(i)
            break


# similar @app.put @app.delete to insert and delete a record
