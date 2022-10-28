import pytest

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def author(mixer):
    return mixer.blend('books.Author', name='Пелевин')


@pytest.fixture
def book(mixer, author):
    return mixer.blend('books.Book', author=author, name='Чапаев и Пустота')


def test_book_list(api, book, author):
    result = api.get('/api/v1/books/')

    assert result[0]['id'] == book.id
    assert result[0]['name'] == 'Чапаев и Пустота'
    assert result[0]['author']['id'] == author.id
    assert result[0]['author']['name'] == 'Пелевин'


def test_book_retrieve(api, book, author):
    result = api.get(f'/api/v1/books/{book.id}/')

    assert result['id'] == book.id
    assert result['name'] == 'Чапаев и Пустота'
    assert result['author']['id'] == author.id
    assert result['author']['name'] == 'Пелевин'
