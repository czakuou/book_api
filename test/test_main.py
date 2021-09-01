from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_home():
    response = client.get('/')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}


def test_read_books():
    response = client.get('/books')
    body = {
        'titles': [
            "Hobbit czyli Tam i z powrotem",
            "Hobbit",
            "LEGO The Hobbit",
            "The Hobbit",
            "The History of the Hobbit",
            "Finding God in the Hobbit",
            "I Am in Fact a Hobbit",
            "CliffsNotes on Tolkien's The Lord of the Rings & The Hobbit",
            "A Hobbit Devotional"
        ]
    }
    assert response.status_code == 200
    assert response.json() == body


def test_read_books_sorted():
    response = client.get('/books?sort=-')
    body = {
          "titles": [
            "The Hobbit",
            "I Am in Fact a Hobbit",
            "Hobbit czyli Tam i z powrotem",
            "The History of the Hobbit",
            "Finding God in the Hobbit",
            "CliffsNotes on Tolkien's The Lord of the Rings & The Hobbit",
            "A Hobbit Devotional",
            "Hobbit",
            "LEGO The Hobbit"
          ]
        }
    assert response.status_code == 200
    assert response.json() == body


def test_read_books_published_date():
    response = client.get('/books?published_date=2004')
    body = {
          "titles": [
            "Hobbit czyli Tam i z powrotem"
          ]
        }
    assert response.status_code == 200
    assert response.json() == body


def test_read_books_published_date_invalid():
    response = client.get('/books?published_date=000')
    body = {
      "titles": []
    }
    assert response.status_code == 200
    assert response.json() == body


def test_read_booksID():
    response = client.get('books/YyXoAAAACAAJ')
    body = {
          "title": "Hobbit czyli Tam i z powrotem",
          "authors": [
            "J. R. R. Tolkien"
          ],
          "publishedDate": "2004",
          "categories": [
            "Baggins, Bilbo (Fictitious character)"
          ],
          "averageRating": 5,
          "ratingsCount": 3,
          "imageLinks": {
            "thumbnail": "http://books.google.com/books/content?id=YyXoAAAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
          }
        }
    assert response.status_code == 200
    assert response.json() == body


def test_db_post():
    response = client.post('/db')
    assert response.status_code == 422


def test_books_list_after_update():
    response = client.get('/books')
    body = {
          "titles": [
            "Hobbit czyli Tam i z powrotem",
            "Hobbit",
            "LEGO The Hobbit",
            "The Hobbit",
            "The History of the Hobbit",
            "I Am in Fact a Hobbit",
            "Finding God in the Hobbit",
            "CliffsNotes on Tolkien's The Lord of the Rings & The Hobbit",
            "A Hobbit Devotional",
            "War",
            "War Labor Reports ...",
            "The Vietnam War",
            "The First War Correspondent",
            "Absolute War",
            "The Face of War",
            "War, Literature, and the Arts",
            "The War in Vietnam",
            "Report to the Membership of the Wisconsin War Fund",
            "Preventive medicine in World War II. 1969 v. 9"
          ]
        }



def main():
    test_read_books()
    test_read_books()
    test_read_booksID()
    test_read_books_sorted()
    test_read_books_published_date()
    test_read_books_published_date_invalid()
    test_db_post()


if __name__ == '__main__':
    main()
