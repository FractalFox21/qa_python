import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    '''@pytest.fixrure
    def collector(self):
        return BooksCollector()'''
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

    def test_add_new_book_invalid_lenhth_empty_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить Что делать, если ваш кот хочет вас убить Что делать, если ваш кот хочет вас убить')  # Превышение длины
        assert len(collector.books_genre) == 0

   # def test_set_book_genre_set_:




    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()