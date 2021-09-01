from typing import Any, Optional

from fastapi import FastAPI, Query

from modules import *
from schemas import *
from database import Database

app = FastAPI()
db = Database.create()


@app.get('/books')
async def books(published_date: Optional[int] = None,
                sort: Optional[Any] = None,
                author: Optional[list[str]] = Query(None)):
    db_view = Database.create_data_view()
    books_list = None

    if sort is not None:
        books_list = [k for k, v in sorted(db_view.items(), key=lambda item: item[1]['date'])]

    if published_date is not None:
        books_list = [k for k, v in db_view.items()
                      if published_date == v['date']]

    if author is not None:
        author = parse_list(author)
        books_list = [k for k, v in db_view.items()
                      for search_aut in author
                      for db_aut in v['authors']
                      if search_aut == db_aut]

    if books_list is None:
        books_list = [k for k, v in db_view.items()]

    return {"titles": books_list}


@app.get('/books/{bookid}', response_model=BookByID)
async def books_byID(bookid: str):
    for item in db['items']:
        if bookid == item['id']:
            return item['volumeInfo']
    return 'No book with that ID'


@app.post('/db')
async def update_database(data: Optional[Data]):
    try:
        Database.fetch_json_data(data.q)
        return 'Data updated successfully'
    except Exception as e:
        return 'Error while downloading data'
