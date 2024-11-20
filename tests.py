import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books_two_books_in_the_dict(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # ------словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2 ---
        # !!!------ такого словаря и метода в исходном коде нет, поэтому я проверил длину по словарю books_genre, в который добавляются новые книги при работе метода add_new_book

        assert len(collector.books_genre) == 2


    name_genre = [['Оно', 'Ужасы'],
                  ['Ревизор', 'Комедии'],
                  ]

        # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_invalid_lenhth_empty_dict(self):      # 1 Проверка на добавление книги с длинным названием
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить Что делать, если ваш кот хочет вас убить Что делать, если ваш кот хочет вас убить')  # Превышение длины
        assert len(collector.books_genre) == 0

    @pytest.mark.parametrize('name,genre', name_genre)
    def test_set_book_genre_set_genre_book_has_a_genre(self, name, genre):      # 2 Проверка на добавление жанра у книги
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    @pytest.mark.parametrize('name,genre', [['Оно', 'Ужастик'],
                                            ['Ревизор', 'Комедия'],
                                            ])
    def test_set_book_genre_set_of_unknown_genre_book_has_no_genre(self, name, genre):      # 3 Проверка на попытку ввода неизвестного жанра
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == ''

    @pytest.mark.parametrize('name,genre', name_genre)
    def test_get_book_genre_ask_genre_get_book_genre(self, name, genre):  # 4 Проверка на получение жанра книги по названию
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_book_genre_unknown_book_entry_is_none (self):      # 5 Проверка получения жанра у книги, которой нет в словаре
        collector = BooksCollector()
        assert collector.get_book_genre("Unknown") is None


    def test_get_books_with_specific_requesting_fiction_returns_two_books(self):     # 6 Проверка выборки книг по жанру
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Оно')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер', 'Властелин колец']

    def test_get_books_with_specific_genre_another_genre_get_empty_list(self):       # 7 Проверка выборки книг по неизвестному жанру
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_books_with_specific_genre('Лит РПГ') == []

    @pytest.mark.parametrize('name,genre', name_genre)
    def test_get_book_genre_ask_genre_get_books_genre(self, name, genre):  # 8 Проверка на получение словаря books_genre
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_genre() == {name : genre}

    def test_get_books_for_children_two_different_books_one_for_children(self): # 9 Проверка на получение списка детских книг
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Оно')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_for_children() == ['Гарри Поттер']

    def test_add_book_in_favorites_add_book_book_in_favorites(self):    # 10 Проверка на наличие книги в избранном
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        assert collector.get_list_of_favorites_books() == ['Оно']

    def test_delete_book_from_favorites_add_and_delete_book_list_empty(self):    # 11 Проверка на удаление книги из избранного
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.delete_book_from_favorites('Оно')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_add_two_books_one_in_favorities(self):    # 12 Проверка получения списка избранных книг
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Оно')
        assert collector.get_list_of_favorites_books() == ['Оно']













