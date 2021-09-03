# books_rest_api

## How to run app on local machine
```
$ git clone https://github.com/czakuou/book_api
$ unicorn main:app --reload
```
## Bugs
App seems to not work properly after hosting on `Heroku` but works fine on local machine (photos below)
```
1. Published date always return empty list
2. Author search returs bad results
3. ID search return Internal Server Error
```
## Photos of working app on local machine
![.](/img/home.png)
![.](/img/books.png)
# url/books
![.](/img/books_work.png)
# url/books?published=
![.](/img/books_date.png)
# url/books?author=
![.](/img/books_author.png)
# url/books?sort=
![.](/img/books_sort.png)
# url/books/{bookid}
![.](/img/books_id.png)
# url/books/db
![.](/img/db_update.png)
![.](/img/data_after_update.png)

