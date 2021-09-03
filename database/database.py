import json
from datetime import datetime
from typing import Optional

import requests


class SingletonValidation(Exception):
    pass


class Database:
    """
    Pseudo Database class
    TODO: add method that creates JSON file on first usage and update it
    TODO: if already exists

    :create: create Database if doesn't exists
    :fetch_json_data: download data to database
    :create_data_view: creates view from data
        view[title] = {
            "date": int(date),
            "authors": None
        }
    """
    db = None

    @classmethod
    def create(cls) -> 'Database':
        if cls.db is None:
            cls.db = {'items': []}
            cls.fetch_json_data()
            return cls.db
        else:
            raise SingletonValidation()

    @classmethod
    def fetch_json_data(cls, name: str = 'Hobbit') -> Optional[Exception]:
        """Fetch JSON data and append it to db"""
        try:
            url = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={name}')
            text = url.text
            data = json.loads(text)
            cls.db['items'].extend(data['items'])
        except Exception as e:
            return e

    @classmethod
    def create_data_view(cls) -> 'view':
        """Create view from DB"""
        view = {}
        for i, _ in enumerate(cls.db['items']):
            try:
                date = datetime.strptime(cls.db['items'][i]['volumeInfo']['publishedDate'], '%Y-%M-%d')
                date = date.year
            except ValueError:
                try:
                    date = datetime.strptime(cls.db['items'][i]['volumeInfo']['publishedDate'], '%Y-%M')
                    date = date.year
                except ValueError:
                    date = cls.db['items'][i]['volumeInfo']['publishedDate']
            try:
                title = cls.db['items'][i]['volumeInfo']['title']
                authors = cls.db['items'][i]['volumeInfo']['authors']
                view[title] = {
                    "date": int(date),
                    "authors": authors
                }
            except KeyError:
                view[title] = {
                    "date": int(date),
                    "authors": None
                }

        return dict(view)
