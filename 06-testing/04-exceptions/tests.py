import pytest
from book import Book


#n tests.py, write three parametrized tests:

#test_valid_creation that create books with valid title and isbn.
#test_creation_with_invalid_title that create books with an invalid title.
#test_creation_with_invalid_isbn that create books with an invalid isbn.

@pytest.mark.parametrize('title', [
    'Watchmen',
    'Harry Potter',
])
@pytest.mark.parametrize('isbn', [
    '978-1779501127',
])
def test_title(title, isbn):
    book1 = Book(title, isbn)

    assert book1.title == title
    assert book1.isbn == isbn


@pytest.mark.parametrize('title', [
    '',
])
@pytest.mark.parametrize('isbn', [
    '978-1779501127',
])
def test_title(title, isbn):
    with pytest.raises(ValueError):
        book1 = Book(title, isbn)

