# books_rest_api

## How to run app on local machine
```
$ git clone https://github.com/czakuou/book_api
$ uvicorn main:app --reload
```
## Bugs
App seems to not run properly after hosting on `Heroku` but works fine on local machine (photos below)
```
1. Published date always return empty list
2. Author search returs bad results
3. ID search return Internal Server Error
```
## What I've learned
1. FastAPI framework
2. How to make API (I've known what It is and how It works but never made one before)
3. It's the first time when I could use Singleton in my project
4. How to deplay on Heroku
5. The fact that the API works locally does not mean that it will work after deployment (It's something i will have to debug in free time)

## Photos of working app on local machine
![.](/img/home.png)
![.](/img/books.png)
# url/books
![.](/img/books_work.png)
# url/books?published_date=
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


