Юнит-тесты для класса `BooksCollector`

- `test_add_new_book_invalid_nqme_not_added` — нельзя добавить книгу с пустым названием или длиннее 40 символов (параметризация)
- `test_add_new_book_added_book_has_no_genre` — у новой книги отсутствует жанр
- `test_set_book_genre_valid_genre_is_set` — жанр устанавливается, если он есть в списке
- `test_set_book_genre_invalid_genre_not_set` — жанр не устанавливается, если его нет в списке
- `test_get_book_genre_returns_correct_genre` — возвращает жанр книги по её названию
- `test_get_books_genre_returns_books_dict` — возвращает словарь с книгами и их жанрами
- `test_get_books_with_specific_genre_returns_correct_books` — возвращаются только книги нужного жанра
- `test_get_books_for_children_age_rated_books_not_included` — книги с возрастным рейтингом не попадают в детский список (параметризация)
- `test_get_books_for_children_returns_child_friendly_books` — детские книги попадают в детский список
- `test_add_book_in_favorites_book_appears_in_favorites` — книга добавляется в избранное
- `test_add_book_in_favorites_duplicate_not_added` — одну книгу нельзя добавить в избранное дважды
- `test_delete_book_from_favorites_book_removed` — книга удаляется из избранного
- `test_get_list_of_favorites_books_returns_added_books` — возвращает список добавленных в избранное книг
