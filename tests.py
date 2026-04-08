import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # Проверка метода add_new_book: параметризация для невалидных имён 
    @pytest.mark.parametrize('name', [
        '',
        'А' * 41,
    ])
    def test_add_new_book_invalid_nqme_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    #Проверка метода add_new_book: у добавленной книги нет жанра 
    def test_add_new_book_added_book_has_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        assert collector.get_book_genre('Война и мир') == ''

    # Проверка метода set_book_genre: установка валидного жанра
    def test_set_book_genre_valid_genre_is_set(self):
        collector = BooksCollector()
        collector.add_new_book('Мы')
        collector.set_book_genre('Мы', 'Фантастика')
        assert collector.get_book_genre('Мы') == 'Фантастика'

    # Проверка метода set_book_genre: невалидный жанр не устнавливается 
    def test_set_book_genre_invalid_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Мы')
        collector.set_book_genre('Мы', 'Роман')
        assert collector.get_book_genre('Мы') == ''

    # Проверка метода get_book_genre: возвращает жанр книги по её названию
    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка на луне')
        collector.set_book_genre('Незнайка на луне', 'Мультфильмы')
        assert collector.get_book_genre('Незнайка на луне') == 'Мультфильмы'

    # Проверка метода get_books_genre: возвращает словарь с книгами и их жанрами
    def test_get_books_genre_returns_books_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Ревизор')
        collector.set_book_genre('Ревизор', 'Комедии')
        assert collector.get_books_genre() == {'Ревизор': 'Комедии'}

    # Проверка метода get_books_with_specific_genre: возвращает только книги нужного жанра
    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book('Мы')
        collector.add_new_book('Вий')
        collector.set_book_genre('Мы', 'Фантастика')
        collector.set_book_genre('Вий', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Мы']

    # Проверка метода get_books_for_children: книги с возрастным рейтингом не попадают в список
    @pytest.mark.parametrize('name,genre', [
        ('Вий', 'Ужасы'),
        ('Преступление и наказание', 'Детективы'),
    ])
    def test_get_books_for_children_age_rated_books_not_included(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert name not in collector.get_books_for_children()

    # Проверка метода get_books_for_children: детские книги попадают в список 
    def test_get_books_for_children_returns_child_friendly_books(self):
        collector = BooksCollector()
        collector.add_new_book('Чебурашка')
        collector.set_book_genre('Чебурашка', 'Мультфильмы')
        assert 'Чебурашка' in collector.get_books_for_children()

    # Проверка метода  add_book_in_favorites: книга добавляется в список избранных
    def test_add_book_in_favorites_book_appears_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        assert 'Мастер и Маргарита' in collector.get_list_of_favorites_books()

    # Проверка метода add_book_in_favorites: повторное добавление книги не вносит ее в существующий список 
    def test_add_book_in_favorites_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        assert collector.get_list_of_favorites_books().count('Мастер и Маргарита') == 1

    # Проверка метода delete_book_from_favorites: книга удаляется из избранного списка
    def test_delete_book_from_favorites_book_removed(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        collector.delete_book_from_favorites('Мастер и Маргарита')
        assert 'Мастер и Маргарита' not in collector.get_list_of_favorites_books()

    # Проверка метода get_list_of_favorites_books: возвращает список добавленных в избранное книг
    def test_get_list_of_favorites_books_returns_added_books(self):
        collector = BooksCollector()
        collector.add_new_book('Собачье сердце')
        collector.add_new_book('Двенадцать стульев')
        collector.add_book_in_favorites('Собачье сердце')
        collector.add_book_in_favorites('Двенадцать стульев')
        assert collector.get_list_of_favorites_books() == ['Собачье сердце', 'Двенадцать стульев']